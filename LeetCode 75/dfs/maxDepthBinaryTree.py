from tree import treeToList, listToTree

def maxDepth(root):
    maxCount = 1
    count = 0

    if not root:
        return 0

    def backtrack(current, count):
        count += 1

        if current.left is None and current.right is None:
            nonlocal maxCount
            maxCount = max(count, maxCount)
            count -= 1
            return
        
        if current.left is not None:
            backtrack(current.left, count)

        if current.right is not None:
            backtrack(current.right, count)
        else:
            return
    
    backtrack(root, count)

    return maxCount

# def maxDepth(root):
#     if root is None:
#         return 0

#     return 1 + max(maxDepth(root.left), maxDepth(root.right))

tree = listToTree([1, 2, 3, 4, 5, 6])
res = maxDepth(tree)
print(res)


