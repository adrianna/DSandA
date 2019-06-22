def heapify(input_list, n, idx):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    
    # consider current index as largest
    largest_index = idx 
    left_node = 2 * idx + 1     
    right_node = 2 * idx + 2     
  
    # compare with left child
    if left_node < n and input_list[idx] < input_list[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and input_list[largest_index] < input_list[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != idx: 
        input_list[idx], input_list[largest_index] = input_list[largest_index], input_list[idx] 
    
        heapify(input_list, n, largest_index) 
        
def sort(input_list):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(input_list) 
  
    # Build a maxheap. 
    for idx in range(n, -1, -1): 
        heapify(input_list, n, idx)
  
    # One by one extract elements 
    for idx in range(n-1, 0, -1): 
        input_list[idx], input_list[0] = input_list[0], input_list[idx] # swap 
        heapify(input_list, idx, 0) 

    return input_list


def convert_list2digits(input_list, digit):

    #print("\t[[convert_list2digits]], input 1: {}".format(digit))
    #print("\t[[convert_list2digits]], input 2: {}".format(input_list))
    num_list = digit + input_list

    #print("\t[[conver_list2digits]]: {}".format(num_list))
    n = len(num_list) - 1

    
    number = 0
    for idx in range(n, -1, -1):
        number += num_list[idx] * 10**idx

    return number
        
    


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort the array
    # If the array is odd number,
    # create two pairs of numbers, whose lengths will differ by 1
    #   1. The first number will start from the largest (last index in the array) and
    #      the numbers until array.size() - array.size()/2+1
    #   2. Create the num string by picking the larger to be:
    #      arry[:-n/2] and substituting the last digit for the last digit in the
    #      sub-array
    #   3. If there is an even number of elements, the array is divided in half
    #      but we create two addend by constructing

    # Size of the input_list

    input_list = sort(input_list)

    n = len(input_list)
    if n % 2 == 0:
        # print("number of elements are even: {}".format(n))
        last = n
        first = 0
        second = first+1

        # Construct the larger number
        addend_1 = convert_list2digits(input_list[second:last:2], [])
        # Construct the smaller number
        addend_2 = convert_list2digits(input_list[first:last:2], [])
        
    else:
        # print("number of elements are odd: {}".format(n))
        mid = (n)//2
        lb = mid + 1  # Digits for the larger addend
        ub = mid - 1  # Digits for the smaller addend
        
        addend_1 = convert_list2digits(input_list[lb:n], [input_list[mid-1]])
        addend_2 = convert_list2digits([input_list[mid]], input_list[0:ub])
        
    sum = addend_1 + addend_2
    # print("sum: {}".format(sum))
    # print("Returning [{}, {}]".format(addend_1, addend_2))

    return addend_1, addend_2



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
#input_list = [4, 6, 2, 5, 9, 8]
#input_list = [1, 2, 3, 4, 5]
#print(rearrange_digits(input_list))

