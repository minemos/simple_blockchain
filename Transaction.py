import MerkleRoot


class Transaction:
    # 트랜잭션 생성자
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        # 트랜잭션 해싱
        return MerkleRoot.hash_value(f'{self.sender}&{self.receiver}&{self.amount}')
