from aiogram import Dispatcher, types

from app.config import Config
from app.handlers.admins.admin import broadcast, cancel_broadcast, start_broadcasting, get_amount_users, \
    get_exists_users
from app.states.admin_states import BroadcastAdmin


def setup_admin(dp: Dispatcher):
    dp.register_message_handler(broadcast, commands="broadcast", user_id=Config.ADMINS)
    dp.register_callback_query_handler(cancel_broadcast, text='cancel', state='*', user_id=Config.ADMINS)
    dp.register_message_handler(start_broadcasting, state=BroadcastAdmin.BROADCAST, user_id=Config.ADMINS,
                                content_types=types.ContentType.ANY)
    dp.register_message_handler(get_amount_users, commands="amount", user_id=Config.ADMINS)
    dp.register_message_handler(get_exists_users, commands="exists_amount", user_id=Config.ADMINS)
