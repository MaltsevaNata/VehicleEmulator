import logging
import json
import asyncio

from aiohttp import WSMessage, WSMsgType, ClientSession
from pydantic import ValidationError

from core.config import Config
from models.message import Message
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
            except (json.decoder.JSONDecodeError, ValidationError):
                self.logger.debug(f"Invalid message: {msg.data}")
                return
            message = Message(**msg_json)  # validates the fields and sets country if it is empty
            result = await self.storage.create(message.dict())
            self.logger.debug(f"Added document: {result.inserted_id}")
        elif msg.type == WSMsgType.ERROR:
            self.logger.warning(f"Connection error: {msg.data}")
        elif msg.type == WSMsgType.CLOSE:
            self.logger.warning("Server closed connection")

    async def bound_handle(self, sem, msg):
        async with sem:
            await self.handle_message(msg)

    async def run(self):
        self.logger.info("ETL process started: getting websocket messages and writing them in MongoDB...")
        sem = asyncio.Semaphore(30000)
        async with ClientSession() as session:
            async with session.ws_connect(self.config.dg_url) as ws:
                tasks = []
                async for msg in ws:
                    task = asyncio.create_task(self.bound_handle(sem, msg))
                    tasks.append(task)
                await asyncio.gather(*tasks)
