from collections import defaultdict

def groupAnagrams(strs):
    strs_hash = defaultdict(list)

    for i, val in enumerate(strs):
        sort_val = "".join(sorted(val))
        strs_hash[sort_val].append(strs[i])
    
    return list(strs_hash.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
