from datetime import datetime
from Geolocation import get_data

class Mongo:
    def __init__(self, ip, ports, services, banners, hostname, image):
        self.geo = get_data(ip)
        self.collection = {"ip": ip, "banners": banners, "services": services, "ports": ports, "hostname": hostname, "country": self.geo[0], "region_name": self.geo[1], "city": self.geo[2],"country_code": self.geo[3], "zip_code": self.geo[4], "latitude": self.geo[5], "longitude": self.geo[6], "date": self.get_time(), "screenshot": image}
        self.document = "{} | {} | {} | {} | {}".format(ip,services,self.geo[3],self.geo[1],self.geo[2])
        self.ports = ports 
 
    def get_time(self):
        current = datetime.now()
        return current.strftime("%d/%m/%Y %H:%M")
    
    def validate(self,data):
        if data in self.ports:
            return True

    def insert_document(self,connection):
        #Add boolean flags in collections, to determine if has been performed a dictionary attack
        if self.validate(21):
           self.collection["ftp"] = False

        if self.validate(22):
           self.collection["ssh"] = False
        
        if self.validate(23):
           self.collection["telnet"] = False

        connection.insert(self.collection)

    def show_document(self):
        return self.document
