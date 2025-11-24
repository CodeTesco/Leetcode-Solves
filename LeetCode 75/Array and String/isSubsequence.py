def isSubsequence(s, t):
    l = 0
    r = 0

    while l < len(s) and r < len(t):
        if (s[l] == t[r]):
            l += 1
            r += 1
        else:
            r += 1

        if r == len(t):
            break

    if(l < len(s)):
        return False
    else:
        return True

print(isSubsequence("abf", "ahbgdc"))