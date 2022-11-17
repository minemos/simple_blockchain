import MerkleRoot
import json
import random


def mining(block_hash, transaction_hash, header):
    nonce = random.randrange(1, 999999999999)
    print()
    print(f'Mining ... Nonce -> ', end=' ')
    while (True):
        nonce = random.randrange(1, 999999999999)
        print(nonce, end=', ')
        if block_hash == MerkleRoot.hashValue(f'{json.dumps(header)}&{nonce}&{",".join(transaction_hash)}'):
            break
    print()
    return nonce
