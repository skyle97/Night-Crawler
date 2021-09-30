import threading
import numpy
from ipaddress import ip_address
from NetworkScanner import NetworkScanner
from Mongo import Mongo

class Crawler:
    def __init__(self,start,end,threads):
        self.start = start
        self.end = end
        self.threads = threads
        self.ip_list = numpy.array_split(self.get_ranges(),self.threads)
       
    def get_ranges(self):
        start_int = int(ip_address(self.start).packed.hex(), 16)
        end_int = int(ip_address(self.end).packed.hex(), 16)
        return [ip_address(ip).exploded for ip in range(start_int, end_int)]

    def new_worker(self,sub_list):
        for ip in sub_list:
            Scanner = NetworkScanner(ip)
            Scanner.start_scanner()
            if Scanner.get_ports():
                ip, banners, ports, services= Scanner.get_results()
                image = Scanner.get_image()
                Base = Mongo()
                Base.insert_document(ip,ports,services,banners,image)

    def start_threads(self):
        for sub in self.ip_list:
            worker = threading.Thread(target=self.new_worker, args=(sub,))
            worker.start()
