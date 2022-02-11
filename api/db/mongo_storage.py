import json

from pymongo import ASCENDING
from motor.motor_asyncio import AsyncIOMotorClient
from bson import json_util

from db.storage import Storage


class AsyncMongoStorage(Storage):
    def __init__(self, client: AsyncIOMotorClient, db: str, collection: str):
        super().__init__()
        self.db = db
        self.collection = collection
        self.client = client

    async def get(self, spec: dict) -> dict:
        return await self.client[self.db][self.collection].find_one(spec)

    async def get_list(self, page_size: int = 0, page_num: int = 1) -> dict:
        page_num -= 1  # pages start from 0
        skip = page_size * page_num  # number of documents to skip
        cursor = self.client[self.db][self.collection].find().sort("component", ASCENDING).skip(skip).limit(page_size)
        raw_data = await cursor.to_list(length=page_size)
        return json.loads(json_util.dumps(raw_data))
