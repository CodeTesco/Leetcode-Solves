def isValid(s):
    opener = "([{"
    stack = []
    valid = True

    if not (len(s) % 2 == 0):
        return False

    for let in s:
        if let in opener:
            stack.append(let)
        elif stack:
            if let == ")" and stack[-1] == "(":
                stack.pop()
                continue
            elif let == "]" and stack[-1] == "[":
                stack.pop()
                continue
            elif let == "}" and stack[-1] == "{":
                stack.pop()
                continue
            else:
                return False
        else: 
            return False

    if not (len(stack) == 0):
        return False
    return valid

print(isValid("){"))
