from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToList(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values (they carry no structural info)
    while result and result[-1] is None:
        result.pop()

    return result

def listToTree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        # Left child
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

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


