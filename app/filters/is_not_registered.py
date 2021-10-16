from aiogram import types, Bot
from aiogram.dispatcher.filters import BoundFilter
from odmantic import AIOEngine

from app.models import UserModel, UserRoles


class NotRegisteredFilter(BoundFilter):
    key = 'is_not_registered'

    def __init__(self, is_not_registered):
        self.is_not_registered = is_not_registered

    async def check(self, m: types.Message):
        bot: Bot = m.bot
        db: AIOEngine = bot["db"]
        user_db = await db.find_one(UserModel, UserModel.id == m.from_user.id)
        if user_db.role == UserRoles.new.value:
            return True
        return False
