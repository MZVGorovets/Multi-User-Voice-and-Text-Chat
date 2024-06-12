from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast


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
    def __init__(self, key, public_key):
        self.key = key
        self.publick_key = public_key
        public_key_obj = RSA.import_key(self.publick_key)
        cipher_rsa = PKCS1_OAEP.new(public_key_obj)
        self.encrypted_key = cipher_rsa.encrypt(self.key)

    def returning(self):
        return self.encrypted_key
