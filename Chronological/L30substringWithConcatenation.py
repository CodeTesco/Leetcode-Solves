from collections import Counter

def findSubstring(s, words):
    if not s or not words: return []
    
    wordLen = len(words[0])
    wordCount = len(words)
    totalLen = wordLen * wordCount
    targetMap = Counter(words)
    results = []

    for i in range(wordLen):
        left = i
        right = i
        currentMap = Counter()
        count = 0
        
        while right + wordLen <= len(s):
            word = s[right : right + wordLen]
            right += wordLen
            
            if word in targetMap:
                currentMap[word] += 1
                count += 1
                
                while currentMap[word] > targetMap[word]:
                    leftWord = s[left : left + wordLen]
                    currentMap[leftWord] -= 1
                    count -= 1
                    left += wordLen
                
                if count == wordCount:
                    results.append(left)
            else:
                currentMap.clear()
                count = 0
                left = right
                
    return results

print(findSubstring("barfoothefoobarman", ["foo","bar"]))
