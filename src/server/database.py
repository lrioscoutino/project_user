import os
from pymongo import MongoClient


class MongoManagement():
    @classmethod
    def connect_mongodb(cls):
        client = MongoClient(os.environ.get('MONGO_URI', 'localhost/2027'))
        db = client.users
        return db