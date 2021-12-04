
import json

from api import API_KEY

from requests import get
from json.decoder import JSONDecodeError

class Geolocation:
    def get_data(ip):
        document = []
        try:
            API = API_KEY
            response = get("https://api.freegeoip.app/json/{}?apikey={}".format(ip, API))

            result = response.content.decode()
            res = json.loads(result)
            document = [res['country_name'], res['region_name'], res['city'],res['country_code'], res['zip_code'], res['latitude'], res['longitude']]
            return document
        except (JSONDecodeError, ConnectionError):
            #Resolve this issue later
            return None
