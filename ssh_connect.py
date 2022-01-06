import paramiko
import os.path
import sys
import time


def check_if_file_exists(file_type):
    """ Checks if a file exists """

    # check if file exists
    file_path = input("# Enter file path with {}: ".format(file_type))

    if not (os.path.isfile(file_path)):
        input("ERROR: {} not found! Please make sure file exists. Press any key to continue...".format(file_path))
        sys.exit()

    return file_path


def create_ssh_connection(ip, credentials_file, command_file):
    """ Create a SSH connection and execute commands """

    try:
        # Get credentials
        open_credentials_file = open(credentials_file, 'r')
        open_credentials_file.seek(0)

        # Extract username and password
        credentials = open_credentials_file.readlines()[0].split(",")
        user_name = credentials[0].strip().rstrip("\n")
        password = credentials[1].strip().rstrip("\n")

        # Login into device
        session = paramiko.SSHClient()

        # AutoAddPolicy accepts any connection, no matter what.
        # In addition to that, it also saves the host/public-key to the host-keys.
        # RejectPolicy rejects the connection if the hostname/public-key are not found in a host-keys file.
        # WarningPolicy is just like AutoAddPolicy, except it doesn't save the host/public-key to the host-keys,
        # and it also prints out a little warning message that will probably be ignored (if it is seen at all).
        # For testing purpose, we are setting it to AutoAddPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # make connection
        session.connect(ip.rstrip("\n"), username=user_name, password=password)

        # start an interactive shell session
        connection = session.invoke_shell()

        open_command_file = open(command_file, 'r')
        open_command_file.seek(0)

        for command in open_command_file.readlines():
            connection.send(command + '\n')
            time.sleep(2)

        open_credentials_file.close()
        open_command_file.close()

        # check for syntax errors + receive max 65535 bytes of output
        output = connection.recv(65535)

        print("\n\n ---------------------- OUTPUT ---------------------- \n\n")
        print(output.decode('utf-8'))
        print("\n\n ---------------------- OUTPUT ---------------------- \n\n")

        session.close()

    except paramiko.BadAuthenticationType:
        """ Exception raised when an authentication type (like password) is used, 
        but the server isn’t allowing that type. (It may only allow public-key, for example.) """
        input("ERROR: Destination does not allow type of authentication. Make sure you are using the correct type of "
              "authentication. Press any key to continue...")
        sys.exit()
    except paramiko.AuthenticationException:
        input("ERROR: Invalid username or password! Press any key to continue...")
        sys.exit()
    except paramiko.ssh_exception.NoValidConnectionsError:
        input("ERROR: Could not connect to port 22! Make sure SSH is configured on remote device. "
              "Press any key to continue...")
        sys.exit()
    except:
        input("ERROR: an unknown exception occurred. Press any key to continue...")
        sys.exit()


def get_file_path():
    # check if file with login credentials exists
    credentials_file = check_if_file_exists("login credentials")
    command_file = check_if_file_exists("commands")

    return credentials_file, command_file
