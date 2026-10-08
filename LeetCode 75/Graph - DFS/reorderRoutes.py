from collections import deque, defaultdict

def minReorder(self, n: int, connections):
        changes = 0
        visited = set([0])
        queue = deque([0])
        adj_list = defaultdict(list)

        for u, v in connections:
            adj_list[u].append((v, 1))
            adj_list[v].append((u, -1))
        
        while queue:
            node = queue.popleft()
            neighbors = adj_list[node]

            for neighbor in neighbors:
                if neighbor[0] not in visited:
                    if neighbor[1] == 1:
                        changes += 1
                    queue.append(neighbor[0])
                    visited.add(neighbor[0])

        return changes