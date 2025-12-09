def decodeString(s):
    numStack = []
    strStack = []
    curr = ""
    k = 0

    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == '[':
            numStack.append(k)
            strStack.append(curr)
            k = 0
            curr = ""
        elif ch == ']':
            repeat = numStack.pop()
            prev = strStack.pop()
            curr = prev + curr * repeat
        else:
            curr += ch

    return curr

print(decodeString("3[a2[c]]"))
