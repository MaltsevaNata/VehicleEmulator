import logging
import json

from aiohttp import ClientWebSocketResponse, WSMsgType, ClientSession

from core.config import Config
from core.message import Message


class WSHandler:
    def __init__(self, config: Config, logger: logging.Logger):
        self.config: Config = config
        self.logger = logger

    async def handle_message(self, ws: ClientWebSocketResponse):
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                try:
                    msg_json = json.loads(msg.data)
                    message = Message(**msg_json)
                    self.logger.debug(f"Received message: {message}")
                except json.decoder.JSONDecodeError:
                    self.logger.debug(f"Invalid message: {msg}")

    async def run(self):
        async with ClientSession() as session:
            async with session.ws_connect(self.config.data_endpoint) as ws:
                await self.handle_message(ws)
