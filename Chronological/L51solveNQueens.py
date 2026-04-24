def solveNQueens(n):
    res = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    sol = [["." for _ in range(n)] for _ in range(n)]

    def updateBoard(board, r, c, val):
        for i in range(n):
            board[r][i] += val
            board[i][c] += val
        
        board[r][c] -= val

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            curr_r, curr_c = r + dr, c + dc
            while 0 <= curr_r < n and 0 <= curr_c < n:
                board[curr_r][curr_c] += val
                curr_r += dr
                curr_c += dc

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in sol])
            return

        for col in range(n):
            if board[row][col] == 0:
                sol[row][col] = "Q"
                updateBoard(board, row, col, 1) 
                
                backtrack(row + 1)
                
                sol[row][col] = "."
                updateBoard(board, row, col, -1) 

    backtrack(0)
    return res

print(solveNQueens(4))