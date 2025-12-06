def equalPairs(grid):
    count = 0
    for i in range(len(grid)):
        arr = grid[i]
        arr2 = []
        for j in range(len(arr)):
            arr2.append(grid[j][i])
        for el in grid:
            if arr2 == el:
                count += 1

    return count

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))