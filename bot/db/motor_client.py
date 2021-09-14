from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from bot.config import MONGODB_URI, MONGODB_DATABASE


class SingletonClient:
    client = None
    db = None

    @staticmethod
    def get_client() -> AsyncIOMotorClient:
        if SingletonClient.client is None:
            SingletonClient.client = AsyncIOMotorClient(MONGODB_URI)

        return SingletonClient.client

    @staticmethod
    def get_data_base() -> AsyncIOMotorDatabase:
        if SingletonClient.db is None:
            client = SingletonClient.get_client()
            SingletonClient.db = client[MONGODB_DATABASE]

        return SingletonClient.db
