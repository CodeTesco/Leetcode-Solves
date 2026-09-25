from collections import defaultdict

def setMatrix(matrix):
    x_coor = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for r in range(len(matrix[0])):
                    x_coor.add((i, r))
                for r in range(len(matrix)):
                    x_coor.add((r, j))

    for coor in x_coor:
        matrix[coor[0]][coor[1]] = 0
        
    return matrix

print(setMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))