import sys


def ip_addr_valid(list):
    """
    This method checks for a valid, ip address
    No: - Loopback              127.0.0.0 - 127.255.255.255
        - Broadcast             255.255.255.255
        - Multicast             224.0.0.0 - 239.255.255.255
        - APIPA/Link-Local      169.254.0.0 - 169.254.255.255
        - Class E address range 240.0.0.0 - 255.255.255.255
    """

    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')

        if len(octet_list) == 4 and int(octet_list[0]) < 224 and int(octet_list[0]) >= 1 and int(octet_list[0]) != 127 and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (int(octet_list[1]) >= 0 and int(octet_list[1]) <= 255 and int(octet_list[2]) >= 0 and int(octet_list[2]) <= 255 and int(octet_list[3]) >= 0 and int(octet_list[3]) <= 255):
            continue
        else:
            input("ERROR: '" + ip + "' is not a valid ip. Press any key to continue...")
            sys.exit()
