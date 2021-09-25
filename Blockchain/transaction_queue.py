from blockchain.transaction import Transaction
from typing import List
import json

class TransactionQueue:


    def __init__(self, file_path: str=None, json_data: str=None):
        self._trasactions: List[Transaction] = self.update_queue(file_path=file_path, json_data=json_data)

    def save_to_file(self, file_path: str) -> None:
        pass
    
    def merge_transaction_queues(self, new_transaction_queue):
        pass

    def update_queue(self, file_path: str=None, json_data: str=None):
        key_name = 'pending_transactions'
        if isinstance(file_path, str):
            with open(file_path, 'r') as file:
                transactions = json.load(file)[key_name]
                
        elif issubclass(json_data, str):
            transactions = json.load(json_data)[key_name]

        raise Exception("unable to update queue. you haven't specified new data")

    def __getitem__(self, transaction_index):
        return self._trasactions[transaction_index]