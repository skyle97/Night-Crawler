from ftplib import FTP, error_temp
from loguru import logger

import socket
import ftplib

def anonymous_login(service,ip,port):
    if service == "ftp":
        try:
            ftp = FTP(ip)
            ftp.connect(ip, port, timeout=1)
            ftp.login("anonymous","anonymous")
            ftp.quit()
            logger.info("Detected default login on: {}".format(ip))
            return True
            #Fix issue with EOFError
        except (ftplib.error_temp, ftplib.error_perm, socket.timeout, EOFError):
            #logger.debug("{} | {}:{}".format(ip, user, password))
            return False
 