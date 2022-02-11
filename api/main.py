import asyncio
import logging
from logging import config as logging_config

from aiohttp import web

from core.config import Config
from core.logger import LOGGING
from db.db_connection import connect_db, close_db
from db.mongo_storage import AsyncMongoStorage
from views.components import routes

config = Config()
logging_config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


async def on_startup(app):
    client = await connect_db(host=app["config"].mongo_host, port=app["config"].mongo_port)
    storage = AsyncMongoStorage(db=config.mongo_db, collection=config.mongo_collection, client=client)
    app["storage"] = storage


async def on_shutdown(app):
    await close_db()


async def main():
    app = web.Application(logger=logger)
    app['config'] = config
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 5000)
    await site.start()
    # wait forever, running the web server
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())
