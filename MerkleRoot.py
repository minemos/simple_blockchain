import hashlib

# Hash pairs of items recursively until a single value is obtained


def calculate_merkle_root(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    for i in range(0, len(hashList)-1, 2):
        newHashList.append(_hash(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1:  # odd, hash last item twice
        newHashList.append(_hash(hashList[-1], hashList[-1]))
    return calculate_merkle_root(newHashList)


def _hash(a, b):
    h = hashlib.sha256(hashlib.sha256(a.encode()+b.encode()).hexdigest().encode()).hexdigest()
    return h


def hashValue(v):
    return hashlib.sha256(v.encode()).hexdigest()
