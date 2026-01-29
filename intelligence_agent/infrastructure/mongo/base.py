import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

_client = None

def get_mongo_client() -> MongoClient:
    global _client

    if _client is None:
        uri = os.getenv("MONGO_URI")
        if not uri:
            raise RuntimeError("MONGO_URI not set in environment")

        _client = MongoClient(
            uri,
            maxPoolSize=20,
            serverSelectionTimeoutMS=5000
        )

    return _client
