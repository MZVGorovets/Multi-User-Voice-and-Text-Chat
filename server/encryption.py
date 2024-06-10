from cryptography.fernet import Fernet


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
