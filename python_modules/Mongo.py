from datetime import datetime
import pymongo
import json
import requests

class Mongo:
    def insert_document(self,ip,ports,services,banners,image_path):
        client = pymongo.MongoClient("localhost",27017)
        self.db = client['IOT']
        self.devices_collection = self.db['devices']
        self.devices_collection.insert({"ip":ip,"ports":ports,"services":services,"banners":banners,"date":self.get_time(), "geo":self.geo_ip(ip), "screenshot":image_path})

    def get_time(self):
        current = datetime.now()
        return current.strftime("%d/%m/%Y %H:%M:%S")

    def geo_ip(self,ip):
        response = requests.get("https://geolocation-db.com/jsonp/{}".format(ip))
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        return json.loads(result)
    