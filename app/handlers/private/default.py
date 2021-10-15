from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import quote_html
from odmantic import AIOEngine
from odmantic.query import QueryExpression

from app.models import UserModel


async def get_default_message(m: Message, user: UserModel, db: AIOEngine):
    chats = await db.find(UserModel, QueryExpression({"language": "1"}))
    await m.answer(quote_html(chats))
    await m.answer(quote_html(user.dict()))


def setup(dp: Dispatcher):
    dp.register_message_handler(get_default_message)
