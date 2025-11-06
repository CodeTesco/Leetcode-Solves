const findMedianSortedArrays = (nums1, nums2) => {
    let jointArr = [...nums1, ...nums2]
    jointArr.sort((a, b) => a - b)
    console.log(jointArr)
    let arrLen = jointArr.length
    let median = 0
    if (arrLen % 2 === 0) {
        let mid = (arrLen / 2) - 1
        median = (jointArr[mid] + jointArr[mid + 1]) / 2
    } else {
        let mid = Math.floor(arrLen / 2)
        median = jointArr[mid]
    }
    return median
}
console.log(findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1]))

function findMedianSortedArrays(nums1, nums2) {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }

    const m = nums1.length;
    const n = nums2.length;
    let left = 0, right = m;

    while (left <= right) {
        const i = Math.floor((left + right) / 2); // Partition nums1
        const j = Math.floor((m + n + 1) / 2) - i; // Partition nums2

        const maxLeft1 = (i === 0) ? -Infinity : nums1[i - 1];
        const minRight1 = (i === m) ? Infinity : nums1[i];

        const maxLeft2 = (j === 0) ? -Infinity : nums2[j - 1];
        const minRight2 = (j === n) ? Infinity : nums2[j];

        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            // Correct partition found
            if ((m + n) % 2 === 0) {
                return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
            } else {
                return Math.max(maxLeft1, maxLeft2);
            }
        } else if (maxLeft1 > minRight2) {
            // Move partition in nums1 to the left
            right = i - 1;
        } else {
            // Move partition in nums1 to the right
            left = i + 1;
        }
    }

    throw new Error("Input arrays are not sorted properly");
}
