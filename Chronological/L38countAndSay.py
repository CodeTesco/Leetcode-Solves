def countAndSay(n):
    encoding = "1"

    def rle(enc):
        l = 0
        r = 1
        newEnc = ""

        while l < r:
            if r >= len(enc):
                newEnc += f"{r-l}{enc[l]}"
                break

            if not enc[r] == enc[l]:
                newEnc += f"{r-l}{enc[l]}"
                l = r
                r = l + 1
            else:
                r += 1

        return newEnc
    
    while n > 1:
        return rle(countAndSay(n - 1))

    return encoding

print(countAndSay(4))