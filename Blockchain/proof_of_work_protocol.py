from Blockchain.block import Block

class ProofOfWorkProtocol:


    def __init__(self, difficulty: int=4):
        self.difficulty = difficulty

    def mine_block(self, block: Block) -> Block:
        while block.hash[:self.difficulty] != ''.zfill(self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

        return block