import os
import uvicorn
from fastapi import (
    FastAPI,
    Depends,
    Header
)
from multiprocessing import Process
from wait4it import wait_for
from src.routers import (
    user_router,
    location_router
)
from src.models import User
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.get(path='/')
def root():
    return {"Hello": "world"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = User().fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

app.include_router(user_router, prefix="/api/v1/users")
app.include_router(location_router, prefix="/api/v1/locations")

_api_process = None


def start_api():
    global _api_process
    if _api_process:
        _api_process.terminate()
        _api_process.join()

    _api_process = Process(target=run, daemon=True)
    _api_process.start()
    wait_for(port=8000)


def delete_route(method: str, path: str):
    [app.routes.remove(route) for route in app.routes if method in route.methods and route.path == path]


def run():
    uvicorn.run(app, reload=os.environ.get('DEBUG_MODE', False), port=os.environ.get('PORT', '8000'))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
