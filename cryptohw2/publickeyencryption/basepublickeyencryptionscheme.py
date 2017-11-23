from abc import ABC, abstractmethod


class BasePublicKeyEncryptionScheme(ABC):
    @staticmethod
    @abstractmethod
    def generate(keySize):
        ...

    @staticmethod
    @abstractmethod
    def encrypt(message, publicKey):
        ...

    @staticmethod
    @abstractmethod
    def decrypt(cipherText, privateKey):
        ...
