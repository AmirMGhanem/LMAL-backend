import os

from pymongo import MongoClient

class MongoDBClientSingleton:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            MONGO_URL = os.getenv("ATLAS_URI", "mongodb://localhost:27017/")
            cls._instance = MongoClient(MONGO_URL)
        return cls._instance


def get_db():
    client = MongoDBClientSingleton.instance()
    db_name=os.getenv("DB_NAME","mydatabase")
    db = client[db_name]
    return db
