from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models import ChatModel, UserModel
from app.utils.notifications.new_notify import notify_new_user


class ACLMiddleware(BaseMiddleware):
    @staticmethod
    async def setup_chat(data: dict, user: types.User, language: str, chat: Optional[types.Chat] = None):
        user_id = int(user.id)
        chat_id = int(chat.id)
        chat_type = chat.type if chat else "private"
        db: AsyncIOMotorDatabase = chat.bot["db"]

        if not (user_db := await db.UserModel.find_one({"id": user_id})):
            await db.UserModel.insert_one(user_db := UserModel(id=user_id, language=language).dict())
            await notify_new_user(user)
        if not (chat_db := await db.ChatModel.find_one({"id": chat_id})):
            await db.ChatModel.insert_one(chat_db := ChatModel(id=chat_id, type=chat_type).dict())

        data["user"]: UserModel = UserModel.parse_obj(user_db)
        data["chat"]: ChatModel = ChatModel.parse_obj(chat_db)

        data["db"]: AsyncIOMotorDatabase = db
        data["_"] = chat.bot['i18n'].gettext

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.from_user.language_code, message.chat)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.from_user.language_code,
                              query.message.chat if query.message else None)
