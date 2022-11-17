import MerkleRoot
import json
import random
import Nonce


def mining(block_hash, transaction_hash, header):
    # 채굴 넌스 디버깅
    print(f'Mining ... Nonce -> ', end=' ')
    # 무한 루프
    while (True):
        # 넌스 랜덤으로
        nonce = random.randrange(1, Nonce.max)
        print(nonce, end=', ')
        # 기존 블록 해쉬와 랜덤으로 만든 넌스를 대입한 해쉬가 일치하는지
        if block_hash == MerkleRoot.hash_value(f'{json.dumps(header)}&{nonce}&{",".join(transaction_hash)}'):
            break
    print()
    # 넌스 리턴
    return nonce
