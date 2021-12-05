import pymongo

def database_connect():
    client = pymongo.MongoClient("localhost", 27017)
    database = client['IOT']
    devices = database['devices']
    return devices