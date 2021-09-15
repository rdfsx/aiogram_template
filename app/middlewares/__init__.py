from aiogram import Dispatcher
from aiogram.contrib.middlewares.environment import EnvironmentMiddleware
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from .data import DataMiddleware
from .database import DatabaseMiddleware
from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.setup_middleware(LoggingMiddleware())
    dp.setup_middleware(EnvironmentMiddleware())
    dp.setup_middleware(DatabaseMiddleware())
    dp.setup_middleware(DataMiddleware())
    dp.setup_middleware(ThrottlingMiddleware())
