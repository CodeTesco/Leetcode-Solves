def maxSubArray(nums):
    l = 0
    r = 1
    max_num = nums[l]
    arr_sum = nums[l]

    while r < len(nums):
        arr_sum += nums[r]

        while (arr_sum <= 0 or nums[l] <= 0) and l < r:
            arr_sum -= nums[l]
            l += 1

        print(arr_sum)
        print(nums[l:r+1])
        max_num = max(max_num, arr_sum)
        r += 1

    return max_num

print(maxSubArray([2,-1,-1,2,0,-3,3]))