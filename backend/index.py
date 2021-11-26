from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import database
from Document import Document

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/IOT"
mongo = PyMongo(app)
CORS(app)

database = mongo.db.devices
Collection = Document(database)

@app.route("/", methods=['GET'])
def home():
    return "Hello World!"

@app.route("/search/<query>", methods=['GET'])
def search(query):
    return Collection.get_devices(query)

@app.route("/search/id/<id>", methods=['GET'])
def get_id(id):
    return Collection.get_document_id(id)

@app.route("/search/ip/<ip>", methods=['GET'])
def get_ip(ip):
    return Collection.get_document_ip(ip)


@app.route("/total", methods=['GET'])
def get_count():
    return str(database.estimated_document_count())

if __name__ == '__main__':
    app.run(debug=True)

