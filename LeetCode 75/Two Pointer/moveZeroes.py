def moveZeroes(nums):
    i = 0
    count = 0
    while count < len(nums):
        num = nums[i]

        if num == 0:
            nums.pop(i)
            nums.append(num)
        else:
            i += 1
        count += 1

    return nums

print(moveZeroes([0,0,1]))