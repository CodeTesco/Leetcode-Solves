def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s

    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:])) or (first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])

# "aab", "c*a*b"
# "ab", ".*c"
print(isMatch("aa", "a"))