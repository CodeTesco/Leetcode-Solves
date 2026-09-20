def mySqrt(x):
    if x == 0:
        return 0

    x_curr = x / 2
    x_next = x_curr - (((x_curr * x_curr) - x) / (2 * x_curr))

    while (x_curr - x_next) > 0.1:
        x_curr = x_next
        x_next = x_curr - (((x_curr * x_curr) - x) / (2 * x_curr))

    return int(x_next)

print(mySqrt(20))
