def findMaxAverage(nums, k):
    maxSum = nums[0]
    maxArr = []
    l = 0
    r = 1

    if (k == 0):
        return max(nums)

    while r < len(nums):
        maxSum += nums[r]
        if (r-l < (k-1)):
            r += 1
        elif (r-l == (k-1)):
            maxArr.append(maxSum)
            maxSum -= nums[l]
            l += 1
            r += 1
    
    return (max(maxArr)/k)

print(findMaxAverage([1,12,-5,-6,50,3], 4))