from aiogram import Dispatcher

from app.handlers.private.default import get_default_message
from app.handlers.private.help import get_help_message
from app.handlers.private.start import get_start_message


def setup_private(dp: Dispatcher):
    dp.register_message_handler(get_start_message, commands="start")
    dp.register_message_handler(get_help_message, commands="help")
    dp.register_message_handler(get_default_message)
