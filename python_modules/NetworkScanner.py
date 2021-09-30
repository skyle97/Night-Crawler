import socket
import requests

class NetworkScanner:
   def __init__(self,ip_address):
      self.ip = ip_address
      self.path = "CUSTOM_PATH"
      self.port_list = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
      self.image_path = None
      self.ports = []
      self.banners = []
      self.services = []

   def start_scanner(self):
      socket.setdefaulttimeout(0.5)

      for port in self.port_list:
         try: 
            target = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            response = target.connect_ex((self.ip,port))

            if (response == 0):
               service = socket.getservbyport(port)

               print("{}:{} {}".format(self.ip,port,service)) 

               self.banners.append(self.get_banners(service,target,port))
               self.ports.append(port)
               self.services.append(service)
 
         except socket.timeout:
            print("Socket timed out")

         except ConnectionResetError:
            print("Connection reset")

         except socket.herror:
            print("Unable to retrieve hostname")
         finally:
            target.close()

   def get_banners(self,service,target,port):
      if (service == "http" or service == "http-alt"):
         target.send(b'GET / HTTP/1.1\n\n')
         self.take_screenshot(port)
      banner = target.recv(512).decode("utf-8", errors='ignore')
      return banner 

   def get_ports(self):
      if self.ports:
         return True
   
   def get_image(self):
      return self.image_path

   def get_results(self):
      return self.ip, self.banners, self.ports, self.services

   def take_screenshot(self,port):
      url = "{}:{}".format(self.ip,port)
      file_path = "{}/{}.png".format(self.path,url)
      response = requests.get("https://render-tron.appspot.com/screenshot/" + "http://{}".format(url), stream=True)
      if (response.status_code == 200):
         with open(file_path,'wb') as file:
            for x in response:
               file.write(x)
         print("Receiving screenshot")
         self.image_path = file_path
      else:
         print("Screenshot module not working")
