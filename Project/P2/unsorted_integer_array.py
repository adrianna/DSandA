
###################################
## unsorted_integer_array
##
## Issue: None
##
## TODO:
##   1. Generate 3 test cases
## 
##
###################################



def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
 #   min_int = 999
 #   max_int = -1111
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

l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
#print("min(l): {}".format(min(l)))
#print("max(l): {}".format(max(l)))
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")
#print(get_min_max(l))
      
l = [i for i in range(-1, 10)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
#print("min(l): {}".format(min(l)))
#print("max(l): {}".format(max(l)))
print ("Pass" if ((-1, 9) == get_min_max(l)) else "Fail")
#print(get_min_max(l))

l = [i for i in range(-1111, 1000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-1111, 999) == get_min_max(l)) else "Fail")

l = [i for i in range(-1111111, -1111)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
print ("Pass" if ((-1111111, -1112) == get_min_max(l)) else "Fail")
#print(get_min_max(l))
#print(max(l))
#print(min(l))
