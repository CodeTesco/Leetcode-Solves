def combinationSum2(candidates, target):
    candidates.sort()
    combinations = []

    def backtrack(startInd, combSum, comb):
        if combSum == target:
            combinations.append(comb[:])
            return
        
        i = startInd
        while i < len(candidates):
            if i > startInd and candidates[i] == candidates[i - 1]:
                i += 1
                continue
            newSum = candidates[i] + combSum
            if newSum > target:
                break
            comb.append(candidates[i])
            backtrack(i + 1, newSum, comb)
            comb.pop()
            i += 1

    backtrack(0, 0, [])

    return combinations

print(combinationSum2([10,1,2,7,6,1,5], 8))
# 1, 1, 2, 5, 6, 7, 10
