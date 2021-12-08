import argparse
import pathlib

def get_flags():
    parser = argparse.ArgumentParser(
        description="Search engine for Internet-connected devices")
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
                        default=100)

    parser.add_argument("-m",
                        "--massive-scan",
                        type=pathlib.Path,
                        help="File path with IP blocks",
                        dest="file")

    parser.add_argument("--timeout",
                        type=int,
                        help="Socket time out",
                        dest="timeout",
                        default=0.5)

    parser.add_argument("--screenshot",
                        action="store_true",
                        help="Take screenshots from devices with HTTP")
        
    parser.add_argument("--top-ports",
                        action="store_true",
                        help="Scan only 20 most common ports",
                        dest="top")

    parser.add_argument("--all-ports",
                        action="store_true",
                        help="Scan 1000 ports",
                        dest="all")

    flags = parser.parse_args()
    return flags.start_ip, flags.end_ip, flags.threads,flags.file, flags.timeout, flags.screenshot, flags.top, flags.all
