import json
from datetime import datetime

from odmantic import Field, Model


class RefAdminModel(Model):
    title: str = Field(...)
    count: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "RefAdmin"
        json_loads = json.loads
