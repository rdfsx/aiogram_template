from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: int = Field(...)
    language: str = Field(default='en')
    set_language: str = Field(default='en')
    create_time: datetime = datetime.now()
    update_time: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": 12345678,
                "language": "en",
                "set_language": "ru",
                "create_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
                "update_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
            }
        }


class UserUpdateModel(BaseModel):
    language: Optional[str]
    set_language: Optional[str]
    update_time: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": 12345678,
                "language": "en",
                "set_language": "ru",
                "create_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
                "update_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
            }
        }
