from collections import deque

def searchBST(root, val):
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()
            if current.val == val:
                return current

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return None