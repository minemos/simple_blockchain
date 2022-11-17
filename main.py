import Chain
import Block
import Mine

# 체인 만들기
my_chain = Chain.Chain()

# 블록 만들기
block = Block.Block()

# 트랜잭션 추가하기
block.add_transaction('a', 'b', 1)
block.add_transaction('b', 'a', 1)

# 체인에 블록 추가하기
my_chain.add_block(block)

# 블록 만들기
block2 = Block.Block()

# 트랜잭션 추가하기
block2.add_transaction('a', 'b', 1)
block2.add_transaction('b', 'a', 1)

# 체인에 블록 추가하기
my_chain.add_block(block2)

# 체인에서 마지막 블록 정보 가져오기
print(my_chain.last_block().show())
print(my_chain.last_block())

# 채굴하기
nonce = Mine.mining(str(my_chain.last_block()), my_chain.last_block(
).transaction_hash, my_chain.last_block().header)
print('Nonce Find :', nonce)
print('Block Nonce : ', my_chain.last_block()._nonce)
print('Block Hash : ', my_chain.last_block())
