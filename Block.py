import datetime
import random
import MerkleRoot
import json
import Transaction
import Nonce


class Block:
    # 블록 생성자
    def __init__(self, transaction=[], version=1):
        # 블록 헤더
        self.header = {
            'version': version,
            'previous_block': None,
            'merkle_root': None,
            'timestamp': datetime.datetime.now().isoformat()
        }
        # 트랜잭션
        self.transaction = transaction
        # 트랜잭션 해쉬 리스트
        self.transaction_hash = list(map(lambda v: str(v), self.transaction))
        # 랜덤 넌스
        self._nonce = random.randrange(1, Nonce.max)

    def add_transaction(self, sender, receiver, amount):
        # 트랜잭션 만들고
        transaction = Transaction.Transaction(sender, receiver, amount)
        # 리스트에 추가
        self.transaction.append(transaction)
        # 해쉬만 따로 리스트에 추가
        self.transaction_hash.append(str(transaction))

    def set_merkle_root(self):
        # 트랜잭션 해쉬 리스트로 머클 루트 만들기
        self.header['merkle_root'] = MerkleRoot.calculate_merkle_root(
            self.transaction_hash
        )

    def set_previous_block(self, previous_block):
        # 이전 블록 설정하기
        self.header['previous_block'] = previous_block

    def show(self):
        # 데이터 표시하기
        return f'{json.dumps(self.header)}&{self._nonce}&{",".join(self.transaction_hash)}'

    def __str__(self):
        # 블록 해쉬 만들기
        return MerkleRoot.hash_value(f'{json.dumps(self.header)}&{self._nonce}&{",".join(self.transaction_hash)}')
