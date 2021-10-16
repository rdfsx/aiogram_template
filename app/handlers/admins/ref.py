import re

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from odmantic import AIOEngine, query

from app.keyboards.inline import CancelKb
from app.models import RefAdminModel
from app.states.admin_states import RefSearchAdmin, AdminRef


async def search_ref(m: Message):
    await RefSearchAdmin.SEARCH.set()
    await m.answer("Введите название ссылки, которую хотите найти:", reply_markup=CancelKb().get())


async def get_concrete_ref(m: Message, db: AIOEngine, state: FSMContext):
    await state.reset_state()
    if re.match(r"^[A-Za-z0-9_]*$", m.text) and len(m.text) < 20:
        if link := await db.find_one(RefAdminModel, RefAdminModel.title == m.text.lower()):
            return await m.answer(f"Показов: {link.count}")
    await m.answer("Такой ссылки нет.")


async def ref_link(m: Message):
    await m.answer("Введите имя реферальной ссылки (допускаются нижние подчеркивания, цифры и латинские буквы):",
                   reply_markup=CancelKb().get())
    await AdminRef.SET.set()


async def create_ref_link(m: Message, state: FSMContext, db: AIOEngine):
    if re.match(r"^[A-Za-z0-9_]*$", m.text) and len(m.text) < 20:
        await state.reset_state()
        bot = await m.bot.get_me()
        if await db.find_one(RefAdminModel, RefAdminModel.title == m.text.lower()):
            return await m.answer("Такая ссылка уже есть! Введите другую:", reply_markup=CancelKb().get())
        await db.save(RefAdminModel(title=m.text.lower()))
        return await m.answer(f"Реферальная ссылка создана <code>t.me/{bot.username}?start={m.text}</code>")
    await m.answer("Реферальная ссылка не создана: содержит неподдерживаемые символы или длинее 20 символов.\n\n"
                   "Попробуйте ещё раз:",
                   reply_markup=CancelKb().get())


async def get_ref_links(m: Message, db: AIOEngine):
    links = await db.find(RefAdminModel, sort=query.desc(RefAdminModel.count))
    result = [f"{link.title} - {link.count}" for link in links]
    await m.answer("Топ реферальных ссылок по переходам:\n\n" + "\n\n".join(result))


def setup(dp: Dispatcher):
    dp.register_message_handler(search_ref, commands="search_ref", is_admin=True)
    dp.register_message_handler(get_concrete_ref, state=RefSearchAdmin.SEARCH, is_admin=True)
    dp.register_message_handler(ref_link, commands="create_ref", is_admin=True)
    dp.register_message_handler(create_ref_link, state=AdminRef.SET, is_admin=True)
    dp.register_message_handler(get_ref_links, commands="ref_list", is_admin=True)
