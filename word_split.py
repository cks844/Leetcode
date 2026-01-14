"Split sentences without using split function"

def word_split(sent):
    words = ""
    split_words = []
    for char in sent:
        if char != " ":
            words += char
        elif words:
            split_words.append(words)
            words =""
    if words:
        split_words.append(words)

    return split_words
inp = input("Enter the sentence:")
word_split(inp)    

def word_split(sent):
    words = ""
    split_words = []
    for char in sent:
        if char != " ":
            words += char
        elif len(words) != 0:
            split_words.append(words)
            words = ""
    if len(words) != 0:
            split_words.append(words)

    return split_words
inp = input("Enter the sentence:")
print(word_split(inp))
