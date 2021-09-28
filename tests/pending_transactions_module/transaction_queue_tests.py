import json
from blockchain.connection_transaction_json_converter import JSONConnectionTransactionConverter
from blockchain.connection_transaction import ConnectionTransaction

transaction_1 = {
      "user_public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCcRVlitXw46zjl2mnna4on5C8U\nM4rzA93j24UuhdesJOGfGXhqot7sOILMfRSrCoq+dUE49ufUrkX1rY+FQzrfCqnu\nBKlmc0rrafjfik+oDq2qY9CdppIuzwyQVKQkwdnQcHxpZyiFyWjcAK8QuW3rccCN\npBEA//dkzjfwG2EX3wIDAQAB\n-----END PUBLIC KEY-----",
      "signature": "cqzzN8rp6fKKMZv7Otorbb9Mzm1aTHJtuaWX9GPCIE/S5OVR9dph+ZFUVAvt1yEa3BfhCLZr59/wmTIO3zb9/atlTgXk6dNFZbfj4qTjg49AnTYci/lETZur2U1wi3IVOLFaI5clMlrYJl2EO72ZXX60SRnxhIjwkeyoyKq3fpc=",
      "user_ip": "127.0.0.1",
      "user_port": 8080,
      "connection_status": "CONNECTED",
      "time": 1632823021.284933,
      "hash": "1e3501d35aaf0cc314ba6a62029401e6513b2de4bd1f56cc92108d722acbba57"
    }
transaction_2 = {
      "user_public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCcRVlitXw46zjl2mnna4on5C8U\nM4rzA93j24UuhdesJOGfGXhqot7sOILMfRSrCoq+dUE49ufUrkX1rY+FQzrfCqnu\nBKlmc0rrafjfik+oDq2qY9CdppIuzwyQVKQkwdnQcHxpZyiFyWjcAK8QuW3rccCN\npBEA//dkzjfwG2EX3wIDAQAB\n-----END PUBLIC KEY-----",
      "signature": "hHYqeXIIJywsxgabsdyCE3mhOepcEdpX+/lhU3X+zKzs8/m7W1JqxyDzFdYriplXzwXQbbkkrWwIlE7d/S4abMGr4W7PAspm4WV+/lNAphk3mDSe6s+BR4yBc9Ii1pi+MERfw9CGwZN29RHvRLgU1PypV4QqIgT1BuUdn63OqPI=",
      "user_ip": "127.0.0.1",
      "user_port": 8080,
      "connection_status": "CONNECTED",
      "time": 1632823093.700642,
      "hash": "524a174f27ebb735faec34c621e83d517af7c22087ad0d2f0fe888d94b5b1d8b"
    }


if __name__ == '__main__':
    transaction_1 = JSONConnectionTransactionConverter(transaction_1).get_result()
    transaction_2 = JSONConnectionTransactionConverter(transaction_2).get_result()
    transaction_3 = JSONConnectionTransactionConverter(transaction_1).get_result()

    assert transaction_1 == transaction_3, True
    print('test 1: transaction_1 == transaction_1 is successful')

    transactions = [transaction_1, transaction_2, transaction_3]
    assert len(transactions) == 3, True
    print('test 2: is successful')

    assert len(set(transactions)) == 2, True
    print('test 3: list of transactions can be transformed into a set')

