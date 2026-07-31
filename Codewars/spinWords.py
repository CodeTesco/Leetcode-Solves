def spin_words(sentence):
    reversed = []
    words = sentence.split()
    
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        reversed.append(word)
    
    return " ".join(reversed)

print(spin_words("Welcome"))