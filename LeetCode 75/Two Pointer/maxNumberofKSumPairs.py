def maxOperations(nums, k):
    nums.sort()
    count = 0
    l = 0
    r = len(nums) - 1

    while l < r:
        sumNum = nums[l] + nums[r]
        if (sumNum == k):
            count += 1
            l += 1
            r -= 1
        elif (sumNum < k):
            l += 1
        elif (sumNum > k):
            r -= 1

    return count

print(maxOperations([3,1,3,4,3], 6))