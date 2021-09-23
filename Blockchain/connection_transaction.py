from hashlib import sha256
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import enum

class ConnectionStatus(enum.Enum):
   CONNECTED = 1,
   DISCONNECTED = 0


class ConnectionTransaction:


    def __init__(self, user_public_key: str, time: str, user_ip: str, 
                            user_port: int, connection_status: ConnectionStatus):
        self.time: str = time
        self.user_ip: str = user_ip
        self.user_port: int = user_port
        self.connection_status: ConnectionStatus = connection_status
        self.user_public_key: str = user_public_key
        self.signature: str = ''

    def sign_transaction(self, private_key: str):
        signature = pkcs1_15.new(private_key)
        message_hash = self.calculate_hash()
        return signature.sign(message_hash)

    def get_string_format(self):
        transaction_message = f'{self.user_public_key};{self.time};{self.user_ip};' + \
                        f'{self.user_port};{self.connection_status.value[0]}'
        return transaction_message
    
    def calculate_hash(self) -> SHA256.SHA256Hash:
        transaction_message: str = self.get_string_format()
        hash = SHA256.new(data=transaction_message.encode('utf-8'))
        return hash