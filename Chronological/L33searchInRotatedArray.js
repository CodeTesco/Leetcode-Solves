const search = (nums, target) => {
    let arr = [...nums]
    if (!arr.includes(target)) {
        return -1
    }
    let n = arr.length
    let mid = Math.floor(n/2)

    while (true) {
        if (arr[mid] == target) {
            const num = arr[mid]
            return nums.indexOf(num)
        }
        if (arr.slice(mid+1).includes(target)) {
            arr = arr.slice(mid+1)
            mid = Math.floor(arr.length/2) 
        } else {
            arr = arr.slice(0, mid)
            mid = Math.floor(arr.length/2) 
        }
    }
}

console.log(search([4,5,6,7,0,1,2], 0))