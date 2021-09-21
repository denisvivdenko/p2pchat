from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor 
from blockchain.blockchain import Blockchain
from chat.get_request import GET
from chat.post_request import POST
from chat.user_address import UserAddress
from Crypto.PublicKey import RSA
from typing import Tuple
import json
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
        # ip and port of a server is not defined => it's server
        if (server_ip == None) | (server_port == None): 
            self.is_server = True
        
        # blockchain data
        self.pending_transactions: json = None
        self.online_users_blockchain: Blockchain = None
        # private / public keys init
        self.USER_KEYS_FILE_PATH = 'user_keys.json' # file with user's keys
        self.PRIVATE_KEY, self.PUBLIC_KEY = self.initialize_keys(self.USER_KEYS_FILE_PATH)

    def startProtocol(self):
        # if it's not a server -> sends request to connect to the network
        if not self.is_server:
            self.connect_to_network((self.server_ip, self.server_port))

    def datagramReceived(self, datagram, addr: Tuple[str, int]) -> None:
        query = datagram.decode('utf-8')
        request_type = self.parse_request_type(query)

        # checks request type (custom GET/POST methods) 
        # and process sent data OR sends requested one
        if request_type == 'GET':
            request = GET(query)
            requested_user_address: Tuple[str, int] = request.address_to_send
            requested_file_name: str = request.file_name
            with open(requested_file_name, "r") as read_file:
                data = json.load(read_file)
            self.send_data(requested_user_address, requested_file_name, json.dumps(data))

        elif request_type == 'POST':
            request = POST(query)
            post_file_name = request.file_name
            recieved_data = request.data
            print(f'recieved: {recieved_data} \t {post_file_name}')
            with open(post_file_name, "w") as write_file:
                write_file.write(recieved_data)

    def connect_to_network(self, server: Tuple[str, int]) -> None:
        """
        This methods connects user to the network using server 
        from which it gets information about online users
        :param server: (server_ip, server_port)
        """
        self.get_data((server[0], server[1]), 'pending_transactions.json')
        self.get_data((server[0], server[1]), 'online_users_blockchain.json')

    # custom realization of GET/POST methods in UDP network
    def get_data(self, address_to_request: Tuple[str, int], file_name: str) -> None:
        """
        Custom realization of GET method from HTTP protocol
        :param address_to_request: address which requests data (ip, port)
        :param file_name: name of the file which will be sent
        """
        query = GET(address_to_send=(self.host, self.port), file_name=file_name).get_query()
        self.transport.write(query.encode('utf-8'), address_to_request)

    def send_data(self, reciever_address: Tuple[str, int], file_name: str, data: str) -> None:
        """
        Custom realization of POST method from HTTP protocol
        :param reciever_address: address where data will be sent
        :param file_name: name of the file which is going to be sent
        :param data: data itself (string)
        """
        query = POST(file_name=file_name, data=data).get_query()
        self.transport.write(query.encode('utf-8'), reciever_address)

    def parse_request_type(self, query: str):
        request_type = query.split('\n')[0]
        if request_type == 'GET':
            return 'GET'
        elif request_type == 'POST':
            return 'POST'

        raise Exception(f'error: undefined request type: {request_type}')

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
        
    def initialize_keys(self, json_file_path: str) -> Tuple[str, str]:
        """
        Reads JSON file with keys or if it doesn't exist then 
        it generates new keys and write them into JSON
        :return: public_key, private_key
        """
        public_key, private_key = ('','')
        if os.path.exists(json_file_path): # if file with keys already exists -> read from JSON file
            with open(json_file_path, "r") as read_file:
                data = json.load(read_file)
                public_key, private_key = data['PUBLIC_KEY'], data['PRIVATE_KEY']
        else: # if not => generate new keys
            public_key, private_key = self.generate_keys()
            with open(json_file_path, "w") as write_file:
                keys = { 'PUBLIC_KEY' : self.PUBLIC_KEY, 'PRIVATE_KEY': self.PRIVATE_KEY }
                json.dump(keys, write_file)
        
        return public_key, private_key


if __name__ == '__main__':
    user_address = UserAddress().get_result()
    new_client = Client('127.0.0.1', user_address[1], '127.0.0.1', 8888)
    reactor.listenUDP(user_address[1], new_client)
    reactor.run()