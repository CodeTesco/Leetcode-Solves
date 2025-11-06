def removeDuplicates(nums):
    k = 1
    l = 0
    r = 1

    while (l < len(nums) - 1):
        uniq = nums[l]
        dup = nums[r]
        if (uniq == dup):
            nums.pop(r)
        else:
            l = r
            r = l + 1
            k += 1

    return k

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))