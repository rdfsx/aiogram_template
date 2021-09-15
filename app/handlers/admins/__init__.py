from aiogram import Dispatcher

from app.handlers.admins.admin import admin_start


def setup_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
