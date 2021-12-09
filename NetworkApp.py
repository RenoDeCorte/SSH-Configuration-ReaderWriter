import sys

from file_vaild import ip_file_valid
from ip_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connect import create_ssh_connection
from threads import create_threads


def main():
    """ Main """

    ip_list = ip_file_valid()

    try:
        ip_addr_valid(ip_list)
        ip_reach(ip_list)
        print("Commands are being executed on all devices. Please wait...")
        create_threads(ip_list, create_ssh_connection)

    except KeyboardInterrupt:
        input("Program aborted by user. Press any key to continue...")
        sys.exit()


if __name__ == '__main__':
    main()
