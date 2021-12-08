import socket

from Screenshot import take_screenshot
from Mongo import create_document
from login import anonymous_login

from loguru import logger


logger.add("logs/{time}.log", enqueue=True, level="DEBUG", backtrace=True, diagnose="True")

#Basic exception handling
class Network_Scanner():
    def __init__(self, ip):
        self.ip = ip
        self.image = None
        self.banners = []
        self.services = []
        self.hostname = []
        self.ports = []
        self.default = False

    def set_connection(self,connection):
        self.connection = connection

    def start(self,timeout,screenshot,ports):
        for port in ports:

            target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target.settimeout(timeout)
            target.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            try:
                response = target.connect_ex((self.ip, port))

                if  response == 0:

                    service = socket.getservbyport(port)
                    self.banners.append(self.get_banners(service, target, port,screenshot))
                    self.ports.append(port)
                    self.services.append(service)
                    #Remove all empty elements in hostnames
                    self.hostname = list(filter(None, socket.gethostbyaddr(self.ip)))
                    
                    self.default = anonymous_login(service,self.ip,port)

            except (socket.timeout, ConnectionResetError):
                logger.debug("{} | Socket timed out".format(self.ip))

            except OSError:
                logger.error("Disconnected from the network")

            except socket.herror:
                logger.debug("Unable to retrieve hostname")

            finally:
                target.close()
        #If variable contain ports, then it, is inserted in MongoDB
        if self.ports:
            create_document(self.ip,self.ports,self.services,self.banners,self.hostname,self.image,self.default,self.connection)

    def get_banners(self, service, target,port,screenshot):
        if  service == "http" or service == "http-alt":
            target.send(b'GET / HTTP/1.1\n\n')
            if screenshot:
               self.image = take_screenshot(self.ip,port)

        banner = target.recv(1024).decode("utf-8", errors='ignore')
        return banner

