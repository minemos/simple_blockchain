class Chain:
    # 체인 생성자
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        # 머클 루트 생성
        block.set_merkle_root()
        # 첫 블록이 아니면
        if len(self.blocks) > 0:
            # 이전 블록 해쉬 지정
            block.set_previous_block(str(self.blocks[-1]))
        # 체인에 블록 추가
        self.blocks.append(block)

    def last_block(self):
        # 마지막 블록
        return self.blocks[-1]
