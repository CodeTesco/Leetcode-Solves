from collections import deque

def canVisitAllRooms(rooms):
    keys = set([0])
    queue = deque([0])
    visited = []

    while queue:
        idx = queue.popleft()
        new_keys = rooms[idx]
        for key in new_keys:
            if key not in keys:
                queue.append(key)
                keys.add(key)
        visited.append(idx)

    if len(visited) == len(rooms):
        return True
    else:
        return False