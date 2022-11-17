import hashlib


def calculate_merkle_root(hashList):
    # 해쉬 리스트 크기가 1이면 반환
    if len(hashList) == 1:
        return hashList[0]
    # 머클 트리 계산하고 저장할 리스트
    newHashList = []
    # 짝수로 0부터 (리스트 크기 -1) 까지 반복
    for i in range(0, len(hashList)-1, 2):
        # 해쉬 만들어서 추가
        newHashList.append(_hash(hashList[i], hashList[i+1]))
    # 만약 리스트 크기가 홀수면
    if len(hashList) % 2 == 1:
        # 마지막 해쉬만 따로 리스트에 추가
        newHashList.append(_hash(hashList[-1], hashList[-1]))
    # 재귀
    return calculate_merkle_root(newHashList)


def _hash(a, b):
    # a 와 b 합쳐서 해쉬로 만들기
    h = hashlib.sha256(hashlib.sha256(a.encode()+b.encode()
                                      ).hexdigest().encode()).hexdigest()
    return h


def hash_value(v):
    # 단순 해쉬 변환
    return hashlib.sha256(v.encode()).hexdigest()
