def climbStairs(n):
    climbStairs(n-1) + climbStairs(n-2)

print(climbStairs(10))