from aiogram import Dispatcher
from aiogram.types import Message
from odmantic import AIOEngine

from app.models import UserModel


async def get_default_message(m: Message, user: UserModel, db: AIOEngine):
    await m.answer("Привет.")


def setup(dp: Dispatcher):
    dp.register_message_handler(get_default_message)
