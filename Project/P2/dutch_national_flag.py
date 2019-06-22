###################################
## dutch_national_flag
##
## Issue: None
##
## TODO:
##   1. Not sure if I generate more unique test cases
##      that was already provided
## 
## Questions
##   1. Solution was given in lectures, although this one does not optimize
##      on space complexity, it does solve the issue in one pass
##
###################################



def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Traverse the array
    # Build three arrays for each value
    # After traversal, append them in order to sorted_list
    # Return sorted list
    
    sorted_list = []
    list_1 = []
    list_2 = []
    for element in range(len(input_list)):
        if input_list[element] == 0:
            sorted_list.append(0)
        elif input_list[element] == 1:
            list_1.append(input_list[element])
        elif input_list[element] == 2:
            list_2.append(input_list[element])

    sorted_list += list_1 + list_2

    return sorted_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
