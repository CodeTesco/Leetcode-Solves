def backtrack(i, avaiArr, current, combArr):
    if (i == len(avaiArr)):
        combArr.append(current)
        return

    for j in range(len(avaiArr[i])):
        current += avaiArr[i][j]
        backtrack(i + 1, avaiArr, current, combArr)
        current = current[:-1]

def letterCombinations(digits):
    combArr = []
    avaiArr = []
    letterMap = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    if (len(digits) == 1):
        return [let for let in letterMap[digits]]

    for i in range(len(digits)):
        num = digits[i]
        avaiArr.append(letterMap[num])

    print(avaiArr)
    
    backtrack(0, avaiArr, "", combArr)

    return combArr

print(letterCombinations("234"))
# let = "abcd"
# print(let[:-1])

# ['abc', 'def']
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# ['abc', 'def', 'ghi']
# ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]