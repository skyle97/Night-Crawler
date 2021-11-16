from datetime import datetime
import pymongo
import json
import requests

class Mongo:
    def insert_document(self, ip, ports, services, banners, hostname, image_path):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client['IOT']
        self.devices_collection = self.db['devices']
        self.geo = self.geo_ip(ip)
        self.devices_collection.insert({"ip": ip, "banners": banners, "services": services, "ports": ports, "hostname": hostname, "country": self.geo[0], "region_name": self.geo[1], "city": self.geo[2],"country_code": self.geo[3], "zip_code": self.geo[4], "time_zone": self.geo[5], "latitude": self.geo[6], "longitude": self.geo[7], "date": self.get_time(), "screenshot": image_path})
        self.document = "{} {} {} {} {} {}".format(ip,ports,services,self.geo[3],self.geo[1],self.geo[2])
        
    def get_time(self):
        current = datetime.now()
        return current.strftime("%d/%m/%Y %H:%M")

    def geo_ip(self, ip):
        document = []
        API_KEY = "681318d0-38c1-11ec-be74-a1a202fc2be4"
        response = requests.get("https://api.freegeoip.app/json/{}?apikey={}".format(ip, API_KEY))
        result = response.content.decode()
        res = json.loads(result)
        document = [res['country_name'], res['region_name'], res['city'], res['country_code'], res['zip_code'], res['time_zone'], res['latitude'], res['longitude']]
        return document
    
    def show_document(self):
        return self.document
