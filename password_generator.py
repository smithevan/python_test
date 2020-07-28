from random import randint
 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = []

while len(password) < 6: 
    letter_or_number = randint(0, 1)
    if letter_or_number == 0:  
        next_character_index = randint(0, 25)
        next_character = letters[next_character_index]
        password.append(next_character)
    elif letter_or_number == 1:
        password.append(randint(0, 9))

for character in password: 
    print (character)


