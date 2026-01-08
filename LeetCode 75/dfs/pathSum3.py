from tree import listToTree

def pathSum(root, targetSum):
    from collections import defaultdict

    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(node, currSum):
        if not node:
            return 0

        currSum += node.val
        count = prefix[currSum - targetSum]

        prefix[currSum] += 1
        count += dfs(node.left, currSum)
        count += dfs(node.right, currSum)
        prefix[currSum] -= 1

        return count

    return dfs(root, 0)


root = listToTree([10,5,-3,3,2,None,11,3,-2,None,1])
print(pathSum(root, 8))
# [3, 3]
# count = 1