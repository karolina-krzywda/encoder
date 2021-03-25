from app.utils.Cipher import Cipher


class CesarCipher(Cipher):
    """Implementation of cipher abstract class use cesar cipher to decode and encode messages"""

    def __init__(self, shift):
        """
        :param shift: move each character by some step
        """
        self.shift = shift

    def encode(self, text):
        """
        :param text: text to encode
        :return: encoded text
        """
        result = ''
        for c in text:
            result += chr(ord(c) + self.shift)
        return result

    def decode(self, text):
        """
         :param text: text to decode
         :return: decoded text
        """
        result = ''
        for c in text:
            result += chr(ord(c) - self.shift)
        return result
