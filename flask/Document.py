from flask import jsonify
from bson import ObjectId
import re

class Document:
    def __init__(self,database):
        self.db = database

    def get_document(self,col):
        colect = ({
            '_id': str(ObjectId(col['_id'])),
            '_ip': col['ip'],
            'ports': col['ports'],
            'services': col['services'],
            'banners': col['banners'],
            'date': col['date'],
            'country': col['country'],
            'region_name': col['region_name'],
            'city': col['city'],
            'country_code': col['country_code'],
            'zip_code': col['zip_code'],
            'time_zone': col['time_zone'],
            'latitude': col['latitude'],
            'longitude': col['longitude']
        })
        return colect

    def get_data(self,collections):
        devices = []
        for col in collections:
            devices.append(self.get_document(col))
        return jsonify(devices)
    
    def get_document_id(self,id):
        id = self.db.find_one({'_id': ObjectId(id)})
        return jsonify(self.get_document(id))

    def get_document_ip(self,ip):
        ip = self.db.find_one({'ip': (ip)})
        return jsonify(self.get_document(ip))

    def get_devices(self,query):
        query = query.lower().split("=")
        search_type = query[0]
        match = query[1]

        if (match != ""):

            if (search_type == "port"):
                collections = self.db.find({"ports": int(match)})

            elif (search_type == "service"):
                collections = self.db.find({"services": str(match)})

            elif (search_type == "banner"):
                reg = re.compile(r"{}".format(match), re.I)
                collections = self.db.find({"banners": {'$regex': reg}})

            elif (search_type == "city"):
                reg = re.compile(r"{}".format(match), re.I)
                collections = self.db.find({"city": {'$regex': reg}}) 
            else:
                return "Invalid search filter"

            return self.get_data(collections)
