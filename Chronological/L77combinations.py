def combine(n, k):
    def backtrack(start, arr, result):
        if len(arr) == k:
            result.append(arr[:])
            return

        for i in range(start, n+1):
            arr.append(i)
            start += 1
            backtrack(start, arr, result)
            arr.pop()
        return result
    
    return backtrack(1, [], [])

print(combine(4, 2))