#given an integer, reverse it.  

integer = int(input("Input an Integer:"))
822

def reverse(integer):
    if integer % 10000000 > 0: 
        millions = int(integer / 1000000)
        integer = integer - (millions * 1000000)
        if integer % 100000 > 0:
            hundred_thousands = int(integer / 100000)
            integer = integer - (hundred_thousands * 100000)
            if integer % 10000 > 0: 
                ten_thousands = int(integer / 10000)
                integer = integer - (ten_thousands * 10000)
                if integer % 1000 > 0: 
                    thousands = int(integer / 1000)
                    integer = integer - (thousands * 1000)
                    if integer % 100 > 0: 
                        hundreds = int(integer / 100)
                        integer = integer - (hundreds * 100)
                        if integer % 10 > 0: 
                            tens = int(integer / 10)
                            integer = integer - (tens * 10)
    ones = integer
    reversed_int_array = [1000000 * ones, 100000 * tens, 10000 * hundreds, 1000 * thousands, 100 * ten_thousands, 10 * hundred_thousands, millions]
  
    while 0 in reversed_int_array: 
        reversed_int_array.remove(0)
    
    reversed_int = 0 
    for i in range(len(reversed_int_array)):
        length = 6 - i
        reversed_int = reversed_int + reversed_int_array[i]
    reversed_int = int(reversed_int / (10 ** length))
    
    return reversed_int
    
print(reverse(integer))
