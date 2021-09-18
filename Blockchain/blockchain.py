from typing import List
from Blockchain.block import Block
from Blockchain.proof_of_work_protocol import ProofOfWorkProtocol

class Blockchain:


    def __init__(self):
        self.chain: List[Block] = []
        self.chain.append(self.create_root_block())
    
    def add_block(self, new_block: Block) -> None:
        protocol = ProofOfWorkProtocol(5)
        last_block = self.get_last_block()
        
        new_block.previous_hash = last_block.hash;
        new_block.hash = new_block.calculate_hash()

        new_block = protocol.mine_block(new_block)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        for block_index in range(1, len(self.chain)):
            previous_block = self.chain[block_index - 1]
            current_block = self.chain[block_index]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False

            return True

    def create_root_block(self) -> Block:
        return Block('00/00/00', 'root', '0')

    def get_last_block(self) -> Block:
        return self.chain[-1]


if __name__ == '__main__':
    blockchain = Blockchain()
    block_1 = Block('01/01/21', 'user_01: connected')
    block_2 = Block('02/01/21', 'user_01: disconnected')

    blockchain.add_block(block_1)
    blockchain.add_block(block_2)

    print(blockchain.is_chain_valid())