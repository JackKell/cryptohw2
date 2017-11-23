from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme


class OAEP(BasePublicKeyEncryptionScheme):
    @staticmethod
    def generate(keySize):
        pass

    @staticmethod
    def encrypt(message, publicKey):
        pass

    @staticmethod
    def decrypt(cipherText, privateKey):
        pass
