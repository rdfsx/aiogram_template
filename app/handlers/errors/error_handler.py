import logging

from aiogram.types import Update
from aiogram.utils.markdown import hcode


async def errors_handler(update, exception):
    text = "Вызвано необрабатываемое исключение. Перешлите это сообщение администратору.\n"
    error = f'Error: {exception}\nUpdate: {update}'
    logging.exception(error)
    await Update.get_current().message.answer(text + hcode(error))
