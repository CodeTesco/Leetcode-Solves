def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
        return 0

    for i, row in enumerate(obstacleGrid):
        for j, cell in enumerate(row):
            if cell == 1:
                obstacleGrid[i][j] = "*"

    for i in range(m):
        if obstacleGrid[i][0] == "*":
            break
        obstacleGrid[i][0] = 1
    for j in range(n):
        if obstacleGrid[0][j] == "*":
            break
        obstacleGrid[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == "*":
                continue
            elif obstacleGrid[i-1][j] == "*" and not obstacleGrid[i][j-1] == "*":
                obstacleGrid[i][j] = obstacleGrid[i][j-1]
            elif not obstacleGrid[i-1][j] == "*" and obstacleGrid[i][j-1] == "*":
                obstacleGrid[i][j] = obstacleGrid[i-1][j]
            elif not obstacleGrid[i-1][j] == "*" and not obstacleGrid[i][j-1] == "*":
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j] = 0
    
    return obstacleGrid[m-1][n-1]

print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))