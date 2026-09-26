def searchMatrix(matrix, target):
    row = []
    
    l, r = 0, len(matrix) - 1
    while l <= r:
        mid = (l + r) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            row = matrix[mid]
            break
        elif target < matrix[mid][0]:
            r = mid - 1
        elif target > matrix[mid][-1]:
            l = mid + 1
    
    if not row:
        return False

    l, r = 0, len(row) - 1
    while l <= r:
        mid = (l + r) // 2
        if target < row[mid]:
            r = mid - 1
        elif target > row[mid]:
            l = mid + 1
        else:
            return True
    
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 31))