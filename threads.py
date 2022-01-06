import threading


def create_threads(list_of_ip, credential, command, function):
    """ Create a thread per ip, so that commands can be executed on each device concurrently """

    threads = []

    for ip in list_of_ip:
        th = threading.Thread(target=function, args=(ip, credential, command,))
        th.start()     # start the thread
        threads.append(th)

    for thread in threads:
        thread.join()  # Wait for all threads to terminate
