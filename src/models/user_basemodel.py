from bson.objectid import ObjectId
import uuid
from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str
    username: str
    location: str
    token: Optional[str] = None
    password: Optional[str] = None

    class Config:
        collections = "users"
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Luis Rios",
                "username": "lrios",
                "location": "Sonora"
            }
        }

    def fake_decode_token(token):
        return User(
            username=token + "fakedecoded", name="Luis Rios"
        )