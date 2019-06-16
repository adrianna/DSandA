def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int = 99
    max_int = -1
    # Traverse the array comparing the elements to the stored integer
    # Replace the stored integer min or max with the smaller or larger of
    # the two numbers, respectively
    for num in range(len(ints)):
        min_int = min(min_int, num)
        max_int = max(max_int, num)
        
    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
