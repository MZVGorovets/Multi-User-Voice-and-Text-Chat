from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
from supersocket import *


class Encryption():
    def __init__(self, key):
        self.cipher_suite = Fernet(key)

    def encryption(self, message: str):
        return self.cipher_suite.encrypt(message.encode())

    def decryption(self, data: bytes):
        return (self.cipher_suite.decrypt(data)).decode()

    def encryption_audio(self, message: bytes):
        return self.cipher_suite.encrypt(message)

    def decryption_audio(self, data: bytes):
        return (self.cipher_suite.decrypt(data))


class Key_Encryption():
    def __init__(self, client_socket):
        self.client_socket = client_socket

        key = RSA.generate(3072)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

        time.sleep(2)
        SuperSocket(self.client_socket).send_msg(self.public_key)
        self.key = SuperSocket(self.client_socket).recv_msg()
        private_key_obj = RSA.import_key(self.private_key)
        cipher_rsa = PKCS1_OAEP.new(private_key_obj)
        self.decrypted_key = cipher_rsa.decrypt(self.key)

    def returning(self):
        return self.decrypted_key
