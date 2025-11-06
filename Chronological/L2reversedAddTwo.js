function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

const toLinkedList = (arr) => {
    let template = new ListNode(0)
    let current = template

    for (let num of arr) {
        current.next = new ListNode(num)
        current = current.next
    }
    return template.next
}

const toArray = (list) => {
    let arr = []
    while (list) {
        arr.push(list.val)
        list = list.next
    }
    return arr
}

const reverseArr = (arr) => {
    let reversedArr = []
    for (let i = 0; i < arr.length; i++) {
        reversedArr.push(arr[arr.length - (i + 1)])
    }
    return reversedArr
}

const addTwoNumbers = function(l1, l2) {
    // const l1Arr = toArray(l1)
    // const l2Arr = toArray(l2)
    const l1Reversed = reverseArr(l1)
    const l2Reversed = reverseArr(l2)
    let sum1 = ""
    let sum2 = ""

    for (let num of l1Reversed) {
        sum1 += `${num}`
    }
    for (let num of l2Reversed) {
        sum2 += `${num}`
    }
    const total = BigInt(sum1) + BigInt(sum2)
    const strTotal = total.toString()
    let arr = []
    for (let i = 0; i < strTotal.length; i++) {
        arr.push(Number(strTotal[i]))
    }
    const reversedArray = reverseArr(arr)
    const linkedList = toLinkedList(reversedArray)
    return linkedList
};
console.log(addTwoNumbers([2, 3, 4], [5, 6, 4]))
