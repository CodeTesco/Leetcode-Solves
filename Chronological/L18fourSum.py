def fourSum(nums, target):
    fourArr = []
    nums.sort()
    n = len(nums)
    first = 0
    second = 1
    third = 2
    fourth = n-1

    while (first + 3 < len(nums)):
        a = nums[first]
        b = nums[second]
        c = nums[third]
        d = nums[fourth]
        sum = a + b + c + d

        if (sum == target):
            arr = [a, b, c, d]
            if (not (arr in fourArr)):
                fourArr.append([a, b, c, d])

        if (sum <= target and third + 1 < fourth):
            third += 1
        elif (sum > target and second + 2 == fourth and not (fourth - first) == 3):
            second = first + 1
            third = second + 1
            fourth -= 1
        elif (sum > target and second + 2 == fourth and (fourth - first) == 3):
            first += 1
            second = first + 1
            third = first + 2
            fourth =  n - 1
        elif (second == fourth - 2 and third == fourth - 1):
            first += 1
            second = first + 1
            third = first + 2
            fourth =  n - 1
        elif (third + 1 <= fourth):
            second += 1
            third = second + 1
        else:
            first += 1
            second = first + 1
            third = first + 2
            fourth =  n - 1

    return fourArr

print(fourSum([1,0,-1,0,-2,2], 0))
# -5, -4, -3, -2, 1, 3, 3, 5

# print(first)
# print(second)
# print(third)
# print(fourth)
# print(f"sum = {sum}")
# print("")