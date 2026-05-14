def spiralOrder(matrix):
    m = len(matrix) # 3
    n = len(matrix[0]) # 3
    length = m*n
    spiral = []

    coordinates = [[0, 0], [1, n-1], [m-1, n-2], [m-2, 0]]
    directions = [[(0, 1), (1, 1)], [(1, 0), (1, -1)], [(0, -1), (-1, -1)], [(-1, 0), (-1, 1)]]
    boundaries = [n, m-1, n-1, m-2]
    j = 0

    while len(spiral) < length:
        # print(coordinates)
        # print(directions)
        # print(boundaries)
        idx = j % 4
        bound = boundaries[idx]
        loc = coordinates[idx][:]
        direction = directions[idx][0]
        boundDirection = directions[idx][1]

        for _ in range(bound):
            # print(loc)
            # print(spiral)
            # print("")
            x, y = loc[0], loc[1]
            spiral.append(matrix[x][y])
            if len(spiral) >= length:
                break

            loc[0] += direction[0]
            loc[1] += direction[1]

        boundaries[idx] -= 2
        coordinates[idx][0] += boundDirection[0]
        coordinates[idx][1] += boundDirection[1]
        j += 1

    return spiral
    
print(spiralOrder([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16],
                   [17,18,19,20],
                   [21,22,23,24]]))
