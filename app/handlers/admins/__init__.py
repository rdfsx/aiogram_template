import importlib
import os

from aiogram import Dispatcher


def setup(dp: Dispatcher, directory: str):
    for module in os.listdir(os.path.dirname(__file__)):
        if module not in ['__init__.py', '__pycache__']:
            (importlib.import_module(f"app.handlers.{directory}.{module}".replace(".py", ''))).setup(dp)

