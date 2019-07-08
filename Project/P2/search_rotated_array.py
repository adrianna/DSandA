###################################
## search_rotated_array.py
##
##
## TODO:
##   1. Fix for TC #3 (uncommented)
##   2. Generate 3 test cases
## 
##
###################################



def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    start_index = 0
    end_index = len(input_list) - 1

    #print("[[rotated_array_search]], target number: {}".format(number))
    while start_index <= end_index:
        #print("\tstart_index: {}, end_index: {}".format(start_index, end_index))
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]
        
        if number == mid_element:
            print("\t\tfound!")
            return mid_index

        elif number < mid_element:
            
            #print("number < mid_element: {}".format(mid_element))
            if withinBoundary(input_list[ mid_index + 1 : end_index], number):
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1

        else:
            
            #print("number > mid_element: {}".format(mid_element))
            #print("passing, start_index: {}, mid_index: {}".format(start_index, mid_index))
            #if withinBoundary(input_list[start_index : mid_index-1], number):         ## Fails TC3, but Passes TC4 and TC5;
            if withinBoundary(input_list[start_index : mid_index], number):         ## Passes TC3, but Fails TC4 and TC5;
                end_index = mid_index - 1 
            else:    
                start_index = mid_index + 1
    
    return -1


def withinBoundary(input_list, number):

    start_index = 0
    end_index = len(input_list)-1


    if start_index >= 0 and end_index >=0:
        #print("[[withinBoundary]] start: {}, end: {}".format(start_index, end_index))
        #print("[[withinBoundary]] start_element: {}, end_element: {}".format(input_list[start_index], input_list[end_index]))
        if input_list[start_index] <= number and number <= input_list[end_index]:
            return True

        
    # print("[[withinBoundary]] FALSE")
    return False
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

        
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[7,8,9,1,2,3,4,5,6], 9])
