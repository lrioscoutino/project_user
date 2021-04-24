from fastapi import (
    APIRouter,
    requests
)
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.models import User
from src.services import UserServices


user_router = APIRouter()


@user_router.get("/{username}/", tags=["users"])
def get_user_by_username(username: str):
    try:
        user = UserServices.get_user_by_username(username)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'result': user
    })


@user_router.get('/users', tags=["users"])
def get_all_users():
    try:
        users = UserServices.get_all_fake_users()
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        "users": users
    })


@user_router.post('/create', tags=["users"])
def create_all_users():
    try:
        users = UserServices.create_all_fake_users()
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'message': "La operacion se completo correctamente."
    })


@user_router.get('/{user_id}', tags=["users"])
def get_user_by_id(user_id: str):
    try:
        user = UserServices.get_user_by_id(user_id)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'result': user
    })


@user_router.put('/{user_id}', tags=["users"])
def update_user(user_id: str, user: User):
    update_user_encoded = jsonable_encoder(user)
    try:
        UserServices.update_user_by_id(
            user_id,
            update_user_encoded
        )
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'message': f'La operacion se completo correctamente.',
        'status': status.HTTP_200_OK
    })


@user_router.delete('/{user_id}', tags=["users"])
async def delete_user(user_id: str):
    try:
        UserServices.delete_user_by_id(user_id)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'message': f'La operacion se completo correctamente.',
        'status': status.HTTP_200_OK
    })


@user_router.post('/create-user', tags=["users"])
def create_user(user: User):
    try:
        user_data = user.dict()
        UserServices.create_user(user_data)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'message': f'La operacion se completo correctamente.',
        'status': status.HTTP_200_OK
    })
