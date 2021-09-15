import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.utils.executor import start_polling

from app import handlers, middlewares
from app.config import Config
from app.utils import logger
from app.utils.startup_notify import notify_superusers


async def on_startup(dp):
    middlewares.setup(dp)
    # Setup handlers
    handlers.setup(dp)

    logger.setup_logger()

    # Notify superusers
    await notify_superusers(Config.admins)


async def on_shutdown(dp):
    logging.warning("Shutting down..")
    await dp.bot.session.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bye!")


def main():
    bot = Bot(token=Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MongoStorage()
    dp = Dispatcher(bot, storage=storage)

    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
