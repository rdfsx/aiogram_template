from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatMemberStatus
from odmantic import AIOEngine

from app.keyboards.inline import CancelKb
from app.states.admin_states import AdminSubscription


async def add_subscription(m: Message):
    await AdminSubscription.SUB.set()
    await m.answer("Назначьте бота админом в канале, затем перешлите любое сообщение из канала сюда:",
                   reply_markup=CancelKb().get())


async def get_channel_message(m: Message, state: FSMContext):
    if not m.forward_from_chat:
        return await m.answer("Вы отправили не пересланное сообщение! Перешлите сообщение из канала:",
                              reply_markup=CancelKb().get())
    bot = m.bot
    bot_me = await bot.get_me()
    if m.forward_from_chat.type == "channel":
        ans = await bot.get_chat_member(m.forward_from_chat.id, bot_me.id)
        if ans.status == ChatMemberStatus.ADMINISTRATOR:
            await state.update_data(channel_id=m.forward_from_chat.id)
            await AdminSubscription.LINK.set()
            await m.answer(f"Принятно. Теперь пришлите ссылку, по которой люди должны будут вступать (в формате t.me)",
                           reply_markup=CancelKb().get())


async def set_channel_link(m: Message, state: FSMContext, db: AIOEngine):
    if "t.me" not in m.text:
        return await m.answer("Неверная ссылка! Ссылка должна начинаться на t.me")
    data = await state.get_data()
    chat = await m.bot.get_chat(data["channel_id"])
    with suppress(DuplicateKeyError):
        await db.ChannelModel.insert_one(ChannelModel(id=chat.id, title=chat.title, link=m.text).dict(by_alias=True))
    await state.reset_state()
    await m.answer("Канал был успешно добавлен для подписки.")


async def manage_channels(m: Message, db: AsyncIOMotorDatabase):
    if not (channels := await db.ChannelModel.find().to_list(None)):
        return await m.answer("Список каналов пуст.")
    await m.answer("Вот список каналов:", reply_markup=AdminChannelsListKb().get(channels))


async def manage_channel(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    channel_id = callback_data["channel_id"]
    bot = call.bot
    chat = await bot.get_chat(channel_id)
    await call.message.answer(f"Канал: {chat.invite_link}", reply_markup=AdminDeleteChannelKb().get(channel_id))


async def delete_channel(call: types.CallbackQuery, callback_data: dict, db: AsyncIOMotorDatabase):
    channel_id = callback_data["channel_id"]
    await db.ChannelModel.delete_one({"_id": int(channel_id)})
    await call.message.edit_text("Канал удалён.")