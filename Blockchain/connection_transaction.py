from hashlib import sha256
from msilib.schema import Signature
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import blockchain.signature
import enum
import json

class ConnectionStatus(enum.Enum):
   CONNECTED = 1,
   DISCONNECTED = 0


class ConnectionTransaction:


    def __init__(self, user_public_key: RSA.RsaKey, time: str, user_ip: str, 
                            user_port: int, connection_status: ConnectionStatus):
        self.time: str = time
        self.user_ip: str = user_ip
        self.user_port: int = user_port
        self.connection_status: ConnectionStatus = connection_status
        self.user_public_key: RSA.RsaKey = user_public_key
        self.user_public_key_string = self.user_public_key.export_key('PEM').decode('utf-8')
        self.signature: blockchain.signature.Signature = None
        self.hash: str = self.calculate_hash().hexdigest()

    def sign_transaction(self, private_key: str) -> None:
        signature = pkcs1_15.new(private_key)
        message_hash = self.calculate_hash()
        self.signature = blockchain.signature.Signature(signature.sign(message_hash))

    def get_transaction_object(self) -> dict:
        transaction = {
            'PK': self.user_public_key_string,
            'SIGN': self.signature.get_decoded_format(),
            'USER_IP': self.user_ip,
            'USER_PORT': self.user_port,
            'STATUS': self.connection_status.name,
            'TIME': self.time,
            'HASH': self.hash
        }

        return transaction

    def get_string_format(self):
        transaction_message = f'{self.user_public_key_string};{self.time};{self.user_ip};' + \
                        f'{self.user_port};{self.connection_status.value[0]}'
        return transaction_message
    
    def calculate_hash(self) -> SHA256.SHA256Hash:
        transaction_message: str = self.get_string_format()
        hash = SHA256.new(data=transaction_message.encode('utf-8'))
        return hash