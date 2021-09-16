from aiogram.types import Message


async def get_default_message(m: Message):
    await m.answer(m.text)
