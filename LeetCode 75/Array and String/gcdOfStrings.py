def gcdOfStrings(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if (l2 > l1):
        subStr = str1
        str1 = str2
        str2 = subStr
        subNum = l1
        l1 = l2
        l2 = subNum

    gcd = ""
    gcd1 = str1[0]
    gcd2 = str2[0]
    l3 = 1

    while l3 <= l2 and gcd2 == gcd1:
        if l1 % l3 == 0 and l2 % l3 == 0:
            isMult = True
            former = str1[:l3]
            for i in range(0, l1, l3):
                if (not (str1[i:i+l3] == former)):
                    isMult = False
                    l3 += 1
                    gcd1 = str1[:l3]
                    gcd2 = str2[:l3]
                    break
            if (isMult == True):
                gcd = gcd1
                l3 += 1
                gcd1 = str1[:l3]
                gcd2 = str2[:l3]
            continue
        else:
            l3 += 1
            gcd1 = str1[:l3]
            gcd2 = str2[:l3]
            continue
    
    if (not (gcd1 == gcd2) and l3 < l2):
        return ""

    return gcd

print(gcdOfStrings("ABABAB", "ABAB"))