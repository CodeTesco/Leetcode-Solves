def removeStars(s):
    result = ""

    for i in range(len(s)):
        if s[i] == "*":
            result = result[:-1]
        else:
            result += s[i]

    return result

print(removeStars("leet**cod*e"))