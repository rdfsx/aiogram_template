import json
from datetime import datetime

from odmantic import Field, Model


class ChannelModel(Model):
    id: int = Field(primary_field=True)
    title: str = Field(...)
    link: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "Channels"
        json_loads = json.loads
