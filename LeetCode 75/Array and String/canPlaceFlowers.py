def canPlaceFlowers(flowerbed, n):
    length = len(flowerbed)
    i = 0

    if (n == 0):
            return True

    if (length == 0 and n > 0):
        return False
    elif (length == 1 and flowerbed[0] == 1 and n > 0):
            return False
    elif (length == 1 and flowerbed[0] == 0 and n > 0):
        if (n == 1):
            return True
        else: 
            return False

    if (flowerbed[1] == 1 and flowerbed[0] == 0):
        i = 3
    elif (flowerbed[0] == 1 and flowerbed[1] == 0):
        i = 2
    
    while (i < length and n >= 0):
        if (flowerbed[i] == 1):
            i += 2
            continue
        elif (flowerbed[i] == 0 and i == (length - 1)):
            flowerbed[i] = 1
            i += 2
            n -= 1
        elif (flowerbed[i] == 0 and flowerbed[i+1] == 0):
            flowerbed[i] = 1
            i += 2
            n -= 1
        elif (flowerbed[i] == 0 and flowerbed[i+1] == 1):
            i += 3

    if (n > 0):
        return False
    else:
        return True

print(canPlaceFlowers([1], 0))