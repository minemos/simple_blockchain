import MerkleRoot


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return MerkleRoot.hashValue(f'{self.sender}&{self.receiver}&{self.amount}')