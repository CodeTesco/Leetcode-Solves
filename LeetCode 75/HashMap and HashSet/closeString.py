def closeStrings(word1, word2):
    if not len(word1) == len(word2):
        return False
    
    set1 = set(word1)
    set2 = set(word2)

    for el in set1:
        if not el in set2:
            return False
    
    hash1 = {}
    hash2 = {}

    for el in word1:
        hash1[el] = hash1.get(el, 0) + 1
    for el in word2:
        hash2[el] = hash2.get(el, 0) + 1
    
    count1 = list(hash1.values())
    count2 = list(hash2.values())
    count1.sort()
    count2.sort()

    for i in range(len(count1)):
        if not count1[i] == count2[i]:
            return False

    return True

print(closeStrings("abcc", "bacc"))