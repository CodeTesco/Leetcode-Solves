def findDifference(nums1, nums2):
    i = 0

    arr1 = []
    arr2 = []
    
    while True:
        if i < len(nums1):
            if not nums1[i] in nums2 and not nums1[i] in arr1:
                arr1.append(nums1[i])
        if i < len(nums2):
            if not nums2[i] in nums1 and not nums2[i] in arr2:
                arr2.append(nums2[i])
        i += 1
        
        if i >= len(nums1) and i >= len(nums2):
            break

    return [arr1, arr2]

print(findDifference([1,2,3], [2,4,6]))