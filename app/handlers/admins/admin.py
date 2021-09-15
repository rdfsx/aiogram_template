from aiogram.types import Message


async def admin_start(m: Message):
    await m.reply("Hello, admin!")
