def addBinary(a, b):
    return bin(int(a, base=2) + int(b, base=2))[2:]

print(addBinary("1010", "1011"))