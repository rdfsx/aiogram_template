from aiogram.types import Message


async def start(m: Message):
    await m.answer(f"Hello there, {m.from_user.first_name}!")
