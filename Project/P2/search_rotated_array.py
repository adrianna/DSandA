###################################
## search_rotated_array.py
##
###################################

import pdb 

debug = 0
def rotated_array_search(input_list, number, start_index, end_index):

    start_index = 0
    end_index = len(input_list) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]
        
        if number == mid_element:
            return mid_index

        if debug:
            print("*** while ***")
            print("start, mid, end elements: {}, {}, {}".format(input_list[start_index], mid_element, input_list[end_index]))
            print("start, mid, end indices: {}, {}, {}".format(start_index, mid_index, end_index))
            pdb.set_trace()
            
        if isSorted(input_list, start_index, mid_index):
            if debug: print("\tbetween start and mid_index-1")
            
            if input_list[start_index] <= number <= input_list[mid_index]:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
                
        elif isSorted(input_list, mid_index + 1, end_index):
            if debug: print("\tbetween mid_index-1 and end_index")
            
            if input_list[mid_index+1] <= number <= input_list[end_index]:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
                
#        if debug:
#            print("start_index, mid_index, end_index: {}, {}, {}".format(start_index, mid_index, end_index))
#            pdb.set_trace()
        
    return -1

def isSorted(input_list, start_index = 0, end_index = 0):

    if input_list[start_index] < input_list[end_index]:
        return True
    
    return False


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    start_index = 0
    end_index = len(input_list) - 1
    
    if debug:
        print("my program: {}".format(rotated_array_search(input_list, number, start_index, end_index )))
        print("linear program: {}".format(linear_search(input_list, number)))
        
    if linear_search(input_list, number) == rotated_array_search(input_list, number, start_index, end_index ):
        print("Pass")
    else:
        print("Fail")

        
#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[7,8,9,1,2,3,4,5,6], 9])
