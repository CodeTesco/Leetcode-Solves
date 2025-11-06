def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    n = len(nums)

    for i in range(n):
        a = nums[i]
        l = i + 1
        r = n - 1

        while(l < r):
            b = nums[l]
            c = nums[r]
            sum = a + b + c
            if (abs(sum - target) < abs(closest - target)):
                closest = sum

            if (sum < target):
                l += 1
            elif (sum > target):
                r -= 1
            else:
                return sum

    return closest

print(threeSumClosest([0, 0, 0], 1))

# [-4, -1, 1, 2]