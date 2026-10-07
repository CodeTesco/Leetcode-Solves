def findCircleNum(isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces

        # 1, 1, 0
        # 1, 1, 0
        # 0, 0, 1