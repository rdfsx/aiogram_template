from aiogram import Dispatcher

from app.config import Config
from app.handlers.admins.admin import broadcast, cancel_broadcast, start_broadcasting
from app.states.admin_states import BroadcastAdmin


def setup_admin(dp: Dispatcher):
    dp.register_message_handler(broadcast, commands=["broadcast"], is_admin=True)
    dp.register_callback_query_handler(cancel_broadcast, text='cancel', state='*', user_id=Config.admins)
    dp.register_message_handler(start_broadcasting, state=BroadcastAdmin.BROADCAST, user_id=Config.admins)
