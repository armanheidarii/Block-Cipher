import unittest
import sys

sys.path.append(".")

from pkg.block_cipher import BlockCipher


class TestBlockCipher(unittest.TestCase):

    def test_1(self):
        plaintext = b"\x00\x11\x22\x33\x44\x55\x66\x77"
        key = b"\x81\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x18"

        self.assertEqual(
            BlockCipher.encrypt(plaintext, key),
            "0101010111110100000110001011001000100101010001001011001101110110",
        )


if __name__ == "__main__":
    unittest.main()
