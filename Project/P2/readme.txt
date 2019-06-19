P2 Problems

## rearrange_array_elements.py
This problem asks to find the largest sum from the list of digits. The digits
must be grouped into two addend	      s with one addend no larger in size by one digit.

First, use an efficient sort routine such as merge sort. This will provide a
O(nlogn) operation.

To create the largest sum, we divide the sorted array into two. Depending
whether the array has an even or odd number, this will determine the size of
the two addends. For the an even number of the array, we can divide the two
array into two addends of equal number of digits. For the odd, it will be
two addends with the size (number of digits) differed by 1 digit length.

To construct the largest sum, the method for even number of digits in the list is
slightly different than how it is constructed for the odd number of digits
in the list. Basically, we want to order the list, so that we select the
largest digits to be in the highest power position to the base 10.

For even number of digits, we construct the array using python's
slicing syntax. The slicing will select starting from the last position
and skip a digit as it selects the next one in steps of 2 indices.
This array is made a "copy" in the subroutine, convert_list2digits(),
which converts the list into an actual number.

For the odd number of digits, we constrct the array, similarly, but we
have two addends, whose length differ by one element in the list. First,
we calculate the midpoint index. This will divide the list in half. Then, we
start from the end of the sorted list until 'midpoint + 1'. We add another
element from second half at index 'midpoint - 1'. The other addend is
constructed going the opposite direction, start at the 0th position and going until
'midpoint-1' and then appending the midpoint element. This is to ensure that
the second addendum has a digit larger in the position of the highest power to the
base 10.

Finally, in the subroutine, conver_list2digits(), this takes the spliced array
and makes a local copy to the routine. It then loops downward in the list,
adding each element to construct the number, according to the formula:

digit* 10^idx

This operation will take roughly O(n//2) because we're using roughly
half the list (depending if it's odd or even) to loop through the digit
elements in creating the number (addend).

The function rearrange_digits calls conver_list2digits() twice, so
effectively it will loop all n elements in the input_list.

This will have an O(n) operation.

The total operation is O(nlogn) + O(n) ~ O(nlogn) for large n.
The first attributes to sorting the array, and the second for looping
the array to construct the two addends.



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
      


