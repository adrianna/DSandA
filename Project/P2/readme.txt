P2 Problems



#################################################
##
## sqrt().py
##
##
#################################################

###### Design

This problem asks to find the floor value of the square root.
To solve this problem, a hash table of a bounded sequence was constructed.



To find the srqt(x), for x > 400, the algorithm was not further developed.
An idea here is to find a number divisible, where one of the divisor can be found
in the table and the other divisor can be estimated with the current sqrt()
implementation for values bounded in the hash. For example,
sqrt(1000) = sqrt(100)*sqrt(10) = 10*3 = 30, where sqrt(10) = 3 (the floor value).
Both values can be found in the table.

Another approach would be to take the log. Given x^2 = y, where y is given and
x is unknown, we can solve the equation by:

log10 y = 2 * log10 x
log 10 x = 0.5*log10 y
x = 10^(0.5*log10 y)

Then, x can be rounded down.


Back to the first implementation using the hash table:
Given a value in the bounded data structures, a binary search is performed looking
for the sqrt of the squared number given. When the squared value, x, is given, the
binary search will start at midpoint and look up in the hash for the sqare root value.
It will then compare this value to the hash lookup of midpoint+1. By comparing the square
root value between the hash midpoint and midpoint+1, the result should be between those two
hash values. The result is chosen with the midpoint (the lower of the two).

The program will test for corner cases as it does not seem to find sqrt(400).
As a result, this upper bound case will test for the input and return what is
in the hash-key table.


###### Time Complexity

The hash table that was used in the lookup provides O(1) constant time for look up.
However, to find the key to the hash, the bineary search employed in the program has 
O(log n) performance.

Therefore, if a larger hash of n keys were implemented, it would still take O(log n) to search
for the right key-value pair. The total time for the execution is:
O(n) ~ O(log n) + O(1)
     ~ O(log n)

O(log n) is the total operation time of sqrt.py


###### Space Complexity

The space complexity can grow very large, depending how many values can  and is therefore not an
efficient program.

Therefore, O(n) is the total space complexity.



#################################################
##
## rearrange_array_elements.py
##
##
#################################################


###### Design

This problem asks to find the largest sum from the list of digits. The digits
must be grouped into two addends with one addend no larger in size by one digit.

First, an efficient sort routine was utilized for this implement. This will provide a
O(n log n) operation.

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

Finally, in the subroutine, convert_list2digits(), this takes the spliced array
and makes a local copy to the routine. It then loops downward in the list,
adding each element to construct the number, according to the formula:

digit* 10^idx

###### Time Complexity

The heap sort used in the algorithm has an O(n log n) operation. It takes a large unsorted array and
divides it between a sorted and unsorted region. As it iterates through each successive unsorted region,
the algorithm selects the largest element and puts it into the sorted array region.

In the convert_list2digits(), this operation will take roughly O(n//2) because we're using
roughly half the list (depending if it's odd or even) to loop through the digit elements in
creating the number (addend).

The function rearrange_digits() calls convert_list2digits() twice, so effectively it will loop all n elements
in the input_list. This will have an O(n) operation.

The total operation for the function rearrange_digits() is:
     O(n) ~ O(n) + O(n*log n) for large n    [1]
     	  ~ O(n)(1 + log n)                  [2]
 	  ~ O(n)(log n)                      [3]
	  ~ O(n*log n)                       [4]

O(n) ~ O(n*log n)

In the above equation [1], the first attributes to sorting the array, and the second for looping
the array to construct the two addends.



###### Space Complexity

The heap sort will provide the most efficient space complexity, as it is an in-place sort algorithm.
Heap sort moves elements between a sorted and unsorted region as it walks through.

The convert_list2digits will take n//2 elements from the array and make a local copy
and carry out its algorithm to convert a list of numbers into a number literal. This space complexity
would depend on the number of elements, n//2.
O(n) ~ O(n//2)
     ~ O(n)

Nonetheless, the total space complexity is O(n).


#################################################
##
## unsorted_integer_array.py
##
##
#################################################

###### Design

This problem asks to find the minimum and maximun elements in the array. The method uses two storage
elements min_int and max_int, which are set to values outside the array element boundaries. For
example, min_int is set to last element of the input list, and max_int to first element of the input
list. The array example has elements numbered [0-9].

For each element, we check against min_int and max_int and compare whether the i-th element is greater
than or less than their respective min_int/max_int storage values. For the case of min_int, we take
the minimum of the two values, i.e.
     min_int  = min(min_int, element_ith).

Likewise,
     max_int = max(max_int, element_ith).

The program returns a tuple(min_int, max_int).


###### Time Complexity

As we traverse the array, these two storage variables are updated. So,
the time it takes to traverse the array is O(n) given n-elements.
The comparision is O(1) for each iteration. Therefore there will be
O(n) ~ O(1)*n
     ~ O(n)

The algorithm will take place in O(n) time.


###### Space Complexity

The algorithm is in-place, in other words, it does not take more space other than the two O(1)
storage variables and updates them as we traverse the array.

Therefore, space complexity is:

O(n) ~ 2*O(1) + O(n)
     ~ O(n)


#################################################
##
## dutch_national_flat.py
##
##
#################################################

###### Design

This problem asks to sort list of elements (0,1,2) and return sorted array. We create three empty lists
to start: sorted_list, array_1, array_2. This takes O(1) operation. As we traverse the array, there are
three conditional statements which we test the i-th element for 0,1, or 2. For each statement, we populate
the sorted_list with 0, and the other elements populate 1, and 2 in their respective arrays.

At the end of the traversal, we will have three arrays, which we can easily append to the sorted array.

###### Time Complexity

The time complexity is formulated by accounting all the O(1) operation conditional testing to allocate
each element into the appropriate sub-array. To traverse the array of n, elements, this will take O(n).


To summarize the derivation of the total operation:

O(n) ~   O(1)*3          create empty arrays
       + n* O(1) + O(1)  for each conditional statement deciphering element
                        and appending to subsequent array O(1)
       + O(1)*2          appending two arrays into sorted_list array

Therefore, total operation: O(n) ~ O(n) 


###### Space Complexity

The space complexity is not efficient because we will create arrays for 1's and 2's and then append them to
the original one. The space complexity is derived:

O(n) ~ O(x) + O(y) + O(z),  where n = x+y+z, for x-number of 0's,  y-number of 1's,  z-number of 2's

Space complexity is:
O(n) ~ O(n)


#################################################
##
## trie.py
##
##
#################################################

###### Design

Trie is a tree of character-Node hashes. To input a word, the tree starts with a root node and then appends child
nodes for each character until it reaches the end of the word. A boolean is given to each node indicating whether
the path along a tree is a word or not. This helps end the tree traversal as we're searching for parts of a word
or its entirety.

The trie is implemented by defining class TrieNode element, which represents the basic storage node in the tree.
The information contained at this node is the character and a dictionary list, as well as a boolean to indicate leaf
status in the tree.

Next is the class Trie, from which will construct a tree of these class TrieNode(s). One information it stores
is a root pointer to the head of the tree. The class Trie includes method functions, such as find() and insert(),
which - as the name implies -  does a basic find node or insert node operation.



###### Time Complexity

Given that a TrieNode has a hash dict(), the class Trie Tree is essentially a nested hash key lookup. For the Trie Traversal,
the hash lookup is generally O(1). Therefore, depending on the size of the word, say size 'm', the path lookup will be O(m).
Worst case, the path lookup could be O(n), if the hash is imperfect and a single path represents the entire word of size 'n'.

Therefore, the time complexity:
O(n)

###### Space Complexity

The space complexity may not be efficient as there will be nodes which will repeat but be placed
in different positions of the tree, depending how the word constructs the path.

However, the space complexity is dependent on the number of letters and the number of words given.
Therefore for each character O(1) space,

O(n) ~  ( O(1)*m + O(1)*m + O(1)*m ... O(1)*m )    , where 'm' number of storage spaces for each character
        |<----- n - times ...  -------------->|
	      
O(n) ~ O(m) * n
     ~ O(m*n)

Because m ~~ is finite roughly 26 to 52 letters +  0-9 numbers (truly depends on what you consider and include
as characters). Some words will overlap because they have the same "prefix", so many of these tree paths can be
retraced several times for different words.



#################################################
##
## http_router_using_tries.py
##
##
#################################################

###### Design

Similar to the word trie implementation, this will also have a O(n) worst case lookup.
The http router parses the URL based on the address and file directories.
It then places each segment into a trie tree.

When it adds the handler, it traces the route of the existing addresses down the trie and add
the handler as a new node. The trie is fundamentally a nested list of dictionaries of class type
TrieNode.

###### Time Complexity

Therefore, the time complexity:
O(n)

###### Space Complexity

The space complexity is similar to the trie algorithm. However, it stores handlers and the paths to those
handlers in a nested dictionary.

The space complexity is:

O(m*n)

Given that many handlers in the world wide web will share similar paths. For example, a company website
will have one base address but individual handlers for linked pages that specialize and inform
specific information, i.e. "about page", "contacts page", "product/services page" , etc.


#################################################
##
## search_rotated_array.py
##
##
#################################################

###### Design

This program searches a rotated array by picking a number at midpoint and then deciding whether to
segment the array right or left halves, depending if the current index is greater or less than the target
It is very similar to binary search except that the search is modified and will account for the rotated
array aspect. What this means is that a portion of the array will be sorted, however, the array
was rotated at a random pivot position. 


###### Time Complexity

The binary array has a O(log n) because at every iteration we are only looking at
half the elements between midpoint and starting. For ever step, we narrow the range in which to search
for target. Suppose we have n elements. We pick a starting point at n/2 (starting from 0 index to n).
From this index, we decide if the current node is > or < the target. We pick a direction and from
n/2 to n (assuming current is less than target), we search over n/2 range and divide that range at
midpoint n + (n-n/2)/2 = n + n/4. If at 3n/4 the target is not found, we then subdivide that range
and recurse through the conditional test.

Out of n = 8, we have three iterations of tests.
Out of n = 4, we have two "            "      "

This shows x = log2 n, where n is the number of elements, and x is the number of iterations
to search in this array.

Therefore, the time complexity is:
O(n) ~ O(log n).


###### Space Complexity
This algorithm is in-place search. Therefore, the space complexity is dependent on the number
of elements in the array.

O(n) ~ O(n)



