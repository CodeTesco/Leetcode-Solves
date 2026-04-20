def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

# transpose + reverse row

# 1 4 7
# 2 5 8
# 3 6 9

# 1 4 7
# 4 5 6
# 7 8 9

# 0,n-1 = 0,0
# n-1,n-1 = 0,n-1
# n-1,0 = n-1,n-1
# 0,0 = n-1,0

# 1, n-1 = 0, 1
# n-1, (n-2) = 1, n-1
# (n-2) ,0 = n-1, (n-2)
# 0, 1 = (n-2), 0

# n = 4

# 

# 1,2 = 1,1
# 2,2 = 1,2
# 2,1 = 2,2
# 1,2 = 2,1

# 0,0 = 0,2
# 0,2 = 2,2
# 2,2 = 2,0
# 2,0 = 0,0

# 0,1 = 1,2
# 1,2 = 2,1
# 2,1 = 1,0
# 1,0 = 0,1