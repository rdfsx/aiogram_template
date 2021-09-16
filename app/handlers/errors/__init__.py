from aiogram import Dispatcher

from app.handlers.errors.error_handler import errors_handler


def setup_errors(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
