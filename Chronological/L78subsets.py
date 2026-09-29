def subsets(nums):
    def backtrack(start, arr, result):
        result.append(arr[:])

        for num in nums[start:]:
            arr.append(num)
            start += 1
            backtrack(start, arr, result)
            arr.pop()

        return result
        
    return backtrack(0, [], [])

print(subsets([0]))