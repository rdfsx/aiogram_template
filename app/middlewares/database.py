from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types.base import TelegramObject
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient

from app.models.motor_client import MongoClient


class DatabaseMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['update']

    def __init__(self):
        super(DatabaseMiddleware, self).__init__()

    async def pre_process(self, obj: TelegramObject, data: dict, *args):
        client = MongoClient()
        db = await client.get_db()
        data["client"]: MongoClient = client
        data["db"]: AsyncIOMotorDatabase = db

    async def post_process(self, obj: TelegramObject, data: dict, *args):
        if client := data.get('client', None):
            await client.close()
