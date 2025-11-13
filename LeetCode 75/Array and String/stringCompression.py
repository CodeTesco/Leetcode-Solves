def compress(chars):
    count = 1
    i = 1

    while i < len(chars):
        print(chars)
        if (chars[i] == chars[i-1]):
            chars.pop(i)
            count += 1
        else:
            if (not (count == 1)):
                if (count >= 10):
                    strCount = str(count)
                    for el in strCount:
                        chars.insert(i, el)
                        i+=1
                else:
                    chars.insert(i, str(count))
                    i+=1
            count = 1
            i += 1

    if (not (count == 1)):
        if (count >= 10):
            strCount = str(count)
            for el in strCount:
                chars.append(el)
        else:
            chars.append(str(count))

    print(chars)

    return len(chars)

print(compress(["E","u","e","e","e","e","e","e","e","e","e","9","9","9","9","R","8","%","%","2","2","2",")",")",")"]))