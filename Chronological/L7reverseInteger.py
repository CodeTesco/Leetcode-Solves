def reverse(x):
    
    if (x < 0):
        prefix = "-"
    else:
        prefix = ""
    strInt = str(x).removeprefix("-")
    reversed = ""
    i = 0

    for let in strInt:
        rep = (i * -1) - 1
        reversed += strInt[rep]
        i += 1

    if (prefix != ""):
        reversed = prefix + reversed

    if ((int(reversed) > (2 ** 31) - 1) or (int(reversed) < -(2 ** 31))):
        return 0

    return int(reversed)

print(reverse(1534236469))