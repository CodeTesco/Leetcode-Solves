def myAtoi(s):
    word = s.strip()
    oper = 1
    if (word == ""):
        return 0
    elif (word == "+"):
        return 0
    elif (word == "-"):
        return 0

    let = "aho"
    if(word[0] == "+"):
        oper = 1
        word = word[1:]
    elif (word[0] == "-"):
        oper = -1
        word = word[1:]

    if (not (word[0].isdigit())):
        return 0

    num = ""
    for let in word:
        try:
            num += str(int(let))
        except ValueError:
            break
    
    returnee = oper * int(num)
    if (returnee > 2**31 - 1):
        returnee = 2**31 - 1
    elif(returnee < -(2**31)):
        returnee = -(2**31)

    return returnee

print(myAtoi(" ++1"))