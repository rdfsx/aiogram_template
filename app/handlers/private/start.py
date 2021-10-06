from aiogram.types import Message, CallbackQuery
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.keyboards.inline import LanguageMarkup
from app.models import UserModel
from app.models.user import UserUpdateModel


async def get_start_message(m: Message):
    await m.answer("🇷🇺 Выберите язык:\n\n"
                   "🇬🇧 Choose your language:", reply_markup=LanguageMarkup().get())


async def set_user_language(query: CallbackQuery, db: AsyncIOMotorDatabase, callback_data: dict):
    await query.answer()
    language = callback_data.get('value')
    update_user = UserUpdateModel(set_language=language)
    await db.UserModel.update_one({"id": query.from_user.id}, {"$set": update_user.dict(exclude_none=True)})
    _ = i18n = query.bot['i18n']
    i18n.ctx_locale.set(language)
    await query.message.answer(_("Привет! Это бот."))
    await query.message.delete()
