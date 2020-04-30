import pymongo

from aiohttp import web
from bson.objectid import ObjectId
from json import JSONDecodeError

from auth import auth_required

routes = web.RouteTableDef()
db = pymongo.MongoClient('db').moti


@auth_required
@routes.get('/dashboard/')
async def dashboard(request):
    user_id = ObjectId(request.user)
    user = db.users.find_one(user_id)
    name = user['name']
    motto = user['motto'] if 'motto' in user else ''
    return web.json_response({'name': name, 'motto': motto})


@auth_required
@routes.post('/dashboard/')
async def update(request):
    try:
        post = await request.json()
    except JSONDecodeError:
        return web.json_response({'error': "Invalid JSON data."}, status=400)
    motto = post['motto']
    db.users.update_one(
        {'_id': ObjectId(request.user)},
        {'$set': {'motto': motto}})
    return web.json_response({'motto': motto})
