from tree import listToTree, treeToList

def goodNodes(root):
    def dfs(node, currentMax):
        if not node:
            return 0
        print(node.val)

        good = 1 if node.val >= currentMax else 0
        currentMax = max(currentMax, node.val)

        good += dfs(node.left, currentMax)
        good += dfs(node.right, currentMax)

        return good

    return dfs(root, root.val)


root = listToTree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
result = goodNodes(root)
print(result)