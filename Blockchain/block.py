from hashlib import sha256

class Block:


    def __init__(self, timestamp: str, data: list, previous_hash: str=''):
        self.nonce: int = 0
        self.timestamp: str = timestamp
        self.data: list = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calculate_hash();

    def calculate_hash(self) -> str:
        block_content = self.timestamp + str(self.data) + \
                            self.previous_hash + str(self.nonce)
        return sha256(block_content.encode('utf-8')).hexdigest()