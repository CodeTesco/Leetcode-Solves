def palindromeNumber(x):
    strNum = str(x)
    isPalin = False
    reverseStr = ""
    
    for i in range(len(strNum)):
        reverseStr += strNum[-(i + 1)]

    try:
        if (int(reverseStr) > 2**31 - 1 or int(reverseStr) < -(2**31)):
            return False
    except ValueError:
        return False

    if (strNum == reverseStr):
        isPalin = True
    return isPalin

print(palindromeNumber(10))