def plusOne(digits):
    number = int("".join(map(str, digits)))
    numPlus = str(number + 1)

    return [int(num) for num in numPlus]

print(plusOne([9]))