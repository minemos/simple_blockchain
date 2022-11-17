

class Chain:
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        block.set_merkle_root()
        if len(self.blocks) > 0:
            block.set_previous_block(str(self.blocks[-1]))
        self.blocks.append(block)

    def last_block(self):
        return self.blocks[-1]
