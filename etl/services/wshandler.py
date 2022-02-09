import logging
import json

from aiohttp import WSMessage, WSMsgType, ClientSession

from core.config import Config
from core.message import Message
from db.storage import Storage


class WSHandler:
    def __init__(self, config: Config, logger: logging.Logger, storage: Storage):
        self.config = config
        self.logger = logger
        self.storage = storage

    async def handle_message(self, msg: WSMessage):
        if msg.type == WSMsgType.TEXT:
            try:
                msg_json = json.loads(msg.data)
                message = Message(**msg_json)
                result = await self.storage.create(message.dict())
                self.logger.debug(f"Added document: {result}")
            except json.decoder.JSONDecodeError:
                self.logger.debug(f"Invalid message: {msg}")

    async def run(self):
        self.logger.info(f"ETL process started: getting websocket messages and writing them in MongoDB...")
        async with ClientSession() as session:
            async with session.ws_connect(self.config.dg_url) as ws:
                async for msg in ws:
                    await self.handle_message(msg)
