from aiogram.types import Message


async def get_start_message(m: Message):
    await m.answer(f"Привет, {m.from_user.first_name}!")
