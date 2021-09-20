from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor 
from blockchain.blockchain import Blockchain
from chat.user_address import UserAddress
from Crypto.PublicKey import RSA
from typing import Tuple
import os

class Client(DatagramProtocol):


    def __init__(self, host, port, server_ip=None, server_port=None):

        # client/server settings
        self.host: str = host # client's ip address
        self.port: int = port # client's port

        # list of online users which client will recieve in porcess of connecting to the network
        # it will use it to communicate with other nodes in the network
        self.online_users: list = []
        
        self.server_ip: str = server_ip # ip/port of a server which connects users to each other 
        self.server_port: int = server_port
        self.is_server = False

        # private / public keys init
        self.USER_KEYS_FILE = '' # file with user's keys
        self.PRIVATE_KEY = ''
        self.PUBLIC_KEY = ''

        if os.path.exists(self.USER_KEYS_FILE): # if file with keys already exists
            pass # read from JSON file
        else: # if not => generate new keys
            self.PUBLIC_KEY, self.PRIVATE_KEY = self.generate_keys()

        # ip and port of a server is not defined => it's server
        if (server_ip == None) | (server_port == None): 
            self.is_server = True
        
        if not self.is_server: # if it's not a server -> sends request to connect to the network
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

    def generate_keys(self) -> Tuple[str, str]:
        """
        Generates two keys for asymmetric encryption
        :return: public_key, private_key
        """
        keys_length = 1024
        keys = RSA.generate(keys_length)
        private_key = ''.join(keys.export_key().decode().split('\n')[1:-1])
        public_key = ''.join(keys.publickey().export_key().decode().split('\n')[1:-1])
        return public_key, private_key


if __name__ == '__main__':
    user_address = UserAddress().get_result()
    new_client = Client('127.0.0.1', user_address[1], '127.0.0.1', 8888)
    reactor.listenUDP(user_address[1], new_client)
    reactor.run()