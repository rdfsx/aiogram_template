from aiogram import Dispatcher

from app.handlers.private.start import get_starting_message


def setup_private(dp: Dispatcher):
    dp.register_message_handler(get_starting_message, commands=["start"])
