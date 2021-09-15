from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Chat(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    tg_id: int = Field(...)
    type: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "tg_id": 1234567,
                "type": "private",
            }
        }


class ChatUpdate(BaseModel):
    language: Optional[str]
    tg_id: Optional[int]
    type: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "tg_id": 1234567,
                "type": "private",
            }
        }
