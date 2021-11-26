import requests

class Screenshot:
    def __init__(self,ip,port):
        self.path = "./screenshots"
        self.file = "{}:{}".format(ip,port)
        self.file_path = self.path + "/" + self.file + ".png"

    def http_screenshot(self):
        response = requests.get("https://render-tron.appspot.com/screenshot/" + "http://{}".format(self.file), stream=True)
        if (response.status_code == 200):
            with open(self.file_path, 'wb') as file:
                for x in response:
                    file.write(x)
            return self.file_path