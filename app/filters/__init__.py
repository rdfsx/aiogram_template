from aiogram import Dispatcher

from .is_admin import AdminFilter
from .is_not_member import NotMemberFilter
from .is_not_registered import NotRegisteredFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(NotRegisteredFilter)
    dp.filters_factory.bind(NotMemberFilter)
