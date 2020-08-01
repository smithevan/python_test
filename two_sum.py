#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

array_set = [1, 5, 9, 34] #target 10
target = 10

def two_sum(array, target):
    first_number = 0
    second_number = 0
    for x in range(len(array)): 
        first_number = array[x]
        first_number_index = x
        for y in range(len(array)): 
            second_number = array[y]
            second_number_index = y
            if first_number + second_number == target:
                return [first_number_index, second_number_index]

    
    
    
   
    #for array_element in array: 
        #while first_number + second_number != target: 
            #if first_number == 0 and second_number == 0: 
             #   first_number = array[array_element]
    #        elif first_number != 0 and second_number == 0:
    #            second_number = array[array_element] 
    #        elif first_number != 0 and second_number != 0:
    #            first_number = second_number
    #            second_number = array[array_element]
    #        return [array_element - 1, array_element + 1]

print(two_sum(array_set, target))
        
        
