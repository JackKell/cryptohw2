from random import randint

from sympy.ntheory import isprime

from cryptohw2.publickeyencryption.basepublickeyencryptionscheme import BasePublicKeyEncryptionScheme
from cryptohw2.utility import getRandomPrime, powerMod, modInverse


class ElGamal(BasePublicKeyEncryptionScheme):
    @staticmethod
    def generate():
        q: int = getRandomPrime(2, 4194303)
        p: int = 2 * q + 1
        while not isprime(p):
            q = getRandomPrime(2, 4194303)
            p = 2 * q + 1
        g: int = randint(1, p - 2)
        g2: int = (g * g) % p
        g3: int = (g2 * g) % p
        while g3 == g or g3 == g2:
            g = randint(2, p)
            g2 = (g * g) % p
            g3 = (g2 * g) % p
        x: int = randint(0, p)
        h = powerMod(g, x, p)
        privateKey = x, p
        publicKey = g, p, h
        return publicKey, privateKey

    @staticmethod
    def encrypt(message, publicKey):
        g, p, h = publicKey
        # choose an ephemeral key
        r: int = randint(1, p - 2)
        t1: int = powerMod(g, r, p)
        t2: int = (powerMod(h, r, p) * message) % p
        return t1, t2

    @staticmethod
    def decrypt(cipherText, privateKey):
        t1, t2 = cipherText
        x, p = privateKey
        # g^r*x
        t1X = powerMod(t1, x, p)
        inverseT1X = modInverse(t1X, p)
        return inverseT1X * t2 % p

