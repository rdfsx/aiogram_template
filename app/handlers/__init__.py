from app.handlers.admins import setup_admin
from app.handlers.private import setup_private


def setup_all_handlers(dp):
    setup_admin(dp)
    setup_private(dp)
