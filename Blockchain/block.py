from hashlib import sha256

class Block:


    def __init__(self, timestamp: str, data: str, previous_hash: str=''):
        self.nonce: int = 0
        self.timestamp: str = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calculate_hash();

    def calculate_hash(self) -> str:
        block_content = self.timestamp + self.data + \
                            self.previous_hash + str(self.nonce)
        return sha256(block_content.encode('utf-8')).hexdigest()