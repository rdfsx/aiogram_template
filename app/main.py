import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.utils.executor import start_polling

from app import handlers, middlewares, filters
from app.config import Config, load_config
from app.utils import logger
from app.utils.certificates import get_ssh_certificate
from app.utils.notifications.startup_notify import notify_superusers
from app.utils.set_bot_commands import set_commands


async def on_startup(dp):
    config: Config = dp.bot.get('config')

    middlewares.setup(dp)
    filters.setup(dp)
    handlers.setup_all_handlers(dp)
    logger.setup_logger()

    await notify_superusers(config.bot.admin_ids)
    await set_commands(dp)

    await dp.bot.set_webhook(
        config.webhook.url,
        certificate=get_ssh_certificate(config.webhook.public_cert),
    )


async def on_shutdown(dp):
    logging.warning("Shutting down..")
    await dp.bot.session.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bye!")


def main():
    config = load_config(".env")
    bot = Bot(token=config.bot.token, parse_mode=types.ParseMode.HTML)
    storage = MongoStorage(host=config.db.host, port=config.db.port)
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
