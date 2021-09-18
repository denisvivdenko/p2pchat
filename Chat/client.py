from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor 
from blockchain.blockchain import Blockchain
from chat.user_address import UserAddress
from typing import Tuple

class Client(DatagramProtocol):


    def __init__(self, host, port, server_ip=None, server_port=None):

        # client/server settings
        self.host: str = host
        self.port: int = port
        self.online_users: list = []
        self.server_ip: str = server_ip
        self.server_port: int = server_port
        self.is_server = False

        if (server_ip == None) | (server_port == None):
            self.is_server = True
        
        if not self.is_server:
            self.connect_to_network((self.server_ip, self.server_port))

    def startProtocol(self):
        if self.is_server != True:
            self.get_data((self.server_ip, self.server_port), 'start blockchain')

    def datagramReceived(self, datagram, addr: Tuple[str, int]) -> None:
        datagram = datagram.decode('utf-8')
        request_type = self.parse_request_type(datagram)
        if request_type == 'GET':
            requested_user_address: Tuple[str, int] = self.parse_query_requestor_address(datagram)
            self.send_data(requested_user_address, 'blockchain')
        elif request_type == 'POST':
            recieved_data = self.parse_request_data(datagram)
            print(f'recieved: {self.recieved_data}')

    def get_online_users(self, blockchain: Blockchain) -> list:
        pass

    def connect_to_network(self, server: Tuple[str, int]) -> None:
        pass

    def broadcast_data(self, recievers: list) -> None:
        pass

    def get_data(self, address_to_request: Tuple[str, int], blockchain_name: str) -> None:
        query = f'GET\n{self.host}\n{self.port}\n' + blockchain_name
        self.transport.write(query.encode('utf-8'), address_to_request)

    def send_data(self, reciever_address: Tuple[str, int], data: str) -> None:
        query = f'POST\n{data}'
        self.transport.write(query.encode('utf-8'), reciever_address)

    def parse_request_type(self, query: str):
        request_type = query.split('\n')[0]
        if request_type == 'GET':
            return 'GET'
        elif request_type == 'POST':
            return 'POST'

        raise Exception(f'error: undefined request type: {request_type}')

    def parse_query_requestor_address(self, query: str):
        lines = query.split('\n')
        return lines[1].strip(), int(lines[2])
    
    def parse_request_data(self, query: str):
        lines = query.split('\n')
        data = '\n'.join(lines[1:])
        return data


if __name__ == '__main__':
    user_address = UserAddress().get_result()
    new_client = Client('192.168.31.67', user_address[1], '192.168.31.67', 8888)
    reactor.listenUDP(user_address[1], new_client)
    reactor.run()