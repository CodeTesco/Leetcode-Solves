import math

def searchRange(nums, target):
    pos = [-1, -1]
    n = len(nums)
    l = 0
    r = n - 1
    mid = math.floor((r-l)/2)
    midInd = 0

    while l <= r:
        mid = l + math.floor((r-l)/2)
        if nums[mid] == target:
            midInd = mid
            pos[0] = mid
            r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    l = midInd
    r = n - 1

    if pos[0] == -1:
        return pos
    
    while l <= r:
        mid = l + math.floor((r-l)/2)
        if nums[mid] == target:
            pos[1] = mid
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
                
    return pos

print(searchRange([5,7,7,8,8,10], 1))

# print(n)
# print(mid)
# print("")