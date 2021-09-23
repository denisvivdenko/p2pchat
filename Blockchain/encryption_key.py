from typing import Tuple
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import os 

class EncryptionKey:


    def __init__(self):
        self.PRIVATE_KEY_FILE = 'private.pem'
        self.PUBLIC_KEY_FILE = 'public.pem'
        self.public_key, self.private_key = self.__initialize_keys()
    
    def get_keys(self) -> Tuple[RSA.RsaKey, RSA.RsaKey]:
        """
        :return: (public_key, private_key)
        """
        return self.public_key, self.private_key

    def __initialize_keys(self) -> Tuple[str, str]:
        """
        Reads private.pem and public.pem files with keys or if they don't exist then 
        it generates new keys and write to seperate files
        :return: public_key, private_key
        """
        public_key, private_key = ('','')
        # checks for already generated keys
        if os.path.exists(self.PRIVATE_KEY_FILE) and os.path.exists(self.PUBLIC_KEY_FILE):
            public_key = self.__read_key_from_file(self.PUBLIC_KEY_FILE)
            private_key = self.__read_key_from_file(self.PRIVATE_KEY_FILE)
        else: # if not -> generate new keys and saves them
            public_key, private_key = self.__generate_keys()
            self.__write_key_to_file(self.PUBLIC_KEY_FILE, public_key)
            self.__write_key_to_file(self.PRIVATE_KEY_FILE, private_key)
        
        return public_key, private_key
    
    def __generate_keys(self) -> Tuple[RSA.RsaKey, RSA.RsaKey]:
        """
        Generates two keys for asymmetric encryption
        :return: public_key, private_key
        """
        keys_length = 1024
        keys = RSA.generate(keys_length)
        return keys.publickey(), keys

    def __read_key_from_file(self, file_name: str) -> RSA.RsaKey:
        with open(file_name, "r") as file:
            data = file.read()
            public_key = RSA.importKey(data)
            return public_key

    def __write_key_to_file(self, file_name: str, key: RSA.RsaKey) -> None:
        with open(file_name, 'w') as file:
            key_string_format = key.export_key('PEM').decode()
            file.write(key_string_format)