import asyncio

from pymongo import errors
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


routes = web.RouteTableDef()


@routes.get('/components')
async def get_components(request: Request) -> Response:
    print(request.url)
    try:
        page_size = int(request.rel_url.query.get('page_size', 50))
        page_num = int(request.rel_url.query.get('page_num', 1))
    except ValueError:
        raise web.HTTPBadRequest(reason='one of the parameters is not a valid integer')
    storage = request.app['storage']
    try:
        data = await storage.get_list(page_size, page_num)
    except errors.ConnectionFailure:
        raise web.HTTPServiceUnavailable(reason='no connection to database')
    return web.json_response([doc for doc in data])


@routes.get('/waiter')
async def waiter(request):
    await asyncio.sleep(20)
    return web.Response(text='waited for 20 sec!')
