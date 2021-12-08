import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import sys


def ip_reach(list):
    """ Test the reachability of devices via ping command. Works for Windows, MacOS and Linux """

    # check OS
    param = "-n" if platform.system().lower() == "windows" else "-c"

    for ip in list:
        ip = ip.rstrip("\n")

        # building the command
        # example: ping -n 2 10.10.10.1
        command = ["ping", param, "2", ip]

        # suppress output and error logs
        if subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            continue
        else:
            input("ERROR: " + ip + " was not reachable! Please re-check ip address. Press any key to continue...")
            sys.exit()
