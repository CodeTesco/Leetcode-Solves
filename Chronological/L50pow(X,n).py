def myPow(x, n):
    def dfs(x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        half = dfs(x, n // 2)
        mult = half * half

        return mult if n % 2 == 0 else mult * x

    res = dfs(x, abs(n))
    if n < 0:
        return 1/res
    else:
        return res


print(myPow(2, -2))