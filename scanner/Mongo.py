from datetime import datetime
from Geolocation import get_data

class Mongo:
    def __init__(self, ip, ports, services, banners, hostname, image,default):
        self.geo = get_data(ip)
        self.col = {"ip": ip, "banners": banners, "services": services, "ports": ports, "hostname": hostname, "country": self.geo[0], "region_name": self.geo[1], "city": self.geo[2],"country_code": self.geo[3], "zip_code": self.geo[4], "latitude": self.geo[5], "longitude": self.geo[6], "date": self.get_time(), "screenshot": image}
        self.document = "{} | {} | {} | {} | {}".format(ip,services,self.geo[3],self.geo[1],self.geo[2])
        self.default = default

    def get_time(self):
        current = datetime.now()
        return current.strftime("%d/%m/%Y %H:%M")

    def insert_document(self,connection):

        if self.col["screenshot"] == None:
           del self.col["screenshot"]

        if self.default == True:
            self.col["default_login"] = True
           
        connection.insert(self.col)

    def show_document(self):
        return self.document
