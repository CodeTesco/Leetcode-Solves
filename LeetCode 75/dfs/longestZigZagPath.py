from tree import listToTree

def longestZigZag(root):
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return (-1, -1)
        print(node.val)

        left = dfs(node.left)
        right = dfs(node.right)
        print(left)
        print(right)
        print("")


        leftLen = left[1] + 1
        rightLen = right[0] + 1

        ans = max(ans, leftLen, rightLen)

        return (leftLen, rightLen)
    
    dfs(root)
    return ans

root = listToTree([1,2,3,None,4,None,None,5,6,None,7])
print(longestZigZag(root))