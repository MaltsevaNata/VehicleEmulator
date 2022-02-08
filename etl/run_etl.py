import logging
from logging import config as logging_config

import asyncio

from services.wshandler import WSHandler
from core.config import Config
from core.logger import LOGGING

if __name__ == '__main__':
    config = Config()
    logging_config.dictConfig(LOGGING)
    logger = logging.getLogger(__name__)
    ws = WSHandler(config, logger)
    asyncio.run(ws.run())
