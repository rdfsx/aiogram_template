from aiogram.types import Message


async def get_starting_message(m: Message):
    await m.answer(f"Hello there, {m.from_user.first_name}!")
