import socket

from Screenshot import Screenshot
from loguru import logger

logger.add("logs/{time}.log", enqueue=True, level="DEBUG", backtrace=True, diagnose="True")

#Basic exception handling
class Network_Scanner:
    def __init__(self, ip_address,timeout,screenshot):
        self.ip = ip_address
        self.port_list = [21, 22, 23, 25,69, 80, 110, 111, 135, 139, 143, 443, 445, 587, 993, 989, 990, 995, 1080, 1100, 1433, 1723, 2082, 2083, 2087, 2095, 2096, 2077, 2078,3000, 3306, 3389, 4000, 5000,5500, 5900, 6379, 8080, 8081, 8181, 8888,9100,27017]
        self.image_path = None
        self.ports = []
        self.banners = []
        self.services = []
        self.hostname = []
        self.timeout = timeout
        self.screenshot = screenshot

    def start(self):
        socket.setdefaulttimeout(self.timeout)

        for port in self.port_list:
            try:
                target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                response = target.connect_ex((self.ip, port))

                if  response == 0:
                    service = socket.getservbyport(port)

                    self.banners.append(self.get_banners(service, target, port))
                    self.ports.append(port)
                    self.services.append(service)
                    #Remove all empty elements in hostnames
                    self.hostname = list(filter(None, socket.gethostbyaddr(self.ip)))

            except (socket.timeout, socket.herror, ConnectionResetError, OSError):
                logger.debug("{} | Socket timed out".format(self.ip))
            except Exception as e:
                logger.exception("Exception ocurred")
            finally:
                target.close()

    def get_banners(self, service, target, port):
        if  service == "http" or service == "http-alt":
            target.send(b'GET / HTTP/1.1\n\n')
            if self.screenshot:
                image = Screenshot(self.ip, port)
                self.image_path = image.http_screenshot()

        banner = target.recv(1024).decode("utf-8", errors='ignore')
        return banner

    def get_ports(self):
        #If variable contain ports, then it, is inserted in MongoDB
        if self.ports:
            return True
    
    def get_results(self):
        return self.ip, self.banners, self.ports, self.services, self.hostname, self.image_path
