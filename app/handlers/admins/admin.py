import asyncio
import logging

from aiogram import Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_broadcaster import MessageBroadcaster
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.keyboards.inline import CancelMarkup
from app.states.admin_states import BroadcastAdmin


async def broadcast(m: Message):
    await BroadcastAdmin.BROADCAST.set()
    await m.answer('Введите сообщение, которое хотели бы отправить всем, кто есть в базе:',
                   reply_markup=CancelMarkup().get())


async def cancel_broadcast(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.answer()
    await call.message.answer('Отменено.')


async def start_broadcasting(m: Message, state: FSMContext, db: AsyncIOMotorDatabase):
    chats = await db.User.find().to_list(None)
    result = []
    for chat in chats:
        result.append(chat['id'])
    broadcaster = MessageBroadcaster(chats=result, message=m)
    await state.reset_state()
    await m.answer("Рассылка запущена.")
    await broadcaster.run()
    await m.answer(f"Отправлено {len(broadcaster._successful)} сообщений.")


async def get_amount_users(m: Message, db: AsyncIOMotorDatabase):
    amount = await db.User.count_documents({})
    await m.answer(f"Количество пользователей в базе данных: {amount}")


async def get_exists_users(m: Message, db: AsyncIOMotorDatabase):
    bot = Bot.get_current()
    users = await db.User.find().to_list(None)
    count = 0
    await m.answer("Начинаем подсчет...")
    for user in users:
        try:
            if await bot.send_chat_action(user['id'], "typing"):
                count += 1
        except Exception as e:
            logging.exception(e)
        await asyncio.sleep(.05)
    await m.answer(f"Активных пользователей: {count}")
