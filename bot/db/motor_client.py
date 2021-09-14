import motor.motor_asyncio as m_m_a

from bot.config import MONGODB_URI, MONGODB_DATABASE


class SingletonClient:
    client = None
    db = None

    @staticmethod
    def get_client():
        if SingletonClient.client is None:
            SingletonClient.client = m_m_a.AsyncIOMotorClient(MONGODB_URI)

        return SingletonClient.client

    @staticmethod
    def get_data_base():
        if SingletonClient.db is None:
            client = SingletonClient.get_client()
            SingletonClient.db = client[MONGODB_DATABASE]

        return SingletonClient.db
