import unittest

from cryptohw2.publickeyencryption.rsa import RSA


class RSATest(unittest.TestCase):
    def testEncryption(self):
        message: int = 13
        publicKey, privateKey = RSA.generate(100)
        cipherText = RSA.encrypt(message, publicKey)
        decryptedCipherText = RSA.decrypt(cipherText, privateKey)
        self.assertEqual(message, decryptedCipherText)
        self.assertNotEquals(message, cipherText)


if __name__ == "__main__":
    unittest.main()
