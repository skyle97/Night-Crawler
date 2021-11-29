
import json

from requests import get
from json.decoder import JSONDecodeError

class Geolocation:
    def get_data(ip):
        try:
            document = []
            API_KEY = "681318d0-38c1-11ec-be74-a1a202fc2be4"
            response = get("https://api.freegeoip.app/json/{}?apikey={}".format(ip, API_KEY))
            result = response.content.decode()
            res = json.loads(result)
            document = [res['country_name'], res['region_name'], res['city'], res['country_code'],res['zip_code'], res['time_zone'], res['latitude'], res['longitude']]
            return document
        except JSONDecodeError:
            return None
