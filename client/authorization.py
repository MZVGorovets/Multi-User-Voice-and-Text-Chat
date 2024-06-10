from message_manipulations import *
import hashlib


class Authorization():
    def __init__(self, key, client_socket, username, password) -> None:
        self.key = key
        self.client_socket = client_socket
        self.username = username
        self.password = password

    def sign_in(self):
        Message_Manipulations(self.key, self.client_socket).sending_message(
            "sign_in" + "!!!" + self.username)
        Message_Manipulations(self.key, self.client_socket).sending_message(
            str(hashlib.sha224(self.password.encode()).hexdigest()))

        if int(Message_Manipulations(self.key, self.client_socket).receiving_message()) == 200:
            return True

        else:
            return False

    def sign_up(self):
        Message_Manipulations(self.key, self.client_socket).sending_message(
            "sign_up" + "!!!" + self.username)
        Message_Manipulations(self.key, self.client_socket).sending_message(
            str(hashlib.sha224(self.password.encode()).hexdigest()))

        if int(Message_Manipulations(self.key, self.client_socket).receiving_message()) == 200:
            return True

        else:
            return False
