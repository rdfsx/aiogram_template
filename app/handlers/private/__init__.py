from aiogram import Dispatcher

from app.handlers import start


def setup_private(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
