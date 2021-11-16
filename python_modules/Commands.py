import argparse


class Commands:
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
                            dest="threads")

        flags = parser.parse_args()
        return flags.start_ip, flags.end_ip, flags.threads
