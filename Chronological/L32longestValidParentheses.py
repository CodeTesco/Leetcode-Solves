def longestValidParentheses(s):
    maxCount = 0
    lCount = 0
    rCount = 0
    count = 0

    for el in s:
        if el == "(":
            lCount -= 1
            count += 1
        elif el == ")" and not lCount == 0:
            rCount += 1
            count += 1
        else:
            count = 0
            lCount = 0
            rCount = 0
        
        if lCount + rCount == 0:
            maxCount = max(count, maxCount)
            lCount = 0
            rCount = 0
    
    lCount = 0
    rCount = 0
    count = 0

    for i in range(len(s)-1, -1, -1):
        el = s[i]

        if el == ")":
            rCount -= 1
            count += 1
        elif el == "(" and not rCount == 0:
            lCount += 1
            count += 1
        else:
            count = 0
            lCount = 0
            rCount = 0
        
        if lCount + rCount == 0:
            maxCount = max(count, maxCount)
            lCount = 0
            rCount = 0

    return maxCount

print(longestValidParentheses("()(()"))