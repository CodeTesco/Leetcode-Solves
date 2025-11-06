def kidsWithCandies(candies, extraCandies):
    greatestArr = []

    highest = 0

    for el in candies:
        if el > highest:
            highest = el

    for el in candies:
        if (el + extraCandies >= highest):
            greatestArr.append(True)
        else:
            greatestArr.append(False)

    return greatestArr

print(kidsWithCandies([2,3,5,1,3], 3))