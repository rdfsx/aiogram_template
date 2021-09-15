from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models import Chat, User


class DataMiddleware(BaseMiddleware):
    @staticmethod
    async def setup_chat(data: dict, user: types.User, language: str, chat: Optional[types.Chat] = None):
        user_id = int(user.id)
        chat_id = int(chat.id)
        chat_type = chat.type if chat else "private"
        db: AsyncIOMotorDatabase = data["db"]

        if not (user := await db.User.find_one({"id": user_id})):
            await db.User.insert_one(user := User(id=user_id, language=language).dict())
        if not (chat := await db.Chat.find_one({"id": chat_id})):
            await db.Chat.insert_one(chat := Chat(id=chat_id, type=chat_type).dict())

        data["user"] = user
        data["chat"] = chat

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.from_user.language_code, message.chat)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.from_user.language_code,
                              query.message.chat if query.message else None)
