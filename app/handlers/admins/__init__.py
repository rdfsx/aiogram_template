from aiogram import Dispatcher

from app.handlers.admins import broadcast, commands, ref, shows


def setup(dp: Dispatcher):
    for module in (broadcast, commands, ref, shows):
        module.setup(dp)
