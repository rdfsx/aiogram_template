from aiogram import Dispatcher


def setup_errors(dp: Dispatcher):
    dp.register_errors_handler()
