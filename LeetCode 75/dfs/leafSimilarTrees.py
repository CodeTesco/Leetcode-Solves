from tree import listToTree, treeToList

def leafSimilar(root1, root2):
    def backtrack(root, arr):
        if not root.left and not root.right:
            arr.append(root.val)
            return

        if root.left: backtrack(root.left, arr)
        if root.right: backtrack(root.right, arr)

    arr1, arr2 = [], []
    backtrack(root1, arr1)
    backtrack(root2, arr2)

    return arr1[:] == arr2[:]

root1 = listToTree([1,2])
root2 = listToTree([2,2])

print(leafSimilar(root1, root2))