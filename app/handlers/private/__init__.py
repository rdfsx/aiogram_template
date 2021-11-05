from aiogram import Dispatcher

from app.handlers.private import default, help_, start


def setup(dp: Dispatcher):
    for module in (start, default, help_):
        module.setup(dp)
