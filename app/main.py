import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.utils.executor import start_polling
from motor.motor_asyncio import AsyncIOMotorDatabase

from app import handlers, middlewares, filters
from app.config import Config
from app.middlewares import I18nMiddleware
from app.models.base import MongoClient
from app.utils import logger
from app.utils.notifications.startup_notify import notify_superusers
from app.utils.set_bot_commands import set_commands


async def on_startup(dp):
    middlewares.setup(dp)
    filters.setup(dp)
    handlers.setup_all_handlers(dp)
    logger.setup_logger()

    client = MongoClient()
    db = await client.get_db()

    dp.bot["client"]: MongoClient = client
    dp.bot["db"]: AsyncIOMotorDatabase = db

    await notify_superusers(Config.ADMINS)
    await set_commands(dp)


async def on_shutdown(dp):
    logging.warning("Shutting down..")
    await dp.bot.session.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
    if client := dp.bot.get('client', None):
        await client.close()
        await client.wait_closed()
    logging.warning("Bye!")


def main():
    bot = Bot(token=Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MongoStorage(host=Config.MONGODB_HOSTNAME)
    dp = Dispatcher(bot, storage=storage)
    i18n = I18nMiddleware("bot", path=Config.LOCALES_DIR)
    bot['i18n'] = i18n

    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
