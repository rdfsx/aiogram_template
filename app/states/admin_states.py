from aiogram.dispatcher.filters.state import StatesGroup, State


class AnswerAdmin(StatesGroup):
    ANSWER = State()


class BroadcastAdmin(StatesGroup):
    BROADCAST = State()


class RefSearchAdmin(StatesGroup):
    SEARCH = State()


class AdminRef(StatesGroup):
    SET = State()


class AdminShows(StatesGroup):
    SHOWS = State()


class AdminSubscription(StatesGroup):
    SUB = State()
    LINK = State()
