from unittest import TestCase

from app.utils.CesarCipher import *


class TestCesarCipher(TestCase):
    def setUp(self) -> None:
        self.cesar_cipher = CesarCipher(3)

    def test_encode(self):
        text = 'abc'
        self.assertEqual('def', self.cesar_cipher.encode(text))

    def test_decode(self):
        text = 'efg'
        self.assertEqual('bcd', self.cesar_cipher.decode(text))
