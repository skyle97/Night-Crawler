import socket
from Screenshot import Screenshot

class NetworkScanner:
    def __init__(self, ip_address):
        self.ip = ip_address
        self.port_list = [21, 22, 23, 25,69, 80, 110, 111, 135, 139, 143, 443, 445, 587, 993, 989, 990, 995, 1080, 1100, 1433, 1723, 2082, 2083, 2087, 2095, 2096, 2077, 2078,3000, 3306, 3389, 4000, 5000,5500, 5900, 6379, 8080, 8081, 8181, 8888,9100,27017]
        self.image_path = None
        self.ports = []
        self.banners = []
        self.services = []
        self.hostname = []

    def start_scanner(self):
        socket.setdefaulttimeout(0.5)

        for port in self.port_list:
            try:
                target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                response = target.connect_ex((self.ip, port))

                if (response == 0):
                    service = socket.getservbyport(port)

                    self.banners.append(self.get_banners(service, target, port))
                    self.ports.append(port)
                    self.services.append(service)
                    self.hostname = list(filter(None, socket.gethostbyaddr(self.ip)))

            except socket.timeout:
                print(self.ip +" Socket timed out")

            except ConnectionResetError:
                print(self.ip + " Connection reset")

            except socket.herror:
                pass
            finally:
                target.close()

    def get_banners(self, service, target, port):
        
        if (service == "http" or service == "http-alt"):
            target.send(b'GET / HTTP/1.1\n\n')
            Image = Screenshot(self.ip, port)
            self.image_path = Image.http_screenshot()

        banner = target.recv(1024).decode("utf-8", errors='ignore')
        return banner

    def get_ports(self):
        if self.ports:
            return True

    def get_image(self):
        return self.image_path

    def get_results(self):
        return self.ip, self.banners, self.ports, self.services, self.hostname
