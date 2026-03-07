def nextPermutation(nums):
    l = len(nums) - 2
    r = len(nums) - 1
    n = len(nums)
    
    while l >= 0:
        if nums[l] < nums[r]:
            next = n - 1
            while nums[next] <= nums[l]:
                next -= 1

            dummy = nums[next]
            nums[next] = nums[l]
            nums[l] = dummy
            nums[l+1:] = sorted(nums[l+1:])
            break
        l -= 1
        r -= 1
    
    if l < 0:
        nums.sort()
    return nums


print(nextPermutation([1,3,2]))