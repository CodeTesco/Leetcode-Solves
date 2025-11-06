def threeSum(nums):
    triplets = []
    n = len(nums)
    nums.sort()
    print(nums)
    i = 0
    l = i + 1
    r = n - 1

    while(i < len(nums) - 2):
        a = nums[i]
        b = nums[l]
        c = nums[r]

        if (i > 0 and a == nums[i - 1]):
            i += 1
            l = i + 1
            r = n - 1
            continue
        
        if (b == nums[l - 1] and l < r and l > i + 1):
            l += 1
            if (l >= r):
                i += 1
                l = i + 1
                r = n - 1
            continue

        if (r < len(nums) - 1 and c == nums[r + 1] and r > l):
            r -= 1
            if (r <= l):
                i += 1
                l = i + 1
                r = n - 1
            continue

        if (a + b + c == 0):
            triplets.append([a, b, c])
            l += 1
            r -= 1
        elif (a + b + c < 0):
            l += 1
        elif (a + b + c > 0):
            r -= 1

        if (l >= r):
            i += 1
            l = i + 1
            r = n - 1

    return triplets

print(threeSum([0, 0, 0]))
# [[-1,-1,2],[-1,0,1]]
# -4, -1, -1, 0, 1, 2

# print(a)
# print(b)
# print(c)
# print("")
# [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]