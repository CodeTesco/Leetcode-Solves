from collections import deque

def maxLevelSum(root):
    max_sum = root.val
    level = 1
    max_level = level
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            current = queue.popleft()
            level_sum += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
        level += 1
    return max_level