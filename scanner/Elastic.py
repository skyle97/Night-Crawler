from datetime import datetime
from Geolocation import get_data
from loguru import logger
from elasticsearch import helpers

import geoip2.database

def create_document(ip, ports, services, banners, hostname, image,default,connection,vnc):
    try:
        with geoip2.database.Reader("../geoip2/CITY/GeoLite2-City.mmdb") as geo_reader:
            response = geo_reader.city(ip)
        with geoip2.database.Reader("../geoip2/ASN/GeoLite2-ASN.mmdb") as asn_reader:        
            resp = asn_reader.asn(ip)
            col = {
                "ip": ip,
                "org": resp.autonomous_system_organization,
                "asn": resp.autonomous_system_number,
                "banners": banners,
                "services": services,
                "ports": ports,
                "hostname": hostname,
                "country": response.country.name,
                "city": response.city.name,
                "country_code": response.country.iso_code,
                "zip_code": response.postal.code,
                "latitude": response.location.latitude,
                "longitude": response.location.longitude,
                "screenshot": image,
                "vnc": vnc,
                "anonymous_login": default,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            logger.success("{} | {} | {} | {} | {}".format(ip,services,response.country.iso_code,response.country.name,response.city.name))
        doc = {k:v for k,v in col.items() if v is not None}
        
        connection.index(index="devices", document=doc)
    except:
        logger.exception("Exception ocurred:")