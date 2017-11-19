from random import randint
from time import time
from typing import Tuple

from cryptohw2.publickeyencryption.elgamal import ElGamal
from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme


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
    # printAverageEncryptionSchemeRunTimes(RSA, 7)
    # printAverageEncryptionSchemeRunTimes(ElGamal, 7)
    # printAverageEncryptionSchemeRunTimes(OAEP, 7)
    message = 13
    publicKey, privateKey = ElGamal.generate()
    cipherText = ElGamal.encrypt(message, publicKey)
    decryptedMessage = ElGamal.decrypt(cipherText, privateKey)

    print(message)
    print(cipherText)
    print(decryptedMessage)


if __name__ == "__main__":
    main()
