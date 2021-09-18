from blockchain.block import Block
import time

class ProofOfWorkProtocol:


    def __init__(self, difficulty: int=4):
        self.difficulty = difficulty

    def mine_block(self, block: Block) -> Block:
        print(f'start mining block: timestamp:{block.timestamp}\tdifficulty:{self.difficulty}\n')
        start = time.time()

        while block.hash[:self.difficulty] != ''.zfill(self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

        done = time.time()
        total_time = done - start
        print(f'block with timestamp:{block.timestamp} has been mined. it took {total_time:.2f}s')
        print(f'{block.hash}\n')

        return block