import datetime
import random
import MerkleRoot
import json
import Transaction


class Block:
    def __init__(self, transaction=[], version=1):
        self.header = {
            'version': version,
            'previous_block': None,
            'merkle_root': None,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.transaction = transaction
        # 거래 내역 해쉬 리스트
        self.transaction_hash = list(map(lambda v: str(v), self.transaction))
        self.nonce = random.randrange(1, 999999999999)

    def add_transaction(self, sender, receiver, amount):
        transaction = Transaction.Transaction(sender, receiver, amount)
        self.transaction.append(transaction)
        self.transaction_hash.append(str(transaction))

    def set_merkle_root(self):
        self.header['merkle_root'] = MerkleRoot.calculate_merkle_root(
            self.transaction_hash
        )

    def set_previous_block(self, previous_block):
        self.header['previous_block'] = previous_block

    def show(self):
        return f'{json.dumps(self.header)}&{self.nonce}&{",".join(self.transaction_hash)}'

    def __str__(self):
        return MerkleRoot.hashValue(f'{json.dumps(self.header)}&{self.nonce}&{",".join(self.transaction_hash)}')
