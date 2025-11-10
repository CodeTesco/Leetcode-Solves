def productExceptSelf(nums):
    length = len(nums)
    prodArr = []

    prod = 1
    for i in range(length):
        prodArr.append(prod)
        prod = prod * nums[i]

    prod2 = nums[-1]
    for i in range(length-1, -1, -1):
        if i == (length - 1):
            continue

        prodArr[i] = prodArr[i] * prod2
        prod2 = nums[i] * prod2

    return prodArr

print(productExceptSelf([1,2,3,4]))
