import os

from pydantic import BaseModel


class Config(BaseModel):
    dg_host: str = os.getenv("DATA_GENERATOR_HOST", "localhost")
    dg_port: int = int(os.getenv("DATA_GENERATOR_PORT", 8000))
    dg_url: str = f"http://{dg_host}:{dg_port}/"

    mongo_host: str = os.getenv("MONGO_HOST", "localhost")
    mongo_port: int = int(os.getenv("MONGO_PORT", 27017))
    mongo_db: str = os.getenv("MONGO_DB", "vehicles")
    mongo_collection: str = os.getenv("MONGO_COLLECTION", "components")


