number = 1
while number != 100: 
    number = int(input())

    def count_to_ten(number):
        while number < 10:
            number += 1
            print (number)
        print (" ")

    count_to_ten(number)