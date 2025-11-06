def mergeAlternately(word1, word2):
    mergedWord = ""
    
    length = len(word1) if len(word1) > len(word2) else len(word2)
    i = 0
    
    while i < length:
        if (i < len(word1)):
            mergedWord += word1[i]
        if (i < len(word2)):
            mergedWord += word2[i]
        i += 1

    return mergedWord

print(mergeAlternately("ab", "pqrs"))