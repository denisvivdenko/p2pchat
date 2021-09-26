from blockchain.connection_transaction import ConnectionStatus, ConnectionTransaction
from Crypto.PublicKey import RSA

class JSONConnectionTransactionConverter:
    _transaction = None
    
    def __init__(self, transaction_info: dict):
        time = transaction_info['time']
        user_ip = transaction_info['user_ip']
        user_port = transaction_info['user_port']
        connection_status = ConnectionStatus[transaction_info['connection_status']]
        signature = transaction_info['signature']
        transaction_hash = transaction_info['hash']
        user_public_key: RSA.RsaKey = RSA.import_key(extern_key=transaction_info['user_public_key'])
        _transaction = ConnectionTransaction(user_public_key, time, user_ip, user_port, connection_status, 
                                signature, transaction_hash)

    def get_result(self):
        return self._transaction
