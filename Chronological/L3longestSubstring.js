const lengthOfLongestSubstring = (str) => {
    let maxLen = 0
    let left = 0
    let right = 1
    while (right !== (str.length + 1)) {
        let sub = str.slice(left, right)
        right += 1
        
        if (sub.length > maxLen) {
            maxLen = sub.length
        }
        if (sub.includes(str[right - 1])) {
            left = left + 1
            right = right - 1
        }
    }
    return maxLen
}
console.log(lengthOfLongestSubstring("dvdf"))