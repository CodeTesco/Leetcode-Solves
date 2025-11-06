def generateParenthesis(n):
    parenArr = []
    
    def backtrack(s, l, r):
        if (len(s) == 2 * n):
            parenArr.append(s)
            return
        if (l < n):
            backtrack(s + "(", l + 1, r)
        if (r < l):
            backtrack(s + ")", l, r + 1)
    backtrack("", 0, 0)
        
    return parenArr

print(generateParenthesis(3))

# ()
# 1 - ()
# 2 - (()), ()()
# 3 - ((())), (()()), ()()(), (())(), ()(())