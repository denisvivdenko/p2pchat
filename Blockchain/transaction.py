from abc import ABC, abstractclassmethod

class Transaction(ABC):

    
    @abstractclassmethod
    def get_transaction_object(self):
        pass