user_input = input("Type a Sentence:")
wordcount = 0


for i, character in enumerate(user_input): 

    if character == " ": 
        wordcount += 1 

    if not i:
        wordcount += 1
    
    if character == user_input[len(user_input) -1] and character == " ":
        wordcount -= 1

if wordcount == 1:
    print("I see " + str(wordcount) + " word")
else:
    print("I see " + str(wordcount) + " words")

