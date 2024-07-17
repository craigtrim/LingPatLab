# -*- coding: utf-8 -*-
""" Crytography Base Functions """


import os

from typing import Optional

from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

enc = 'utf-8'


class CryptoBase(object):
    """ Crytography Base Functions """

    def __init__(self,
                 crypto_key: Optional[str] = None):
        """ Change Log

        Created:
            2-Mar-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/baseblock/issues/1
        Updated:
            20-Oct-2022
            craigtrim@gmail.com
            *   remove hard-coded crypto key
                https://github.com/craigtrim/baseblock/issues/4

        Args:
            crypto_key (str): the fernet private key
        """
        def get_key() -> str:
            if crypto_key:
                return crypto_key
            if 'BASEBLOCK_CRYPTO_KEY' in os.environ:
                return os.environ['BASEBLOCK_CRYPTO_KEY']
            raise ValueError('Crypto Key Not Found')

        self._key = get_key()

    @staticmethod
    def generate_private_key() -> str:
        """ Use to Generate Private Key for ecrypting and decrypting text
        This key will be passed in as a value to the constructor of CryptoBase

        Returns:
            str: the private key
        """
        return Fernet.generate_key()

    def encrypt_str(self,
                    some_input: str) -> str:
        """ Encrypt a String

        Args:
            some_input (str): any input string

        Returns:
            str: the encrypted string
        """
        result = str(self.encrypt(some_input.encode(enc)))

        # eliminate the 'bytes' prefix and suffix markers
        if result.startswith("b'") and result.endswith("'"):
            return result[2:-1]

        return result

    def encrypt(self,
                message: bytes) -> str:
        """ Encrypt Bytes

        Args:
            message (bytes): any input bytes

        Returns:
            str: the encrypted string
        """
        f = Fernet(self._key)
        return str(f.encrypt(message))

    def decrypt_str(self,
                    some_input: str) -> str or None:
        """ Decrypt a String

        Args:
            some_input (str): any input string

        Raises:
            ValueError: the encrypted token is invalid

        Returns:
            str or None: the decrypted string if the encrypted token is valid
        """
        return self.decrypt(some_input.encode(enc))

    def decrypt(self,
                message: bytes) -> str:
        """ Decrypt Bytes

        Args:
            message (bytes): any input bytes

        Raises:
            ValueError: the encrypted token is invalid

        Returns:
            str: the decrypted string
        """
        try:
            f = Fernet(self._key)
            return f.decrypt(message).decode(enc)
        except InvalidToken:
            raise ValueError('Invalid Token')


def main(param1, param2):
    def _action():
        if param1 == 'encrypt':
            return CryptoBase().encrypt_str(param2)
        elif param1 == 'decrypt':
            return CryptoBase().decrypt_str(param2)
        else:
            raise NotImplementedError('\n'.join([
                'Unknown Param: {}'.format(param1)]))

    print(_action())


if __name__ == '__main__':
    import plac

    plac.call(main)
