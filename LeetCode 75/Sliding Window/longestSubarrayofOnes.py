def longestSubArray(nums):
    if (not 0 in nums) or nums.count(0) == 1:
        return len(nums) - 1
    
    l = 0
    count = 0
    zeros = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:
            if zeros == 1:
                l += nums[l:r].index(0) + 1
                zeros -= 1
            zeros += 1
        if zeros == 1:
            count = max(count, r - l)

    return count

print(longestSubArray([1,1,0,0,1,1,1,0,1]))