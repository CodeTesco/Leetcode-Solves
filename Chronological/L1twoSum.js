const twoSum = (nums, target) => {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if ((nums[i] + nums[j]) === target) {
                return [i, j]
            } else {
                continue
            }
        }
    }
};

const indArr = twoSum([2, 7, 11, 15], 9)
console.log(indArr)