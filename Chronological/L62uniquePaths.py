def uniquePaths(m, n):
    map = dict()
    def numPaths(m, n):
        if map.get(f"({m}, {n})") is not None:
            return map[f"({m}, {n})"]
        if m == 1 or n == 1:
            return 1

        sum = numPaths(m-1, n) + numPaths(m, n-1)
        map[f"({m}, {n})"] = sum
        return sum
    return numPaths(m, n)

print(uniquePaths(23, 12))