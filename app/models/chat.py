from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Chat(BaseModel):
    id: int = Field(...)
    type: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 123456789,
                "type": "private",
            }
        }


class ChatUpdate(BaseModel):
    type: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 123456789,
                "type": "private",
            }
        }
