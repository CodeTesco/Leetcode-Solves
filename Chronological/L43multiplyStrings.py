def multiply(num1, num2):
    if len(num1) < len(num2):
        placeholder = num1
        num1 = num2
        num2 = placeholder

    res = "0"
    zero_count = 0

    for i in range(len(num1) - 1, -1, -1):
        x = num1[i]
        part_mult = ""
        carry = 0
        for j in range(len(num2) - 1, -1, -1):
            y = num2[j]
            mult = str((int(x) * int(y)) + carry)
            part_mult = mult[-1] + part_mult
            if len(mult) == 2:
                if j == 0:
                    part_mult = mult[0] + part_mult
                    continue
                carry = int(mult[0])
            else:
                carry = 0
        
        for _ in range(zero_count):
            part_mult += "0"
        
        res = str(int(res) + int(part_mult))
        zero_count += 1

    return res

print(multiply("3", "514"))