from Crawler import Crawler
from Commands import Commands


def main():
    start, end, threads = Commands.get_flags()
    if (start and end and threads):
        NightCrawler = Crawler(start, end, threads)
        NightCrawler.start_threads()
    else:
        print("Please use -h to see all options")
        exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closing program")
