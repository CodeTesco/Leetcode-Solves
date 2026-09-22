def simplifyPath(path):
    stack = []
    path = path.split("/")

    for el in path:
        if el == "" or el == ".":
            continue
        elif el == "..":
            if len(stack) == 0:
                continue
            stack.pop()
        else:
            stack.append(el)

    return "/" + "/".join(stack)
        

print(simplifyPath("/.../a/../b/c/../d/./"))