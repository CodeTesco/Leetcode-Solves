from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])
    root.left = list_to_tree(arr, 2*i+1)
    root.right = list_to_tree(arr, 2*i+2)

    return root

def rightSideView(root):
    if not root:
        return []

    visited = set([root])
    queue = deque([root])
    level = 0
    result = []

    while queue:
        level_size = len(queue)
        result.append(queue[-1].val)

        for _ in range(level_size):
            current = queue.popleft()

            if current.left and current.left not in visited:
                visited.add(current.left)
                queue.append(current.left)
            if current.right and current.right not in visited:
                visited.add(current.right)
                queue.append(current.right)
        level += 1

    return result


root = list_to_tree([1,None,3])
print(rightSideView(root))