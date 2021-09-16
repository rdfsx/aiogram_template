from app.handlers.admins import setup_admin
from app.handlers.errors import setup_errors
from app.handlers.private import setup_private


def setup_all_handlers(dp):
    setup_errors(dp)
    setup_admin(dp)
    setup_private(dp)
