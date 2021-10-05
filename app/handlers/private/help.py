from aiogram.types import Message

from app.middlewares import i18n


async def get_help_message(m: Message, _: i18n):
    await m.answer(_("Это бот."))
