import pymongo

from aiohttp import web
from bson.objectid import ObjectId

from auth import auth_required

routes = web.RouteTableDef()
db = pymongo.MongoClient('db').moti


@auth_required
@routes.get('/dashboard/')
async def dashboard(request):
    """Placeholder for function that will generate the user's dashboard."""
    user_id = ObjectId(request.user)
    name = db.users.find_one(user_id)['name']
    return web.json_response({'name': name})
