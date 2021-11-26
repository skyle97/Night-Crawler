from ftp import FTP_Test
def main():
    test = FTP_Test("../default-credentials/ftp.txt")
    test.start()

if __name__ == '__main__':
    main()
