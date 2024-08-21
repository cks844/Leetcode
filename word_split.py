"Split sentences without using split function"

def word_split(sen):
    word = ""
    words=[]
    for char in sen:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word =""
    if word:
        words.append(word)
    return words
inp = input("Enter the sentence:")
word_split(inp)    