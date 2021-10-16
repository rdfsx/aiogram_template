from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatMemberStatus, CallbackQuery
from odmantic import AIOEngine

from app.keyboards.inline import CancelKb, AdminChannelsListKb, AdminDeleteChannelKb
from app.models import ChannelModel
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
    channel = await m.bot.get_chat(data["channel_id"])
    if await db.find_one(ChannelModel, ChannelModel.id == channel.id):
        await state.reset_state()
        return await m.answer("Канал уже был добавлен ранее.")
    await db.save(ChannelModel(id=channel.id, title=channel.title, link=m.text))
    await state.reset_state()
    await m.answer("Канал был успешно добавлен для подписки.")


async def manage_channels(m: Message, db: AIOEngine):
    if not (channels := await db.find(ChannelModel)):
        return await m.answer("Список каналов пуст.")
    await m.answer("Вот список каналов:", reply_markup=AdminChannelsListKb().get(channels))


async def manage_channel(query: CallbackQuery, callback_data: dict, db: AIOEngine):
    await query.answer()
    channel_id = callback_data["channel_id"]
    if not (channel := await db.find_one(ChannelModel, ChannelModel.id == int(channel_id))):
        return await query.message.answer("Такого канала уже нет.")
    await query.message.answer(f"Канал: {channel.link}", reply_markup=AdminDeleteChannelKb().get(channel_id))


async def delete_channel(query: CallbackQuery, callback_data: dict, db: AIOEngine):
    await query.message.delete()
    channel_id = callback_data["channel_id"]
    if channel := await db.find_one(ChannelModel, ChannelModel.id == int(channel_id)):
        await db.delete(channel)
        return await query.message.answer("Канала удалён.")
    await query.message.answer("Канала и не было.")


def setup(dp: Dispatcher):
    dp.register_message_handler(add_subscription, commands="add_channel", is_admin=True)
    dp.register_message_handler(get_channel_message, state=AdminSubscription.SUB, is_admin=True,
                                content_types=types.ContentType.ANY)
    dp.register_message_handler(set_channel_link, state=AdminSubscription.LINK, is_admin=True)
    dp.register_message_handler(manage_channels, commands="channel_list", is_admin=True)
    dp.register_callback_query_handler(manage_channel, AdminChannelsListKb.callback_data.filter(), is_admin=True)
    dp.register_callback_query_handler(delete_channel, AdminDeleteChannelKb.callback_data.filter(), is_admin=True)
