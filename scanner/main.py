from ThreadScanner import ThreadScanner
from Commands import Commands
from colorama import Fore
from loguru import logger



def show():
    return Fore.GREEN +'''

              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |     Computer          | |
              | |      Services         | |
              | |       Company         | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''+ Fore.RESET

def main():
    print(show())
    logger.info("Searching for connected devices, please wait")
    start, end, threads = Commands.get_flags()
    if (start and end and threads):
        NightCrawler = ThreadScanner(start,end,threads)
        NightCrawler.start_threads()
    else:
        logger.info("Please use -h to see all options")
        exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closing program")
