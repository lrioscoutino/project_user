import logging
import os
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string
from .location_services import LocationServices

client = MongoClient(os.environ.get('MONGO_URI',
                                    'mongodb://debug:debug@mongodb:27017/user_store?retryWrites=true&w=majority')
                     )
db = client[os.environ.get('MONGO_INITDB_DATABASE', 'user_store')]
msg_collection = db[os.environ.get('MONGO_COLLECTION_USERS', 'users')]


class UserServices():

    @classmethod
    def create_all_fake_users(cls):
        fake_user_list = []
        for num_user in range(100):
            location = LocationServices.get_fake_location_by_code(str(random.randint(1, 32)).zfill(2))
            letters = string.ascii_lowercase
            prefix = "user"
            username = f'{prefix}-{"".join(random.choice(letters) for i in range(5))}'
            password = generate_password_hash(letters)
            user_fake = {
                "username": username,
                "name": f"User {username}",
                "location": str(location.get('_id')),
                "password": password
            }
            fake_user_list.append(user_fake)
        msg_collection.insert_many(fake_user_list)
        return True

    @classmethod
    def get_all_fake_users(cls):
        data = []
        users = msg_collection.find()
        data = [user for user in users]
        if users.count() == 0:
            raise Exception(f'No existen usuarios.')

        return dumps(data)

    @classmethod
    def get_user_by_id(cls, user_id):
        user = msg_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise Exception(f'No existe el usuario {user_id}.')

        return dumps(user)

    @classmethod
    def update_user_by_id(cls, user_id, user_data):
        user = msg_collection.update_one({'_id': ObjectId(user_id)}, {"$set": user_data})
        if not user:
            raise Exception('No existe el usuario a actualizar')

        return user

    @classmethod
    def delete_user_by_id(cls, user_id):
        user = msg_collection.delete_one({"_id": ObjectId(user_id)})
        ack = user.acknowledged

        return ack

    @classmethod
    def create_user(cls, user_data):
        letters = string.ascii_letters
        location = LocationServices.get_fake_location_by_name(user_data.get('location'))
        password = generate_password_hash(letters)
        user_data['location'] = str(location.get('_id'))
        user_data['password'] = password
        user = msg_collection.insert_one(user_data)
        return user

    @classmethod
    def get_user_by_username(cls, username):
        user = msg_collection.find_one({"username": username})
        if len(user) == 0:
            raise Exception(f'No existe el usuario con username {username}.')

        return dumps(user)
