from aiogram.types import Message


async def get_help_message(m: Message):
    await m.answer("Это бот.")
