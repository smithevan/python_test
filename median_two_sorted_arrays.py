#return median of two sorted arrays 

array1 = [1, 4, 6, 7, 16, 22]
array2 = [3, 5, 8, 9, 12, 14]
#median is 7.5

def get_median(array1, array2):
    full_array = array1 + array2
    full_array.sort()
    number_of_elements = len(full_array)
    if number_of_elements % 2 == 0:
        first_number = int(number_of_elements / 2 - 1)
        second_number = int(number_of_elements / 2)
        median = (full_array[first_number] + full_array[second_number]) / 2
        return median
    #elif number_of_elements % 2 > 0: 

print(get_median(array1, array2))
