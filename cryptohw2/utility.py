from typing import Tuple, Any, Union, Optional

from sympy.ntheory import isprime
from sys import maxsize
from random import randint


def getRandomPrime(minValue: int = 2, maxValue: int = maxsize) -> int:
    primeValue: int = randint(minValue, maxValue)
    while not isprime(primeValue):
        primeValue = randint(minValue, maxValue)
    return primeValue


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modInverse(a, m) -> Union[Optional[int], Any]:
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def powerMod(term: int, exponent: int, mod: int) -> int:
    value = term
    for i in range(1, exponent):
        value *= term
        value %= mod
    return value
