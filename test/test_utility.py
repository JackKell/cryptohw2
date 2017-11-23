import unittest

from sympy import isprime

from cryptohw2.utility import gcd, egcd, modInverse, getRandomPrime


class GDCTest(unittest.TestCase):
    def test_numbers_5_10(self):
        self.assertEqual(gcd(5, 10), 5)

    def test_numbers_7_10(self):
        self.assertEqual(gcd(7, 10), 1)

    def test_numbers_55_9(self):
        self.assertEqual(gcd(55, 9), 1)

    def test_numbers_55_10(self):
        self.assertEqual(gcd(55, 10), 5)

    def test_numbers_49_14(self):
        self.assertEqual(gcd(49, 14), 7)


class EGDCTest(unittest.TestCase):
    def test_numbers_5_10(self):
        self.assertEqual(egcd(5, 10), (5, 1, 0))

    def test_numbers_180_150(self):
        self.assertEqual(egcd(180, 150), (30, 1, -1))

    def test_numbers_7_11(self):
        self.assertEqual(egcd(7, 11), (1, -3, 2))


class ModInverseTest(unittest.TestCase):
    def test_numbers_3_5(self):
        self.assertEqual(modInverse(3, 5), 2)

    def test_numbers_5_10(self):
        self.assertEqual(modInverse(5, 10), None)

    def test_numbers_7_11(self):
        self.assertEqual(modInverse(7, 11), 8)


class GetRandomPrime(unittest.TestCase):
    def test_random_range_2_100(self):
        for i in range(100):
            self.assertTrue(isprime(getRandomPrime(2, 100)))


if __name__ == "__main__":
    unittest.main()
