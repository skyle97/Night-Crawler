from datetime import datetime
from Geolocation import get_data
from loguru import logger

def create_document(ip, ports, services, banners, hostname, image,default,connection):
    geo = get_data(ip)
    col = {"ip": ip, "banners": banners, "services": services, "ports": ports, "hostname": hostname, "country": geo["country_name"], "region_name": geo["region_name"], "city": geo["city"], "country_code": geo["country_code"], "zip_code": geo["zip_code"], "latitude": geo["latitude"], "longitude": geo["longitude"], "date": datetime.now().strftime("%d/%m/%Y %H:%M"), "screenshot": image}
    default = default
    insert_document(col,default,connection)
    logger.success("{} | {} | {} | {} | {}".format(ip, services,geo["country_code"], geo["country_name"], geo["city"]))
    
def insert_document(col,default,connection):
    if col["screenshot"] == None:
        del col["screenshot"]
    if default == True:
        col["default_login"] = True
    connection.insert(col)

