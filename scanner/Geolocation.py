
import json
from api import API_KEY

from requests import get
from json.decoder import JSONDecodeError
from loguru import logger

def get_data(ip):
    document = []
    try:
        API = API_KEY
        response = get("https://api.freegeoip.app/json/{}?apikey={}".format(ip, API))
        result = response.content.decode()
        document = json.loads(result)
        return document
    except (JSONDecodeError, ConnectionError):
        #Resolve this issue later
        logger.error("Error API response")
