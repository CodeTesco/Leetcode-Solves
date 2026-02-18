from tree import listToTree

def lowestCommonAncestor(root, p, q):
    if not root:
        return
        
    if root.val == p or root.val == q:
        return root
    
    leftFound = lowestCommonAncestor(root.left, p, q)
    rightFound = lowestCommonAncestor(root.right, p, q)
    
    if leftFound and rightFound:
        return root

    return leftFound or rightFound

root = listToTree([3,5,1,6,2,0,8,None,None,7,4])
result = lowestCommonAncestor(root, 5, 1)
print(result.val)