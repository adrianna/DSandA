
###################################
## unsorted_integer_array
##
##
###################################



def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int = ints[0]
    max_int = ints[len(ints)-1]
    # Traverse the array comparing the elements to the stored integer
    # Replace the stored integer min or max with the smaller or larger of
    # the two numbers, respectively
    for num in ints:
        min_int = min(min_int, num)
        max_int = max(max_int, num)
        
    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

Test Case #1 
l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

Test Case #2
l = [i for i in range(-1, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-1, 9) == get_min_max(l)) else "Fail")

Test Case #3
l = [i for i in range(-1111, 1000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-1111, 999) == get_min_max(l)) else "Fail")

Test Case #4 with negative numbers
l = [i for i in range(-1111111, -1111)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-1111111, -1112) == get_min_max(l)) else "Fail")


