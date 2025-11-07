def reverseVowels(s):
    l = 0
    r = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    mod = s

    def replaceChar(s, i, new):
        return s[:i] + new + s[i+1:]

    while (l < r):
        let1 = s[l]
        let2 = s[r]

        if ((let1 in vowels) and (let2 in vowels)):
            dummy = s[l]
            mod = replaceChar(mod, l, s[r])
            mod2 = replaceChar(mod, r, dummy)
            l += 1
            r -= 1
            mod = mod2
            continue

        if (not (let1 in vowels)):
            l += 1
        if (not (let2 in vowels)):
            r -= 1

    return mod

print(reverseVowels("IceCreAm"))