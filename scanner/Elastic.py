from datetime import datetime
from Geolocation import get_data
from loguru import logger

def create_document(ip, ports, services, banners, hostname, image,default,connection,vnc):
    geo = get_data(ip)
    col = {"ip": ip, "banners": banners, "services": services, "ports": ports, "hostname": hostname, "country": geo["country_name"], "region_name": geo["region_name"], "city": geo["city"], "country_code": geo["country_code"], "zip_code": geo["zip_code"], "latitude": geo["latitude"], "longitude": geo["longitude"], "date": datetime.now().strftime("%d/%m/%Y %H:%M")}
    default = default
    if default == True:
        col.update({"default_login": default})
    if vnc != None:
        col.update({"vnc_screenshot": vnc})
    if image != None:
        col.update({"http_screenshot": image})
    connection.insert(col)
    logger.success("{} | {} | {} | {} | {}".format(ip, services,geo["country_code"], geo["country_name"], geo["city"]))
