def romanToInt(s):
    intTable = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    intRoman = 0
    for i in range(len(s)):
        if (i + 1 < len(s) and intTable[s[i]] < intTable[s[i + 1]]):
            intRoman -= intTable[s[i]]
        else:
            intRoman += intTable[s[i]]

    return intRoman

print(romanToInt("IX"))