from aiogram import Dispatcher, types

from app.config import Config
from app.handlers.admins.admin import broadcast, cancel_broadcast, start_broadcasting, get_amount_users, \
    get_exists_users, write_users_to_file
from app.states.admin_states import BroadcastAdmin


def setup_admin(dp: Dispatcher):
    dp.register_message_handler(broadcast, commands="broadcast", is_admin=True)
    dp.register_callback_query_handler(cancel_broadcast, text='cancel', state='*', is_admin=True)
    dp.register_message_handler(start_broadcasting, state=BroadcastAdmin.BROADCAST, is_admin=True,
                                content_types=types.ContentType.ANY)
    dp.register_message_handler(get_amount_users, commands="amount", is_admin=True)
    dp.register_message_handler(get_exists_users, commands="exists_amount", is_admin=True)
    dp.register_message_handler(write_users_to_file, commands="users_file", is_admin=True)
