from aiohttp import web

from auth import routes as auth_routes, auth_middleware
from dashboard import routes as dashboard_routes


api = web.Application(middlewares=[auth_middleware])
api.add_routes(auth_routes)
api.add_routes(dashboard_routes)

app = web.Application()
app.add_subapp('/api/', api)
