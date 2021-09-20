from hashlib import sha256
import enum

class ConnectionStatus(enum.Enum):
   CONNECTED = 1,
   DISCONNECTED = 0


class ConnectionTransaction:


    def __init__(self, user_public_key: str, signature: str, time: str, user_ip: str, 
                            user_port: int, connection_status: ConnectionStatus):
        self.user_public_key: str = user_public_key
        self.signature: str = signature
        self.time: str = time
        self.user_ip: str = user_ip
        self.user_port: int = user_port
        self.connection_status: ConnectionStatus = connection_status

    def get_string_format(self):
        record = f'{self.user_public_key};{self.signature};{self.connection_status}' + \
                    f'{self.connection_status.value[0]}'
        return record
    
    def calculate_hash(self) -> str:
        string_format_record: str = self.get_string_format()
        hash = sha256(string_format_record.encode('utf-8')).hexdigest()
        return hash