def intToRoman(num):
    romanTable = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    romanInt = ""
    intArr = []
    strInt = str(num)
    n = len(strInt) - 1
    mult = 10 ** n

    for let in strInt:
        intArr.append(int(int(let) * mult))
        mult = mult / 10

    for i in intArr:
        n = int(len(str(i)) - 1)
        x = int(i / (10 ** n))
        if (x < 4):
            romanInt += romanTable[10**n] * x
        elif (x == 4):
            romanInt += romanTable[10**n]
            romanInt += romanTable[5 * (10**n)]
        elif (x == 5):
            romanInt += romanTable[5 * (10**n)]
        elif (x > 5 and x < 9):
            romanInt += romanTable[5 * (10**n)]
            romanInt += romanTable[10**n] * (x - 5)
        elif (x == 9):
            romanInt += romanTable[10**n]
            romanInt += romanTable[10**(n+1)]

    return romanInt

print(intToRoman(449))
# CD XL IX
# 400 + 40 + 9
