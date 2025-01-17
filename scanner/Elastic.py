from datetime import datetime
from loguru import logger
from var import CITY, ASN
import geoip2.database

def create_document(ip, ports_dict, banners, hostname, image,default,connection,vnc):
    try:
        keys = list(ports_dict.keys())
        values = list(ports_dict.values())

        with geoip2.database.Reader(CITY) as geo_reader:
            response = geo_reader.city(ip)
        with geoip2.database.Reader(ASN) as asn_reader:        
            resp = asn_reader.asn(ip)
            
            col = {
                "ip": ip,
                "org": resp.autonomous_system_organization,
                "asn": resp.autonomous_system_number,
                "banners": banners,
                "services": keys,
                "ports": values,
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
            logger.success("{} | {} | {} | {}".format(ip,keys,response.country.name,response.city.name))
        doc = {k:v for k,v in col.items() if v is not None}
        
        connection.index(index="devices", document=doc)
    except:
        logger.exception("Exception ocurred:")