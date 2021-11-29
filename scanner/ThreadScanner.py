import threading
from numpy import array_split
from ipaddress import ip_address
from NetworkScanner import NetworkScanner
from Mongo import Mongo
from colorama import Fore

class Crawler:
    def __init__(self,start,end,threads):
        self.start = start
        self.end = end
        self.threads = threads
        self.ip_list = array_split(self.get_ranges(),self.threads)
       
    def get_ranges(self):
        start_int = int(ip_address(self.start).packed.hex(), 16)
        end_int = int(ip_address(self.end).packed.hex(), 16)
        return [ip_address(ip).exploded for ip in range(start_int, end_int)]

    def new_worker(self,sub_list,count):
        for ip in sub_list:
            Scanner = NetworkScanner(ip)
            Scanner.start_scanner()
            if Scanner.get_ports():
                ip, banners, ports, services, hostname = Scanner.get_results()
                image = Scanner.get_image()
                Base = Mongo()
                Base.create_document(ip, ports, services,banners, hostname, image)
                Base.insert_document()
                print(Fore.GREEN + Base.show_document(count)+Fore.RESET)

    def start_threads(self):
        count = 0
        for sub in self.ip_list:
            count += 1
            worker = threading.Thread(target=self.new_worker, args=(sub, count))
            worker.start()
