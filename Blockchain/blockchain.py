from blockchain.connection_record import ConnectionStatus
from typing import List
from blockchain.block import Block
from blockchain.proof_of_work_protocol import ProofOfWorkProtocol
from blockchain.connection_record import ConnectionRecord
from blockchain.connection_record import ConnectionStatus

class Blockchain:


    def __init__(self, mining_difficulty: int=3):
        self.mining_difficulty = mining_difficulty
        self.chain: List[Block] = []
        self.chain.append(self.create_root_block())
    
    def add_block(self, new_block: Block) -> None:
        protocol = ProofOfWorkProtocol(self.mining_difficulty)
        last_block = self.get_last_block()

        new_block.previous_hash = last_block.hash;
        new_block.hash = new_block.calculate_hash()

        new_block = protocol.mine_block(new_block)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        print('started checking chain validity...')

        for block_index in range(1, len(self.chain)):
            previous_block = self.chain[block_index - 1]
            current_block = self.chain[block_index]

            if current_block.hash != current_block.calculate_hash():
                print("chain isn't valid\n")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print("chain isn't valid\n")
                return False

            print("chain is valid\n")
            return True

    def create_root_block(self) -> Block:
        return Block('00/00/00', 'root', '0')

    def get_last_block(self) -> Block:
        return self.chain[-1]


if __name__ == '__main__':
    blockchain = Blockchain()
    block_1 = Block('01/01/21', [ConnectionRecord('127.0.0.1', '8989', ConnectionStatus.CONNECTED).get_string_format()])
    block_2 = Block('02/01/21', [ConnectionRecord('127.0.0.1', '2283', ConnectionStatus.CONNECTED).get_string_format()])

    blockchain.add_block(block_1)
    blockchain.add_block(block_2)

    blockchain.is_chain_valid()