def maxVowels(s, k):
    l = 0
    r = k
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for let in s[l:r]:
        if let in vowels:
            count += 1

    localCount = count
    r -= 1
    while r < len(s):
        if (s[l] in vowels):
            localCount -= 1
        l += 1
        r += 1
        if (r == len(s)):
            break
        if (s[r] in vowels):
            localCount += 1
        
        if (localCount > count):
            count = localCount

    return count

print(maxVowels("weallloveyou", 7))