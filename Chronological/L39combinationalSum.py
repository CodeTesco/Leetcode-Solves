def combinationSum(candidates, target):
    combinations = []
    candidates.sort() 

    def backtrack(start_index, comb, currentSum):
        if currentSum == target:
            combinations.append(comb[:])
            return

        for i in range(start_index, len(candidates)):
            newSum = currentSum + candidates[i]

            if newSum > target:
                break 
                
            comb.append(candidates[i])
            backtrack(i, comb, newSum)
            comb.pop()

    backtrack(0, [], 0)
    return combinations

print(combinationSum([2,3,5], 8))