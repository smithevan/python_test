user_input = input("Type a Sentence:")
wordcount = 0

for character in user_input: 
    if character == " ": 
        wordcount += 1 
    if character == user_input[len(user_input) -1]:
        wordcount += 1

print(wordcount)

