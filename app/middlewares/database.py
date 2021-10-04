from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types.base import TelegramObject
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.motor_client import MongoClient


class DatabaseMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['update']

    def __init__(self):
        super(DatabaseMiddleware, self).__init__()

    async def pre_process(self, obj: TelegramObject, data: dict, *args):
        data["client"]: MongoClient = obj.bot["client"]
        data["db"]: AsyncIOMotorDatabase = obj.bot["db"]

    async def post_process(self, obj: TelegramObject, data: dict, *args):
        pass
