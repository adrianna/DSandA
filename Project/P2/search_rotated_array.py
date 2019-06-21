def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    
# Rotate Array by Pivot, x
def rotateLeft(input_list, x):
    temp = input_list[0]
    end = len(input_list) - 1
    for dgt in range(x):
        #print("Currently: {}".format(input_list[dgt]))
        #print("At dgt+x: {}, number: {}".format(dgt+x,input_list[dgt+x]) )
        input_list[dgt], input_list[dgt+x]  = input_list[dgt+x], input_list[dgt]
        #print("Now: {}".format(input_list[dgt]))
    input_list[x] = temp

    #input_list[end] = temp

    return input_list

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


input_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
print("Before: {}".format(input_list))

print("pivot at 4")
print("After: {}".format(rotateLeft(input_list, 4)))
print("pivot at 3")
input_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
print("After: {}".format(rotateLeft(input_list, 3)))
print("pivot at 2")
input_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
print("After: {}".format(rotateLeft(input_list, 2)))

        
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
