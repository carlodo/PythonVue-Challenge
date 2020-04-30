import jwt
import bcrypt
import pymongo

from json import JSONDecodeError
from aiohttp import web
from datetime import datetime, timedelta


routes = web.RouteTableDef()
db = pymongo.MongoClient('db').moti

JWT_SECRET = open('/run/secrets/authkey').read()
assert len(JWT_SECRET) > 512/8  # Keys smaller than 512 bytes are not secure.


@web.middleware
async def auth_middleware(request, handler):
    """
    Intercept request and inject `user` property that contains:
      - `user_id` from a valid auth token, or
      - `None` if no token is presented.
    Return 401 error if an invalid token or header is presented.
    """
    token = request.headers.get('authorization')
    if token:
        token = token.split()
        if len(token) != 2 or token[0].lower() != 'bearer':
            err = {'error': "Invalid authentication header."}
            return web.json_response(err, status=401)
        try:
            token = jwt.decode(token[1], JWT_SECRET, 'HS256')
        except jwt.DecodeError:
            err = {'error': "Authentication token is invalid."}
            return web.json_response(err, status=401)
        except jwt.ExpiredSignatureError:
            err = {'error': "Authentication token is expired."}
            return web.json_response(err, status=401)
    request.user = token['user_id'] if token else None
    return await handler(request)


def auth_required(func):
    """
    Decorator required for non-public aiohttp web functions. Return 401 error
    if request has no authentication.
    """
    async def wrapper(request):
        if request.user:
            return await func(request)
        return web.json_response({'error': "Please log in."}, status=401)
    return wrapper


@routes.post('/auth/')
async def auth(request):
    """
    Handle login request. Check credentials and return authentication token.
    """
    try:
        post = await request.json()
    except JSONDecodeError:
        return web.json_response({'error': "Invalid JSON data."}, status=400)

    email = post.get('email', '').lower().strip()
    password = post.get('password', '')
    if not (email and password):
        return web.json_response({'error': "Insufficient data."}, status=400)
    user = db.users.find_one({'email': email})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        token = issue_token(user['_id'])
        return web.json_response({'token': token})
    err = "Email address and password do not match."
    return web.json_response({'error': err}, status=401)


@routes.post('/signup/')
async def signup(request):
    """
    Create a new user with name, email and password.
    """
    try:
        post = await request.json()
    except JSONDecodeError:
        return web.json_response({'error': "Invalid JSON data."}, status=400)
    name = post.get('name', '').strip()
    email = post.get('email', '').strip()
    password = post.get('password')
    if not (name and email and password):
        return web.json_response({'error': "Insufficient data."}, status=400)

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {'name': name,
            'email': email.lower(),
            'password': hashed,
            'created': datetime.utcnow(),
            'team': None}
    try:
        db.users.insert_one(user)
    except pymongo.errors.DuplicateKeyError:
        err = "A user with this email address already exists."
        return web.json_response({'error': err}, status=409)
    return web.json_response({'message': "New user created."}, status=201)


def issue_token(user_id, duration=1):
    """
    Issue a token containing user_id and an expiry date.
    """
    tok = {
        'user_id': str(user_id),
        'exp': datetime.utcnow() + timedelta(hours=duration)
    }
    return jwt.encode(tok, JWT_SECRET, 'HS256').decode('utf-8')
