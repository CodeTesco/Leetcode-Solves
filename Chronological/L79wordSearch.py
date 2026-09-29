def exist(board, word):
    def dfs(cell, visited, remain):
        if cell[0] >= len(board) or cell[0] < 0 or cell[1] >= len(board[0]) or cell[1] < 0:
            return False
        if board[cell[0]][cell[1]] != remain[0]:
            return False

        if len(remain) == 1:
            return True
        
        visited.add(cell)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = [(dirs[i][0] + cell[0], dirs[i][1] + cell[1]) for i in range(len(dirs))]
        if board[cell[0]][cell[1]] == remain[0]:
            remain = remain[1:]

        for neighbor in neighbors:
            if neighbor not in visited:
                if dfs(neighbor, visited, remain):
                    return True
        visited.remove(cell)
        return False
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if dfs((r, c), set(), word):
                    return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "A"))
