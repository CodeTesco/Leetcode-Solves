def firstMissingPositive(nums):
    nums.sort()
    least = 1
    
    for i in range(len(nums)):
        num = nums[i]
        if num <= 0:
            continue

        if num == least:
            least = num + 1
        if num > least:
            return least
        
    return least

print(firstMissingPositive([3,4,-1,1]))