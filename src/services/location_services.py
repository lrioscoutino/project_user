import os
from pymongo import MongoClient
from bson.json_util import dumps
import re

client = MongoClient(os.environ.get('MONGO_URI',
                                    'mongodb://debug:debug@mongodb:27017/user_store?retryWrites=true&w=majority')
                     )
db = client[os.environ.get('MONGO_INITDB_DATABASE', 'user_store')]
msg_collection = db[os.environ.get('MONGO_COLLECTION_LOCATIONS', 'locations')]


class LocationServices():
    @classmethod
    def create_all_fake_locations(cls):
        locations_data = []
        locations = [
            "Aguascalientes",
            "Baja California",
            "Baja California Sur",
            "Campeche",
            "Chiapas",
            "Chihuahua",
            "Coahuila de Zaragoza",
            "Colima",
            "Distrito Federal",
            "Durango",
            "Guanajuato",
            "Guerrero",
            "Hidalgo",
            "Jalisco",
            "Mexico",
            "Michoacan de Ocampo",
            "Morelos",
            "Nayarit",
            "Nuevo Leon",
            "Oaxaca",
            "Puebla",
            "Queretaro",
            "Quintana Roo",
            "San Luis Potosi",
            "Sinaloa",
            "Sonora",
            "Tabasco",
            "Tamaulipas",
            "Tlaxcala",
            "Veracruz de Ignacio de la Llave",
            "Yucatan",
            "Zacatecas"
        ]
        for num, location in enumerate(locations):
            data = {
                "name": location,
                "code": str(num+1).zfill(2)
            }
            locations_data.append(data)

        if msg_collection.find({}).count() == 0:
            msg_collection.insert_many(locations_data)
            locations = msg_collection.find({})

        return locations

    @classmethod
    def get_all_fake_locations(cls):
        locations = msg_collection.find({})
        if locations.count() == 0:
            raise Exception(f'No existen locaciones.')

        return dumps(locations)

    @classmethod
    def get_fake_location_by_name(cls, name_location):
        location = msg_collection.find_one({'name': re.compile(f'^{name_location}$', re.IGNORECASE)})
        if len(location) == 0:
            raise Exception(f'No existen la locacion.')

        return location

    @classmethod
    def get_fake_location_by_code(cls, code_location):
        location = msg_collection.find_one({'code': code_location})
        if len(location) == 0:
            raise Exception(f'No existen la locacion con codigo {code_location}.')

        return location
