from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import quote_html
from odmantic import AIOEngine

from app.models import UserModel


async def get_default_message(m: Message, user: UserModel, db: AIOEngine):
    await m.answer(quote_html(user))


async def edit_db(m: Message, user: UserModel, db: AIOEngine):
    await db.save(UserModel(id=m.from_user.id, language='хер'))


def setup(dp: Dispatcher):
    dp.register_message_handler(edit_db, commands="edit")
    dp.register_message_handler(get_default_message)
