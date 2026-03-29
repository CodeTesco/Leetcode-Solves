def searchInsert(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    mid = (r - l) // 2

    while l <= r:
        mid = l + ((r - l) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    
    return l

print(searchInsert([1,3,5,6], 2))

# print(l)
# print(mid)
# print(r)
# print("")
