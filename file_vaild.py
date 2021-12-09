import os.path
import sys


def ip_file_valid():
    """ Checking IP address file and content validity """

    # prompting user for input
    ip_file = input("# Enter IP file path: ")

    # checking if the file exists
    if not (os.path.isfile(ip_file)):
        print("\n* File {} does not exist. Please check and try again".format(ip_file))
        input("Press any key to continue...")
        sys.exit()

    # open user selected file for reading (IP addresses file)
    selected_ip_file = open(ip_file, 'r')

    # starting from the beginning of the file
    selected_ip_file.seek(0)

    # extracting all ip addresses on each line
    ip_list = selected_ip_file.readlines()

    # closing the file
    selected_ip_file.close()

    return ip_list
