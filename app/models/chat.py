from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class ChatModel(BaseModel):
    id: int = Field(...)
    type: str = Field(...)
    create_time: datetime = datetime.now()
    update_time: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 123456789,
                "type": "private",
                "create_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
                "update_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
            }
        }


class ChatUpdateModel(BaseModel):
    type: Optional[str]
    update_time: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 123456789,
                "type": "private",
                "create_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
                "update_time": datetime(2021, 10, 5, 13, 33, 29, 695694),
            }
        }

    @property
    def clear_dict(self):
        return {k: v for k, v in self.dict().items() if v is not None}
