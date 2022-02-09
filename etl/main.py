import logging
from logging import config as logging_config

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from db.mongo_storage import AsyncMongoStorage
from services.wshandler import WSHandler
from core.config import Config
from core.logger import LOGGING

config = Config()
logging_config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
client = AsyncIOMotorClient(
        host=config.mongo_host,
        port=config.mongo_port
    )
client.get_io_loop = asyncio.get_running_loop
storage = AsyncMongoStorage(db=config.mongo_db, collection=config.mongo_collection, client=client)
ws = WSHandler(config, logger, storage)


if __name__ == '__main__':
    try:
        asyncio.run(ws.run(), debug=False)
    finally:
        client.close()


