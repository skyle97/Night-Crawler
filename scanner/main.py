from Crawler import Crawler
from Commands import Commands
from colorama import Fore

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
    start, end, threads = Commands.get_flags()
    if (start and end and threads):
        print("START: {} END: {} THREADS: {}\n".format(start,end,threads))
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
