def longestCommonPrefix(strs):
    longestPref = ""
    
    lowest = len(strs[0])

    for str in strs:
        if (len(str) < lowest):
            lowest = len(str)

    for i in range(lowest):
        commonStr = strs[0][i]
        for j in range(len(strs)):
            if (strs[j][i] == commonStr):
                if (j == len(strs) - 1):
                    longestPref += commonStr
                continue
            else: 
                commonStr = "BREAK"
                break
        
        if (commonStr == "BREAK"):
            break

    return longestPref

print(longestCommonPrefix(["dog","racecar","car"]))