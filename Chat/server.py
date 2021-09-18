from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor 
from Blockchain.blockchain import Blockchain
from Chat.user_address import UserAddress
from Chat.client import Client

if __name__ == '__main__':
    user_address = UserAddress().get_result()
    new_client = Client('192.168.31.67', 8888)
    reactor.listenUDP(8888, new_client)
    reactor.run()