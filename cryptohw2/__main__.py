import hashlib
from random import randint
from time import time

from cryptohw2.publickeyencryption.elgamal import ElGamal
from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme
from cryptohw2.publickeyencryption.rsa import RSA


def printAverageEncryptionSchemeRunTimes(publicKeyEncryptionScheme: BasePublicKeyEncryptionScheme, keySize, trials: int = 3):
    keyGenerationTimes = []
    encryptionTimes = []
    decryptionTimes = []

    print(publicKeyEncryptionScheme.__name__, "Trail Times:")
    for i in range(trials):
        print("\tTrail", i + 1, ":")
        message: int = randint(1, 1000)
        # "Generate Keys"
        start = time()
        publicKey, privateKey = publicKeyEncryptionScheme.generate(keySize)
        end = time()
        keyGenerationTimes.append(end - start)
        print("\t\tKey Generation:", (end - start) * 1000, "ms")
        # Encrypt
        start = time()
        cipherText: int = publicKeyEncryptionScheme.encrypt(message, publicKey)
        end = time()
        encryptionTimes.append(end - start)
        print("\t\tEncryption:", (end - start) * 1000, "ms")
        # Decrypt
        start = time()
        decyptedCipherText: int = publicKeyEncryptionScheme.decrypt(cipherText, privateKey)
        end = time()
        decryptionTimes.append(end - start)
        print("\t\tDecryption:", (end - start) * 1000, "ms")

    averageKeyGenerationTime = sum(keyGenerationTimes) / len(keyGenerationTimes) * 1000
    averageEncryptionTime = sum(encryptionTimes) / len(encryptionTimes) * 1000
    averageDecryptionTime = sum(decryptionTimes) / len(decryptionTimes) * 1000
    print("\tAverage Trail Times:")
    print("\t\tAverage Key Generation Time:", averageKeyGenerationTime, "ms")
    print("\t\tAverage Encryption Time:", averageEncryptionTime, "ms")
    print("\t\tAverage Decryption Time:", averageDecryptionTime, "ms")


def main():
    trails = 5
    printAverageEncryptionSchemeRunTimes(RSA, 2048, trails)
    printAverageEncryptionSchemeRunTimes(ElGamal, 1024, trails)


if __name__ == "__main__":
    main()
