def convert(s, numRows):
    width = (numRows * 2) - 3
    end = width
    strArr = []
    newArr = []
    newStr = ""
    start = 0
    count = 0
    alt = width

    if (numRows == 1):
        return s

    for let in s:
        strArr.append(let)

    while(len(newArr) < len(s)):
        newArr.append(strArr[start])
        if (alt < width and alt > 0):
            if (start + alt + 1 < len(s)):
                newArr.append(strArr[start + alt + 1])

        start += width + 1

        if (start >= len(s)):
            count += 1
            start = count
            alt -= 2

    for let in newArr:
        newStr += let

    return newStr

print(convert("PAYPALISHIRING", 4))
# P   A   H   N -------3
# A P L S I I G--------1
# Y   I   R    --------3
# PAHNAPLSIIGYIR.......len(s) = 14
# 3 1 3 1 3 1 2

# P   A   H   N--------3
# A P L S I I G--------1
# Y   I   R   D--------3
# PAHNAPLSIIGYIRD.......len(s) = 15
# 3 1 3 1 3 1 2

# PAYPALISHIRING, 4

# P     I    N --------5   
# A   L S  I G --------3, 1
# Y A   H R    --------1, 3
# P     I      --------5
# PINALSIGYAHRPI.........len(s) = 14
# 4 1 1 4 1 1 2

# PAYPALISHIRING, 5

# P    H    --------7
# A   SI    --------5, 1
# Y  I R    --------3, 3
# P L  I G  --------1, 5
# A    N    --------7
# PHASIYIRPLIGAN........len(s) = 14
# 5 1 1 1 5 1

# PAYPALISHIRING, 6

# P     R    --------9
# A    II    --------7, 1
# Y   H N    --------5, 3
# P  S  G   ---------3, 5
# A I       ---------1, 7
# L         ---------9
# PRAIIYHNPSGAIL........len(s) = 14
# 5 1 1 1 5 1

# AB, 1
# 1