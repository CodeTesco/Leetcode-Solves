def permute(nums):
    permutations = []

    def backtrack(res):
        if len(res) == len(nums):
            permutations.append(res[:])
            return

        for num in nums:
            if num in res:
                continue
            res.append(num)
            backtrack(res)
            res.pop()

    backtrack([])
    return permutations

print(permute([0,1]))