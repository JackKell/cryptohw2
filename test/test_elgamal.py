import unittest

from cryptohw2.publickeyencryption.elgamal import ElGamal


class ElGamalTest(unittest.TestCase):
    def testEncryption(self):
        message: int = 456
        publicKey, privateKey = ElGamal.generate(100)
        cipherText = ElGamal.encrypt(message, publicKey)
        decryptedCipherText = ElGamal.decrypt(cipherText, privateKey)
        self.assertEqual(message, decryptedCipherText)
        self.assertNotEquals(message, cipherText)


if __name__ == "__main__":
    unittest.main()
