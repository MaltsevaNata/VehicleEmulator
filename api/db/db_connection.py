import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

client: AsyncIOMotorClient = None


async def connect_db(host, port):
    """Create database connection."""
    global client
    client = AsyncIOMotorClient(
        host=host,
        port=port
    )
    client.get_io_loop = asyncio.get_running_loop
    return client


async def close_db():
    """Close database connection."""
    client.close()
