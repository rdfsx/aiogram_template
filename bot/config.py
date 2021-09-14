from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

STATISTICS_TOKEN = env.str('STATISTICS_TOKEN')

LOGS_BASE_PATH = "../"

admins = [
    env.str('ADMIN_ID')
]

MONGODB_DATABASE = env.str('MONGODB_DATABASE')
MONGODB_USERNAME = env.str('MONGODB_USERNAME')
MONGODB_PASSWORD = env.str('MONGODB_PASSWORD')
MONGODB_HOSTNAME = env.str('MONGODB_HOSTNAME')
MONGODB_PORT = env.str('MONGODB_PORT')

MONGODB_URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOSTNAME}:{MONGODB_PORT}"