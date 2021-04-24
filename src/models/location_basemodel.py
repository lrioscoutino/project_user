from bson.objectid import ObjectId
from pydantic import BaseModel, Field
import uuid


class Location(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    code: str
    name: str

    class Config:
        collections = "locations"
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Sonora"
            }
        }
