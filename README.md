# Night Crawler :spider:
Project focused on designing an Internet of Things (IoT) search engine.

![img](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![img](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![img](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![img](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)


## How does it work ?

Night Crawler uses a [command line interface](https://github.com/alechilczenko/Night-Crawler/tree/main/python_modules) to scan ip address ranges with multi-threading. Using sockets, it determines which ports are open and captures more information about the target, see the features section for details.

Each collection is stored in a database, and finally the deployment of an [API](https://github.com/alechilczenko/Night-Crawler/tree/main/flask) allows users to access the devices.

<a href="https://asciinema.org/a/4s6bDDZDVYlKf1Xdnb3o0y3Up" target="_blank"><img src="https://asciinema.org/a/N4Cmbsve4Y8iXREtRW27URU1K.svg" width="500"/></a>

## Features

- ### Port Scanning
  Is a method of determining which ports on a network are open and could be receiving or sending data. It is also a process for sending packets to specific ports on a host and     analyzing responses to identify vulnerabilities.
  
- ### Banner Grabbing
  Whenever performing the intel-reconnaissance process during penetration testing or security auditing, we need to pay attention to the current web-server’s exposed               information.

  That’s where banner grabbing comes in. Banner grabbing is the act of getting software banner information (name and version), whether it’s done manually, or by using any OSINT   tools that can do it for you automatically.

  FTP servers, web servers, SSH servers and other system daemons often expose critical information about not only the software name, but also about the exact versions and         operating systems they’re running.
  
  For example, following is a FTP banner:
  ```
  "220 CONICET La Plata FTP Server ready."
  ```

- ### IP Geolocation
  IP Geolocation is the identification of the geographic location of a device, such as a mobile phone, gadget, laptop, server and so on, by using an IP address.
  This search engine consumes an [API](https://freegeoip.app) to get the locations in JSON format.
  ```
  "country" : "Argentina",
  "region_name" : "Buenos Aires",
  "city" : "La Plata",
  "country_code" : "AR",
  "zip_code" : "1900",
  "time_zone" : "America/Argentina/Buenos_Aires",
  "latitude" : -34.9314,
  "longitude" : -57.9489,
  ```
- ### Screenshot
  If it detects that a device has an HTTP service running, it sends a request to a [server](https://github.com/GoogleChrome/rendertron) and take screenshot.

### Modules Explained 
<img src="images/iot.svg" width="800" />

## To-do list

- [x] [Command-line interface](https://github.com/alechilczenko/Night-Crawler/tree/main/python_modules)
- [x] [Backend API with Flask](https://github.com/alechilczenko/Night-Crawler/tree/main/flask)
- [ ] Frontend with React
- [ ] Web application vulnerability scan
- [ ] Build image with Docker and deployment
- [ ] Search filter by tags
- [ ] CMS Detection (Wordpress, Drupal, Joomla)

## Requirements
 ```
 pip install -r requirements.txt
 ```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Contact

alechilczenko@gmail.com

## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
