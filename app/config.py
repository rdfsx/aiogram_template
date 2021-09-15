from typing import NamedTuple

from environs import Env

env = Env()
env.read_env()


class Config(NamedTuple):
    BOT_TOKEN = env.str('BOT_TOKEN')
    STATISTICS_TOKEN = env.str('STATISTICS_TOKEN')

    admins = [
        env.str('ADMIN_ID')
    ]

    MONGODB_DATABASE = env.str('MONGODB_DATABASE')
    MONGODB_USERNAME = env.str('MONGODB_USERNAME')
    MONGODB_PASSWORD = env.str('MONGODB_PASSWORD')
    MONGODB_HOSTNAME = env.str('MONGODB_HOSTNAME')
    MONGODB_PORT = env.str('MONGODB_PORT')
    MONGODB_URI = 'mongodb://'

    if MONGODB_USERNAME and MONGODB_PASSWORD:
        MONGODB_URI += f"{MONGODB_USERNAME}:{MONGODB_PASSWORD}@"
    MONGODB_URI += f"{MONGODB_HOSTNAME}:{MONGODB_PORT}" if MONGODB_HOSTNAME else f"localhost:{MONGODB_PORT}"
