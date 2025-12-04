def uniqueOccurences(arr):
    hashmap = {}
    
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
    
    if len(set(hashmap.values())) == len(hashmap.values()):
        return True
    else:
        return False

print(uniqueOccurences([1,2,2,2,1,1,3]))