def removeElement(nums, val):
    k = 0
    i = 0

    while i < len(nums):
        el = nums[i]
        if (el == val):
            nums.pop(i)
        else:
            k += 1
            i += 1

    return k

print(removeElement([0,1,2,2,3,0,4,2], 2))