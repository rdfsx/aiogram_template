from aiogram.dispatcher.filters.state import State, StatesGroup


class AnswerAdmin(StatesGroup):
    ANSWER = State()


class BroadcastAdmin(StatesGroup):
    BROADCAST = State()
