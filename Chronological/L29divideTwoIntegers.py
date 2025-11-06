import math

def divide(dividend, divisor):
    quotient = 0
    
    if (dividend == 0):
            return 0
        
    hasMinus = False
    if (str(divisor)[0] == "-" and str(dividend)[0] == "-"):
        dividend = int(str(dividend)[1:])
        divisor = int(str(divisor)[1:])
        hasMinus = False
    else:
        if (str(dividend)[0] == "-"):
            dividend = int(str(dividend)[1:])
            hasMinus = True
        elif (str(divisor)[0] == "-"):
            divisor = int(str(divisor)[1:])
            hasMinus = True

    while (divisor <= dividend):
        print(divisor)
        copyDivisor = divisor
        mult = 1

        while (dividend >= (copyDivisor << 1)):
            copyDivisor <<= 1
            mult <<= 1

        dividend -= copyDivisor
        quotient += mult

    if (hasMinus == True):
        quotient = int("-" + str(quotient))

    if (quotient > (2**31 - 1)):
        return 2**31 - 1
    elif (quotient < -(2**31)):
        return -(2**31)

    return quotient

print(divide(20, 3))
# 20, 3
# 3 6 12
# 3 6 9 12 15 18

# 15, 4
# 4 8
# 4 8 12