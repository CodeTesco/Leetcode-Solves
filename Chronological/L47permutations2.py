def permuteUnique(nums):
    n = len(nums)
    nums.sort()
    
    permutations = []
    used = set()

    def backtrack(res):
        if len(res) == n:
            permutations.append(res[:])
            return

        for i in range(n):
            num = nums[i]

            if i in used:
                continue

            if i > 0 and num == nums[i - 1] and (i - 1) not in used:
                    continue

            res.append(num)
            used.add(i)
            backtrack(res)

            res.pop()
            used.remove(i)

    backtrack([])
    return permutations

print(permuteUnique([1,1,2]))