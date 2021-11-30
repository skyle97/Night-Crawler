import threading
from numpy import array_split
from ipaddress import ip_address
from NetworkScanner import Network_Scanner
from Mongo import Mongo
from loguru import logger
from datetime import datetime

import sys

class Thread_Scanner():
    def __init__(self,start,end,threads,timeout,screenshot):
        self.timeout = timeout
        self.screenshot = screenshot
        self.ip_list = array_split(self.get_ranges(start,end),threads)

    def get_ranges(self,start,end):
        #Get total of ip addresses
        start_int = int(ip_address(start).packed.hex(), 16)
        end_int = int(ip_address(end).packed.hex(), 16)
        return [ip_address(ip).exploded for ip in range(start_int, end_int)]

    def job(self,sub_list):
        for ip in sub_list:
            Scanner = Network_Scanner(ip,self.timeout,self.screenshot)
            Scanner.start()
            if Scanner.get_ports():
                ip, banners, ports, services, hostname, image = Scanner.get_results()
                Base = Mongo()
                Base.create_document(ip, ports, services,banners, hostname, image)
                Base.insert_document()
                logger.success(Base.show_document())
        
    def start_threads(self):
        logger.info("Searching connected devices, please wait")
        jobs = []
        start = datetime.now()
        try:
            logger.info("Launching threads")
            for sub in self.ip_list:
                thread = threading.Thread(target=self.job, args=(sub,))
                thread.start()
                jobs.append(thread)
            for  t in jobs:
                t.join()
            end = datetime.now()
            elapsed_time = end-start
            logger.info("Execution time: {}".format(elapsed_time))
            
        except KeyboardInterrupt:
            #Not working, fix this issue later
            logger.info("You pressed CTRL+C")
            sys.exit(1)
