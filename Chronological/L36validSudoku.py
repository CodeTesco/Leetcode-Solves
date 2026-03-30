def isValidSudoku(board):
    column = []
    valid = True

    for i in range(9):
        for j in range(9):
            if not (board[j][i] == "."):
                column.append(board[j][i])
        row = [x for x in board[i] if not x == "."]
        if not len(set(row)) == len(row) or not len(set(column)) == len(column):
            valid = False
            break
        column.clear()
    
    box = []
    count = 0
    colCount = 0

    for _ in range(3):
        for i in range(9):
            count += 1
            for j in range(3):
                j += colCount
                if not (board[i][j] == "."):
                    box.append(board[i][j])
            if count == 3:
                if not (len(set(box)) == len(box)):
                    valid = False
                    break
                count = 0
                box = []
        colCount += 3

    return valid

print(isValidSudoku([["1","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

# arr = [1, 2, 2, 3]
# print(len(set(arr)))

# print(row)
# print(column)
# print("")