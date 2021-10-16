import asyncio
from contextlib import suppress

import aiofiles.os
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InputFile, CallbackQuery
from odmantic import AIOEngine

from app.models import UserModel


async def get_amount_users(m: Message, db: AIOEngine):
    amount = await db.count(UserModel)
    await m.answer(f"Количество пользователей в базе данных: {amount}")


async def get_exists_users(m: Message, db: AIOEngine):
    await m.answer("Начинаем подсчет...")
    bot = m.bot
    users = await db.find(UserModel)
    count = 0
    for user in users:
        with suppress(Exception):
            if await bot.send_chat_action(user.id, "typing"):
                count += 1
        await asyncio.sleep(.05)
    await m.answer(f"Активных пользователей: {count}")


async def write_users_to_file(m: Message, db: AIOEngine):
    await m.answer("Начинаем запись...")
    users = await db.find(UserModel)
    filename = 'users.txt'
    async with aiofiles.open(filename, mode='w') as f:
        for user in users:
            await f.write(f"{user.id}\n")
    await m.answer_document(InputFile(filename))
    await aiofiles.os.remove(filename)


async def cancel_all(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.delete()
    await call.message.answer('Отменено.')


def setup(dp: Dispatcher):
    dp.register_message_handler(get_amount_users, commands="amount", is_admin=True)
    dp.register_message_handler(get_exists_users, commands="exists_amount", is_admin=True)
    dp.register_message_handler(write_users_to_file, commands="users_file", is_admin=True)
    dp.register_callback_query_handler(cancel_all, text='cancel', state='*', is_admin=True)
