from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    tg_id: int = Field(...)
    language: str = Field(default='en')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "tg_id": 1234567,
                "language": "en",
            }
        }


class UpdateUser(BaseModel):
    language: Optional[str]
    tg_id: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "tg_id": 1234567,
                "language": "en",
            }
        }
