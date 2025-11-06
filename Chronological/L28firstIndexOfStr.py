def strStr(haystack, needle):
    l = 0
    r = len(needle)

    while (r <= len(haystack)):
        subStr = haystack[l:r]

        if (subStr == needle):
            return l
        else:
            l += 1
            r += 1

    return -1

print(strStr("a", "a"))