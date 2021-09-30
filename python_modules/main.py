from Crawler import Crawler

def main():
    NightCrawler = Crawler("186.182.0.0","186.182.255.255",100)
    NightCrawler.start_threads()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closing program")
