import logging

from aiogram.types import Update
from aiogram.utils.markdown import hcode


async def errors_handler(update: Update, exception):
    _ = update.bot["i18n"]
    text = _("Вызвано необрабатываемое исключение. Перешлите это сообщение администратору.\n\n")
    error = f'Error: {exception}\n\nUpdate: {update}'
    logging.exception(error)
    await Update.get_current().message.answer(text + hcode(error))
