def longestOnes(nums, k):
    l = 0
    zeros = 0
    count = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        
        count = max(count, r - l + 1)

    return count

print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))