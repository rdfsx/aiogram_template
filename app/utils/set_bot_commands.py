from aiogram import types
from aiogram.types import BotCommandScopeChat

from app.config import Config


async def set_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )
    for admin in Config.ADMINS:
        await dp.bot.set_my_commands(
            [
                types.BotCommand("amount", "Количество юзеров в бд"),
                types.BotCommand("create_ref", "Создать реф ссылку"),
                types.BotCommand("ref_list", "Получить список реф ссылок"),
                types.BotCommand("search_ref", "Получить стату конкретной ссылки"),
                types.BotCommand("shows", "Открыть меню показов"),
                types.BotCommand("add_channel", "Добавить канал для подписки"),
                types.BotCommand("channel_list", "Список каналов с подписками"),
                types.BotCommand("exists_amount", "Количество живых юзеров"),
                types.BotCommand("broadcast", "Рассылка по всем юзерам"),
                types.BotCommand("users_file", 'Записать юзеров в файл'),
            ],
            BotCommandScopeChat(admin)
        )
