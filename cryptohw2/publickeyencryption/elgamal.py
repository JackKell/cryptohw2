from random import randint

from sympy.ntheory import isprime

from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme
from cryptohw2.utility import getRandomPrime, modInverse


class ElGamal(BasePublicKeyEncryptionScheme):
    @staticmethod
    def generate():
        print("Finding p ...")
        q: int = getRandomPrime(2, 2 ** 1024 - 1)
        p: int = 2 * q + 1
        while not isprime(p):
            print(q)
            q = getRandomPrime(2, 2 ** 1024 - 1)
            p = 2 * q + 1
        print(p)
        print("Finding g ...")
        g: int = randint(2, p - 2)
        g2: int = (g * g) % p
        g3: int = (g2 * g) % p
        while g3 == g or g3 == g2:
            g = randint(2, p - 2)
            g2 = (g * g) % p
            g3 = (g2 * g) % p
        print(g)
        x: int = randint(1, p - 1)
        h = pow(g, x, p)
        privateKey = x, p
        publicKey = g, p, h
        return publicKey, privateKey

    @staticmethod
    def encrypt(message, publicKey):
        g, p, h = publicKey
        # choose an ephemeral key
        r: int = randint(1, p - 2)
        t1: int = pow(g, r, p)
        t2: int = (pow(h, r, p) * message) % p
        return t1, t2

    @staticmethod
    def decrypt(cipherText, privateKey):
        c1, c2 = cipherText
        x, p = privateKey
        t1X = pow(c1, x, p)
        inverseT1X = modInverse(t1X, p)
        return inverseT1X * c2 % p

