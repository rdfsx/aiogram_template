from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import quote_html
from odmantic import AIOEngine

from app.keyboards.inline import AdminShowsSettingsKb, CancelKb
from app.models import ShowsModel
from app.states.admin_states import AdminShows


async def get_shows_menu(m: Message):
    await m.answer("Выберите действие:", reply_markup=AdminShowsSettingsKb().get())


async def display_shows(query: CallbackQuery,  db: AIOEngine):
    await query.answer()
    shows = await db.find(ShowsModel)
    if not shows:
        return await query.message.answer("Нет показов.")
    await query.message.answer(shows[0].text)


async def set_shows_text(query: CallbackQuery):
    await AdminShows.SHOWS.set()
    await query.message.delete()
    await query.message.answer("Введите текст:", reply_markup=CancelKb().get())


async def create_shows_text(m: Message, db: AIOEngine, state: FSMContext):
    await db.save(ShowsModel(text=quote_html(m.text)))
    await state.reset_state()
    await m.answer("ОК, текст для показов добавлен.")


async def delete_shows_text(query: CallbackQuery, db: AIOEngine):
    await query.message.delete()
    shows = await db.find(ShowsModel)
    if not shows:
        return await query.message.answer("Нет показов.")
    await db.delete(shows[0])
    await query.message.answer("Показы удалены.")


def setup(dp: Dispatcher):
    dp.register_message_handler(get_shows_menu, commands="shows", is_admin=True)
    dp.register_callback_query_handler(display_shows, text=AdminShowsSettingsKb.display_shows, is_admin=True)
    dp.register_callback_query_handler(set_shows_text, text=AdminShowsSettingsKb.add_shows, is_admin=True)
    dp.register_message_handler(create_shows_text, state=AdminShows.SHOWS, is_admin=True)
    dp.register_callback_query_handler(delete_shows_text, text=AdminShowsSettingsKb.delete_shows, is_admin=True)
