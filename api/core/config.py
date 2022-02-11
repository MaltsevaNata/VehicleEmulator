import os

from pydantic import BaseModel


class Config(BaseModel):
    mongo_host: str = os.getenv("MONGO_HOST", "localhost")
    mongo_port: int = int(os.getenv("MONGO_PORT", 27017))
    mongo_db: str = os.getenv("MONGO_DB", "vehicles")
    mongo_collection: str = os.getenv("MONGO_COLLECTION", "components")
