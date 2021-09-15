from typing import Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config import Config


class MongoClient:
    def __init__(self, db_name=Config.MONGODB_DATABASE, uri=Config.MONGODB_URI):
        self._db_name: str = db_name
        self._uri = uri

        self._client: Optional[AsyncIOMotorClient] = None
        self._db: Optional[AsyncIOMotorDatabase] = None

    async def get_client(self) -> AsyncIOMotorClient:
        if isinstance(self._client, AsyncIOMotorClient):
            return self._client

        self._client = AsyncIOMotorClient(self._uri)
        return self._client

    async def get_db(self) -> AsyncIOMotorDatabase:
        if isinstance(self._db, AsyncIOMotorDatabase):
            return self._db

        client = await self.get_client()
        self._db = client.get_database(self._db_name)

        return self._db

    async def close(self):
        if self._client:
            self._client.close()

    @staticmethod
    async def wait_closed():
        return True
