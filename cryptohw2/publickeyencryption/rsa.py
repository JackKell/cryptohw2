from random import randint
from typing import Tuple

from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme
from cryptohw2.utility import getRandomPrime, gcd, modInverse


class RSA(BasePublicKeyEncryptionScheme):
    @staticmethod
    def generate() -> Tuple[Tuple[int, int], Tuple[int, int]]:
        p: int = getRandomPrime(2, 2 ** 2048 - 1)
        q: int = getRandomPrime(2, 2 ** 2028 - 1)
        N: int = p * q
        phiN: int = (p - 1) * (q - 1)
        e: int = randint(10000, 100000)
        while gcd(e, phiN) != 1:
            e = randint(10000, 100000)
        d: int = modInverse(e, phiN)
        publicKey: Tuple[int, int] = (e, N)
        privateKey: Tuple[int, int] = (d, N)
        return publicKey, privateKey

    @staticmethod
    def encrypt(message: int, publicKey: Tuple[int, int]):
        e, N = publicKey
        return pow(message, e, N)

    @staticmethod
    def decrypt(cipherText: int, privateKey: Tuple[int, int]):
        d, N = privateKey
        return pow(cipherText, d, N)
