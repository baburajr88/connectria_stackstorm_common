from oslo_config import cfg
from st2common.util.crypto import read_crypto_key, symmetric_decrypt, symmetric_encrypt


class CryptoLib:
    """
    A class to handle encryption and decryption using StackStorm's utilities.
    """

    def __init__(self):
        """
        Initializes the CryptoLib class by loading the encryption key.
        """
        crypto_key_path = cfg.CONF.keyvalue.encryption_key_path
        self.crypto_key = self._read_crypto_key(crypto_key_path)

    @staticmethod
    def _read_crypto_key(key_path):
        """
        Reads the cryptographic key from the given path.

        :param key_path: Path to the cryptographic key.
        :return: Cryptographic key.
        """
        return read_crypto_key(key_path=key_path)

    def encrypt(self, plaintext):
        """
        Encrypts the given plaintext.

        :param plaintext: The text to be encrypted.
        :return: Encrypted text.
        """
        return symmetric_encrypt(self.crypto_key, plaintext).decode("utf-8")

    def decrypt(self, ciphertext):
        """
        Decrypts the given ciphertext.

        :param ciphertext: The text to be decrypted.
        :return: Decrypted text.
        """
        return symmetric_decrypt(self.crypto_key, ciphertext.encode("utf-8"))
