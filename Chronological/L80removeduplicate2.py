def removeDuplicates(nums):
    l, r = 0, 0
    count = 0
    k = 0

    while r < len(nums) and nums[r] != "_":
        if nums[l] == nums[r] and count < 2:
            count += 1
            r += 1
            k += 1
        elif nums[l] == nums[r] and count >= 2:
            nums.pop(r)
            nums.append("_")
        elif nums[l] != nums[r]:
            l = r
            count = 0

    return k

print(removeDuplicates([1]))