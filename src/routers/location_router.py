from fastapi import APIRouter
from src.services import LocationServices
from fastapi import status
from fastapi.responses import JSONResponse
location_router = APIRouter()


@location_router.post('/locations/create', tags=['locations'])
def create_locations():
    try:
        locations = LocationServices.create_all_fake_locations()
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


@location_router.get('/locations', tags=['locations'])
def get_all_locations():
    try:
        locations = LocationServices.get_all_fake_locations()
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'locations': locations
    })


@location_router.get('/location/{name_location}/', tags=['locations'])
def get_location_by_name(name_location: str):
    try:
        location = LocationServices.get_fake_location_by_name(name_location)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'location': location
    })


@location_router.get('/location/{code_location}/', tags=['locations'])
def get_location_by_name(code_location: str):
    try:
        location = LocationServices.get_fake_location_by_code(code_location)
    except Exception as err:
        return JSONResponse({
            'success': False,
            'message': f"{err}",
            'status': status.HTTP_400_BAD_REQUEST
        })
    return JSONResponse({
        'success': True,
        'location': location
    })