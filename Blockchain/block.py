from hashlib import sha256

class Block:


    def __init__(self, timestamp, data, previousHash=''):
        self.timestamp: str = timestamp
        self.data: str = data
        self.previousHash: str = previousHash
        self.hash: str = self.calculate_hash();

    def calculate_hash(self) -> str:
        block_content = self.timestamp + self.data + \
                            self.previousHash
        return sha256(block_content)
        