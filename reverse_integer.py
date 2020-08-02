#given an integer, reverse it.  

integer = int(input("Input an Integer:"))
822

def reverse(integer):
    if integer % 100 > 0: 
        hundreds = int(integer / 100)
        integer = integer - (hundreds * 100)
        if integer % 10 > 0: 
            tens = int(integer / 10)
            integer = integer - (tens * 10)
    ones = integer
    reversed_int_array = [100 * ones, 10 * tens, hundreds]
    reversed_int = 0 
    for i in range(len(reversed_int_array)):
        reversed_int = reversed_int + reversed_int_array[i]
    
    return reversed_int
   

    

print(reverse(integer))
