#Local modules
from NetworkScanner import Network_Scanner
from Mongo import Mongo

from ipaddress import ip_address
from loguru import logger
from datetime import datetime
from time import sleep

import queue
import sys
import threading

class Thread_Scanner():
    def __init__(self,start,end,threads,timeout,screenshot):
        self.timeout = timeout
        self.screenshot = screenshot
        self.ip_list = self.get_ranges(start,end)
        self.threads = threads

    def get_ranges(self,start,end):
        #Get total of ip addresses
        start_int = int(ip_address(start).packed.hex(), 16)
        end_int = int(ip_address(end).packed.hex(), 16)
        return [ip_address(ip).exploded for ip in range(start_int, end_int)]

    def job(self,q):
        while not q.empty():
            ip = q.get()
            Scanner = Network_Scanner(ip,self.timeout,self.screenshot)
            Scanner.start()
            q.task_done()

    def start_threads(self):
        #Implemeting Queue to limit number of threads
        logger.info("Searching connected devices, please wait")
        start = datetime.now()
        q = queue.Queue()
        try:
            logger.info("Launching threads")
            for j in self.ip_list:
                q.put(j)
                
            logger.info("Waiting for Queue to complete, {} jobs".format(q.qsize()))
        
            for i in range(self.threads):
                thread = threading.Thread(target=self.job, args=(q,),daemon=True)
                thread.start()
            q.join()
            end = datetime.now()
            elapsed = end-start
            logger.info("Execution time: {}".format(elapsed))

        except KeyboardInterrupt:
            logger.info("You pressed CTRL+C")
            sys.exit(1)
