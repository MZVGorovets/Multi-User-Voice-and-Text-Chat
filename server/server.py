import socket
import threading
from operations import *
from global_arrays import *
import sys


class Server:
    # opening a server and connecting a client and create a thread for every client
    def __init__(self, port):
        self.server_socket = socket.socket()
        self.port = port
        self.server_socket.bind(('0.0.0.0', port))
        print(port)
        self.server_socket.listen(100)
        print("Listening for clients...")

        while True:
            client, address = self.server_socket.accept()
            threading.Thread(target=self.play_client,
                             args=(client, address)).start()

    # add a client to list of client and run the main class
    def play_client(self, client, address):
        CLIENT_LIST.append((client, address))
        Operations(client, address, self.server_socket)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            if int(sys.argv[1]) <= 65535 and int(sys.argv[1]) >= 1000:
                Server(int(sys.argv[1]))
        raise ValueError
    except (ValueError, TypeError):
        Server(2000)
