import math

def getPermutation(n, k):

    def getNext(pool, target_idx, result):
        if len(pool) == 1:
            result += pool.pop(0)
            return result

        remaining = len(pool) - 1
        idx = target_idx // math.factorial(remaining)
        remainder = target_idx % math.factorial(remaining)
        choice = pool.pop(idx)
        result += choice

        return getNext(pool, remainder, result)
        
    result = ""
    pool = [str(i+1) for i in range(n)]
    return getNext(pool, k-1, result)

print(getPermutation(3, 1))