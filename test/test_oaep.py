import unittest

from cryptohw2.publickeyencryption.oaep import OAEP


class OAEPTest(unittest.TestCase):
    def testEncryption(self):
        message: int = 456
        publicKey, privateKey = OAEP.generate()
        cipherText = OAEP.encrypt(message, publicKey)
        decryptedCipherText = OAEP.decrypt(cipherText, privateKey)
        self.assertEqual(message, decryptedCipherText)
        self.assertNotEquals(message, cipherText)


if __name__ == "__main__":
    unittest.main()