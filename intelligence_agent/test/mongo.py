from infrastructure.mongo.base import get_mongo_client

client = get_mongo_client()
print("Connected. Databases:", client.list_database_names())
