def reverseWords(s):
    s = s.strip()
    arrStr = s.split(" ")
    i = 0

    while i < len(arrStr):
        el = arrStr[i]
        if (el == ""):
            arrStr.pop(i)
            continue
        i += 1
    
    arrStr.reverse()
    reverseStr = ""
    j = 0

    for el in arrStr:
        j += 1
        reverseStr += el
        reverseStr += " " if not (j == len(arrStr)) else ""

    return reverseStr

print(reverseWords("  hello world  "))