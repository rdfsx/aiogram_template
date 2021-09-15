from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_broadcaster import TextBroadcaster
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
    broadcaster = TextBroadcaster(chats=result, text=m.html_text)
    await state.reset_state()
    await m.answer("Рассылка запущена.")
    await broadcaster.run()
    await m.answer(f"Отправлено {len(broadcaster._successful)} сообщений.")
