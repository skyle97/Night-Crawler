from requests import get

def take_screenshot(ip,ports):
    if "http" in ports:
        image = "{}:{}".format(ip, ports["http"])
        path = "../screenshots/{}.png".format(image)
        response = get("https://render-tron.appspot.com/screenshot/" + "http://{}".format(image), stream=True)

        if (response.status_code == 200):
            with open(path, 'wb') as file:
                for x in response:
                    file.write(x)
            return path
        else:
            return None
