def lengthOfLastWord(s):
    count = 0

    for i in range(len(s)-1, -1, -1):
        letter = s[i]
        if not letter == " ":
            count += 1
        if letter == " " and not count == 0:
            break

    return count

print(lengthOfLastWord("a"))