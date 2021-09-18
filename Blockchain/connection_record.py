import enum

class ConnectionStatus(enum.Enum):
   CONNECTED = 1,
   DISCONNECTED = 2


class ConnectionRecord:


    def __init__(self, user_ip: str, user_port: int, connection_status: ConnectionStatus):
        self.user_ip = user_ip
        self.user_port = user_port
        self.connection_status = connection_status

    def get_string_format(self):
        record = f'{self.user_ip};{self.user_port};{self.connection_status.value[0]}'
        return record

    