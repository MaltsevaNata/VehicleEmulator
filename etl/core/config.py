import os

from pydantic import BaseModel


class Config(BaseModel):
    dg_host: str = os.getenv("data_generator_host", "127.0.0.1")
    dg_port: int = os.getenv("data_generator_port", 8000)
    data_endpoint: str = f"http://{dg_host}:{dg_port}/"

