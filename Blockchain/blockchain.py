from block import Block

class Blockchain:


    def __init__(self):
        self.chain = []

    def create_root_block():
        return Block('00/00/00', 'root_block', '0')

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block: Block):
        new_block.previousHash = self.get_last_block().hash;
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)