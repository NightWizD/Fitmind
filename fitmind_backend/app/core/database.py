import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

logger = logging.getLogger(__name__)

client: AsyncIOMotorClient = None

async def connect_to_mongo():
    global client
    try:
        client = AsyncIOMotorClient(settings.mongodb_url)
        await client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise

def close_mongo_connection():
    global client
    if client:
        client.close()
        logger.info("Disconnected from MongoDB")

def get_database():
    return client.fitmind_ai
