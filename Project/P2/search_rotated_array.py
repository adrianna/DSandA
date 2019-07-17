###################################
## search_rotated_array.py
##
##
##
###################################



def rotated_array_search(input_list, number, start_index, end_index):

    start_index = 0
    end_index = len(input_list) - 1
    
    #print("[[rotated_array_search]], target number: {}".format(number))
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]
        
        if number == mid_element:
            return mid_index

        elif number < mid_element:

            if isSorted(input_list, start_index, mid_index - 1):
                mid_index = (start_index + mid_index - 1)//2
                mid_element = input_list[mid_index]
                if withinBoundary(input_list, number, start_index, mid_index-1):
                    end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        else:
             if isSorted(input_list, mid_index + 1, end_index):
                mid_index = (start_index + mid_index-1)//2
                mid_element = input_list[mid_index]
                if withinBoundary(input_list, number, mid_index + 1, end_index):
                    start_index = mid_index + 1
             else:
                    end_index = mid_index - 1
                
    return -1

def isSorted(input_list, start_index = 0, end_index = 0):

    if input_list[start_index] < input_list[end_index]:
        return True
    
    return False


def withinBoundary(input_list, number, start_index, end_index):

   
    if start_index >= 0 and end_index >=0:
        mid_index = (end_index-start_index) //2
        mid_element = input_list[mid_index]
        
        if input_list[start_index] <= number and number <= input_list[end_index]:
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
    print(rotated_array_search(input_list, number, start_index, end_index ))
    print(linear_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number, start_index, end_index ):
        print("Pass")
    else:
        print("Fail")

        
#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#test_function([[7,8,9,1,2,3,4,5,6], 9])
