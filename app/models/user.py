from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(...)
    language: str = Field(default='en')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": 12345678,
                "language": "en",
            }
        }


class UserUpdate(BaseModel):
    language: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": 12345678,
                "language": "en",
            }
        }
