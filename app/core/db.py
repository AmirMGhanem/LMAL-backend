import os
from pymongo import MongoClient

class MongoDBClientSingleton:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
            cls._instance = MongoClient(MONGO_URL)
        return cls._instance


def get_db():
    client = MongoDBClientSingleton.instance()
    db = client["mydatabase"]
    return db
