from aiogram import Dispatcher

from app.handlers.private.start import get_start_message


def setup_private(dp: Dispatcher):
    dp.register_message_handler(get_start_message, commands=["start"])
