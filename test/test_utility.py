import unittest
from cryptohw2.utility import gcd, powerMod


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


class ModPowerTest(unittest.TestCase):
    def test_numbers_2_5_3(self):
        self.assertEqual(powerMod(2, 5, 3), 2)

    def test_numbers_7_12_5(self):
        self.assertEqual(powerMod(7, 12, 5), 1)

    def test_numbers_22_3_100(self):
        self.assertEqual(powerMod(22, 3, 100), 48)


if __name__ == "__main__":
    unittest.main()
