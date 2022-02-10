from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import InsertOneResult

from db.storage import Storage


class AsyncMongoStorage(Storage):
    def __init__(self, client: AsyncIOMotorClient, db: str, collection: str):
        super().__init__()
        self.db = db
        self.collection = collection
        self.client = client

    async def create(self, document: dict) -> InsertOneResult:
        return await self.client[self.db][self.collection].insert_one(document)

    async def get(self, spec: dict) -> dict:
        return await self.client[self.db][self.collection].find_one(spec)
