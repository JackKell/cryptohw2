from random import randint
from time import time

from cryptohw2.publickeyencryption.elgamal import ElGamal
from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme
from cryptohw2.publickeyencryption.rsa import RSA


def printAverageEncryptionSchemeRunTimes(publicKeyEncryptionScheme: BasePublicKeyEncryptionScheme, trials: int = 3):
    keyGenerationTimes = []
    encryptionTimes = []
    decryptionTimes = []

    print(publicKeyEncryptionScheme.__name__, "Run Times:")
    for i in range(trials):
        message: int = randint(1, 1000)
        # "Generate Keys"
        start = time()
        publicKey, privateKey = publicKeyEncryptionScheme.generate()
        end = time()
        keyGenerationTimes.append(end - start)
        # Encrypt
        start = time()
        cipherText: int = publicKeyEncryptionScheme.encrypt(message, publicKey)
        end = time()
        encryptionTimes.append(end - start)
        # Decrypt
        start = time()
        decyptedCipherText: int = publicKeyEncryptionScheme.decrypt(cipherText, privateKey)
        end = time()
        decryptionTimes.append(end - start)

    averageKeyGenerationTime = sum(keyGenerationTimes) / len(keyGenerationTimes) * 1000
    averageEncryptionTime = sum(encryptionTimes) / len(encryptionTimes) * 1000
    averageDecryptionTime = sum(decryptionTimes) / len(decryptionTimes) * 1000
    print("\tAverage Key Generation Time", averageKeyGenerationTime, "ms")
    print("\tAverage Encryption Time", averageEncryptionTime, "ms")
    print("\tAverage Decryption Time", averageDecryptionTime, "ms")


def main():
    trails = 1
    printAverageEncryptionSchemeRunTimes(RSA, trails)
    printAverageEncryptionSchemeRunTimes(ElGamal, trails)
    # printAverageEncryptionSchemeRunTimes(OAEP, trails)
    # message = 13
    # publicKey, privateKey = ElGamal.generate()
    # cipherText = ElGamal.encrypt(message, publicKey)
    # decryptedMessage = ElGamal.decrypt(cipherText, privateKey)

    # print(message)
    # print(cipherText)
    # print(decryptedMessage)


if __name__ == "__main__":
    main()
