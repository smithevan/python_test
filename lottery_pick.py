from random import randint 

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
picked_numbers = []

while len(picked_numbers) < 6:
    for number in lottery_numbers: 
        iterator = randint(1, len(lottery_numbers))
        if number == iterator: 
            picked_numbers.append(number)
            lottery_numbers.remove(number)
    

for number in picked_numbers:
    print (number)
    
    