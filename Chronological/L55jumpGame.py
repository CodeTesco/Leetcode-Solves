def canJump(nums):
    n = len(nums)
    if n <= 1:
        return True
    
    i = 0
    furthest = 0
    
    while i < n and i <= furthest:
        furthest = max(furthest, i + nums[i])

        if furthest == (n - 1) or i == (n-1):
            return True

        i += 1

    return False


print(canJump([3,2,1,0,4]))