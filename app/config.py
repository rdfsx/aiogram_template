from dataclasses import dataclass

from environs import Env


@dataclass(frozen=True)
class DbConfig:
    host: str
    password: str
    username: str
    database: str
    uri: str


@dataclass(frozen=True)
class Bot:
    token: str
    admin_ids: list[int]


@dataclass(frozen=True)
class Webhook:
    host: str
    port: int
    path: str
    url: str
    public_cert: str
    private_cert: str


@dataclass(frozen=True)
class WebApp:
    host: str
    port: int


@dataclass(frozen=True)
class Miscellaneous:
    other_params: str = None


@dataclass(frozen=True)
class Config:
    bot: Bot
    db: DbConfig
    webhook: Webhook
    webapp: WebApp
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    mongo_username = env.str("MONGODB_USERNAME")
    mongo_password = env.str("MONGODB_PASSWORD")
    mongo_hostname = env.str("MONGODB_HOSTNAME")
    mongo_port = env.str("MONGODB_PORT")
    mongo_uri = 'mongodb://'
    if mongo_username and mongo_password:
        mongo_uri += f"{mongo_username}:{mongo_password}@"
    mongo_uri += f"{mongo_hostname}:{mongo_port}"

    return Config(
        bot=Bot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
        ),
        db=DbConfig(
            host=mongo_hostname,
            password=mongo_password,
            username=mongo_username,
            database=env.str('MONGODB_DATABASE'),
            uri=mongo_uri,
        ),
        webhook=Webhook(
            host=env.str('WEBHOOK_HOST'),
            port=env.int('WEBHOOK_PORT'),
            path=env.str('WEBHOOK_PATH'),
            url=env.str('WEBHOOK_URL'),
            public_cert="webhook_cert.pem",
            private_cert="webhook_pkey.pem",
        ),
        webapp=WebApp(
            host=env.str('WEBHOOK_HOST'),
            port=env.int('WEBHOOK_PORT'),
        ),
        misc=Miscellaneous()
    )
