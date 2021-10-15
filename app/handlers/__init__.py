import importlib
import os

from aiogram import Dispatcher


def setup_all_handlers(dp: Dispatcher):
    for module in os.listdir(os.path.dirname(__file__)):
        if module not in ['__init__.py', '__pycache__']:
            (importlib.import_module(f"app.handlers.{module}")).setup(dp, module)
