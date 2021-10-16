from aiogram import types, Bot
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import ChatMemberStatus
from odmantic import AIOEngine

from app.models import ChannelModel


class NotMemberFilter(BoundFilter):
    key = 'is_not_member'

    def __init__(self, is_not_member):
        self.is_not_member = is_not_member

    async def check(self, m: types.Message):
        bot: Bot = m.bot
        db: AIOEngine = bot["db"]
        if not (channels := await db.find(ChannelModel)):
            return False
        for channel in channels:
            if (await bot.get_chat_member(channel.id, m.from_user.id)).status == ChatMemberStatus.LEFT or None:
                return True
        return False
