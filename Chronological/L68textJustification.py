def fullJustify(words, maxWidth):
    paragraph = []
    sentence = []
    sentence_length = 0

    for i, word in enumerate(words):
        if (sentence_length + len(word)) > maxWidth:
            if len(sentence) > 2 or sentence_length > maxWidth:
                sentence.pop()
                sentence_length -= 1
            remainder = maxWidth - sentence_length
            j = 1
            while remainder > 0:
                if j >= len(sentence):
                    j = 1
                sentence[j] += " "
                remainder -= 1
                j += 2
            line = "".join(sentence)
            paragraph.append(line)
            sentence = []
            sentence_length = 0
        if i == len(words) - 1:
            sentence.append(word)
            sentence_length += len(word)
            remainder = maxWidth - sentence_length
            sentence.append(" " * remainder)
            line = "".join(sentence)
            paragraph.append(line)

        sentence.append(word)
        sentence.append(" ")
        sentence_length += (len(word) + 1)
        # print(sentence)
        # print(sentence_length)

    return paragraph

print(fullJustify(["What","must","be","acknowledgment","shall","be"], 16))