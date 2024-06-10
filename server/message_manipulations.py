from supersocket import *
from encryption import *


class Message_Manipulations():
    def __init__(self, key, client_socket):
        self.key = key
        self.client_socket = client_socket

    def sending_message(self, message):
        SuperSocket(self.client_socket).send_msg(
            Encryption(self.key).encryption(message))

    def receiving_message(self):
        return Encryption(self.key).decryption(SuperSocket(self.client_socket).recv_msg())

    def sending_audio(self, message):
        SuperSocket(self.client_socket).send_msg(
            Encryption(self.key).encryption_audio(message))

    def receiving_audio(self):
        return Encryption(self.key).decryption_audio(SuperSocket(self.client_socket).recv_msg())
