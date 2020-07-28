from random import randint
 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = []

while len(password) < randint(6, 15): 
    letter_or_number = randint(0, 1)
    capital_true_false = randint(0, 1)
    if letter_or_number == 0:  
        next_character_index = randint(0, 25)
        if capital_true_false == 1: 
            password.append(letters[next_character_index].upper())
        elif capital_true_false == 0:
            password.append(letters[next_character_index])
    elif letter_or_number == 1:
        password.append(randint(0, 9))

for character in password: 
    print (character)


