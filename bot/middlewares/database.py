from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types.base import TelegramObject
from sqlalchemy.orm import Session, sessionmaker

from bot.db.motor_client import SingletonClient


class DatabaseMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['update']

    def __init__(self, pool):
        super(DatabaseMiddleware, self).__init__()

    async def pre_process(self, obj: TelegramObject, data: dict, *args):
        db = SingletonClient.get_data_base()
        data["db"]: SingletonClient = db

    async def post_process(self, obj: TelegramObject, data: dict, *args):
        if session := data.get('session', None):
            await session.close()
