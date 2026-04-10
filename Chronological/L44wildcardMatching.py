def isMatch(s, p):
    if not p:
        return not s

    i, j = 0, 0
    star_idx = -1
    match_idx = -1
    
    while i < len(s):
        if j < len(p) and (p[j] == '?' or p[j] == s[i]):
            i += 1
            j += 1 
        elif j < len(p) and p[j] == '*':
            star_idx = j
            match_idx = i
            j += 1
        elif star_idx != -1:
            j = star_idx + 1
            match_idx += 1
            i = match_idx 
        else:
            return False
            
    while j < len(p) and p[j] == '*':
        j += 1

    return j == len(p)

print(isMatch("abcabc", "a*bc"))