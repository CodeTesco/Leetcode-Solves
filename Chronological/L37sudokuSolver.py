class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(index=0):
            if index == len(empty_cells):
                return True 

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + c // 3

            for val in map(str, range(1, 10)):
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)

            return False

        backtrack()
        return board

solver = Solution()
print(solver.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))