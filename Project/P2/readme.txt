P2 Problems

## unsorted_integer_array.py

This problem asks to find the minimum and maximun elements in the array.
The method uses two storage elements min_int and max_int, which are set
to values outside the array element boundaries. For example, min_int is set
to 99, and max_int to -1. The array example has elements numbered [0-9].

For each element, we check against min_int and max_int and compare
whether the ith element is greater than or less than their respective
min_int/max_int storage values. For the case of min_int, we take the minimum
of the two values, i.e min_int  = min(min_int, element_ith). Likewise,
max_int = max(max_int, element_ith).

The program returns a tuple(min_int, max_int).

As we traverse the array, these two storage variables are updated. So,
the time it takes to traverse the array is O(n) given n-elements.
The comparision is O(1) for each iteration. Therefore there will be
O(1)*n = O(n)

The algorithm will take place in O(n) time.

# dutch_national_flag.py

This problem asks to sort list of elements (0,1,2) and return sorted array.
We create three empty lists to start: sorted_list, array_1, array_2. This takes
O(1) operation. As we traverse the array, there are three conditional
statements which we test the ith element for 0,1, or 2. This is an O(1)
operation. For each statement, we populate the sorted_list with 0, and
the other elements populate 1, and 2 in their respective arrays.

At the end of the traversal, we will have three arrays, which we can easily
append to the sorted array. This takes O(1). Therefore, total operation
of the function is O(n).

O(n) =  O(1)*3          create empty arrays
        n* O(1) + O(1)  for each conditional statement deciphering element
                        and appending to subsequent array O(1)
      + O(1)*2          appending two arrays into sorted_list array
      


