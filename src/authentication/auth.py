from src.models import User
from src.services import UserServices
from starlette.authentication import SimpleUser  # or a custom user model
from starlette_auth_toolkit.base.backends import BaseBasicAuth


class BasicAuth(BaseBasicAuth):
    async def verify(self, username: str, password: str):
        # In practice, request the database to find the user associated
        # to `username`, and validate that its password hash matches the
        # given password.
        if (username, password) != ("bob", "s3kr3t"):
            return None
        return SimpleUser(username)