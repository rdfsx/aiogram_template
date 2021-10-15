import json
from datetime import datetime

from odmantic import Field, Model


class ChatModel(Model):
    id: int = Field(primary_field=True)
    type: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "Chats"
        json_loads = json.loads
