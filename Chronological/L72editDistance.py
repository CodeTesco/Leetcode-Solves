import math

def minDistance(word1, word2):
    notebook = dict()

    for i in range(len(word1) + 1):
        let1 = word1[:i]
        for j in range(len(word2) + 1):
            let2 = word2[:j]
            if let1 == let2:
                notebook[(let1, let2)] = 0
                continue

            replace = 1 + notebook[(let1[:-1], let2[:-1])] if not let1[-1:] == let2[-1:] else notebook[(let1[:-1], let2[:-1])]
            delete = 1 + notebook[(let1[:-1], let2)] if (let1[:-1], let2) in notebook.keys() else math.inf
            insert = 1 + notebook[(let1, let2[:-1])] if (let1, let2[:-1]) in notebook.keys() else math.inf

            cost = min(replace, delete, insert)
            notebook[(let1, let2)] = cost
            
    return notebook[(word1, word2)]

print(minDistance("intention", "execution"))