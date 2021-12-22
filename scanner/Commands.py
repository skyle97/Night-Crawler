import argparse
import pathlib

def get_flags():
    parser = argparse.ArgumentParser(
        description="Scanner for Internet-connected devices")
    parser.add_argument("-s",
                        "--start",
                        type=str,
                        dest="start_ip")

    parser.add_argument("-e",
                        "--end",
                        type=str,
                        dest="end_ip")

    parser.add_argument("-t",
                        "--threads",
                        type=int,
                        dest="threads",
                        help="Number of threads [Default: 100]",
                        default=100)

    parser.add_argument("-m",
                        "--massive-scan",
                        type=pathlib.Path,
                        help="File path with IP blocks",
                        dest="file")

    parser.add_argument("--timeout",
                        type=int,
                        help="Socket timeout [Default: 0.5]",
                        dest="timeout",
                        default=0.5)

    parser.add_argument("--screenshot",
                        action="store_true",
                        help="Take screenshots from hosts with HTTP")
        
    parser.add_argument("--top-ports",
                        action="store_true",
                        help="Scan only 20 most used ports",
                        dest="top")

    parser.add_argument("--all-ports",
                        action="store_true",
                        help="Scan 1000 most used ports",
                        dest="all")

    flags = parser.parse_args()
    return flags.start_ip, flags.end_ip, flags.threads,flags.file, flags.timeout, flags.screenshot, flags.top, flags.all
