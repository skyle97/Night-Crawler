from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId
import re

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/IOT"
mongo = PyMongo(app)
CORS(app)

db = mongo.db.devices


@app.route("/", methods=['GET'])
def home():
    return "Hello World!"


@app.route("/search/<new_query>", methods=['GET'])
def get_devices(new_query):
    query = new_query.lower().split("=")
    if (query[1] != ""):

        if (query[0] == "port"):
            collections = db.find({"ports": int(query[1])})

        elif (query[0] == "service"):
            collections = db.find({"services": str(query[1])})

        elif (query[0] == "banner"):
            reg = re.compile(r"{}".format(query[1]), re.I)
            collections = db.find({"banners": {'$regex': reg}})
        else:
            return "Invalid search filter"
        devices = []

        for col in collections:
            colect = ({
                'ip': col['ip'],
                'ports': col['ports'],
                'services': col['services'],
                'banners': col['banners'],
                'date': col['date'],
                'geo': col['geo']
            })
            devices.append(colect)
        return jsonify(devices)
    else:
        return "Invalid search filter"


@app.route("/search/id/<id>", methods=['GET'])
def get_one_device(id):
    device = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(device['_id'])),
        'ip': device['ip'],
        'ports': device['ports'],
        'services': device['services'],
        'banners': device['banners'],
        'date': device['date'],
        'geo': device['geo']
    })


if __name__ == '__main__':
    app.run(debug=True)
