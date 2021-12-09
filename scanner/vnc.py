#!/usr/bin/env python
import socket
import os
from loguru import logger

# Connect to designated IP over port. Negotiate RFB version handshake + capture authentication methods
# Returns True if no authentication is needed, else returns False                                           

def get_security_level(ip,port):
    vnc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vnc_socket.settimeout(0.5)
    try:
        vnc_socket.connect((ip,port))
        RFB_VERSION = vnc_socket.recv(12)
        if not "RFB".encode() in RFB_VERSION:
            return False
        vnc_socket.send(RFB_VERSION)
        num_of_auth = vnc_socket.recv(1)
        if not num_of_auth:
            return False
        for i in range(0, ord(num_of_auth)):
            if ord(vnc_socket.recv(1)) == 1:
                return True
    except:
        pass
    finally:
        vnc_socket.close()

def test_vnc(service,ip,port):
    if service == "rfb":
        if get_security_level(ip,port):
            CMD = "timeout 60 vncsnapshot -allowblank " + ip + ":0 " + ip + ".jpg > /dev/null 2>&1"
            os.system(CMD)
            logger.success("Receiving screenshot from {}:{}".format(ip,port))
            return ip + ".jpg"
        else:
            logger.debug("Failed to take screenshot {}:{}".format(ip,port))   
            return None