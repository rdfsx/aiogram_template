from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types.base import TelegramObject
from motor.motor_asyncio import AsyncIOMotorDatabase

from bot.db.motor_client import SingletonClient


class DatabaseMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['update']

    def __init__(self, pool):
        super(DatabaseMiddleware, self).__init__()

    async def pre_process(self, obj: TelegramObject, data: dict, *args):
        db = SingletonClient.get_data_base()
        data["db"]: AsyncIOMotorDatabase = db

    async def post_process(self, obj: TelegramObject, data: dict, *args):
        pass
