from abc import ABC, abstractmethod


class Cipher(ABC):
    """Abstract class used to represent the cipher"""
    @abstractmethod
    def encode(self, text):
        """Returns encoded text"""
        pass

    @abstractmethod
    def decode(self, text):
        """Returns decoded text"""
        pass
