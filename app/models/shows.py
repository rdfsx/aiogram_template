import json
from datetime import datetime

from odmantic import Field, Model


class ShowsModel(Model):
    text: str = Field(primary_field=True)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "Shows"
        json_loads = json.loads
