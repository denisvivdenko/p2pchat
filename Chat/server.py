from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor 
from blockchain.blockchain import Blockchain
from chat.user_address import UserAddress
from chat.client import Client

if __name__ == '__main__':
    user_address = UserAddress().get_result()
    new_client = Client('127.0.0.1', 8888)
    reactor.listenUDP(8888, new_client)
    reactor.run()