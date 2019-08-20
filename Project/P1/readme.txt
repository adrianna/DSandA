##
## Readme.txt - P1 Problems


#################################################
##
## lru_cache.py
##
##
#################################################

###### Design
This program updates the cache with value. It uses a hash key to store
the array list. To get O(1) operation on the add or remove, the array
is a doubly linked list.


###### Time Complexity
The time complexity is O(1) operation to add or remove a value from the
lru_cache.

Worst case, time complexity: O(n) since it will have to traverse the list to
remove the least used memory value.

Time Complexity: O(n) (for worse case)

###### Space Complexity
The LRU cache store n-elements per key. Given m-keys. The storage is m*n
elements, which totals O(n). Since the least used value is always removed and
replaced by a new value, the number of elements stays constant.

Space complexity: O(n) 


#################################################
##
## find_directory.py
##
##
#################################################


###### Design
This program asks to find a directory within a tree and return true, if found. False, otherwise.
The algorithm is to test each item for 'ls -l' status. If it is a directory, it must descend into
that directory and recurse on this path, again, checking for file, directory or *.c program.


###### Time Complexity
The time complexity can be computed by the number of branches it needs to traverse. The algorithm
cannot make assumptions or guesses on which subdirectory will have the *.c programs. Therefore,
given m-subdirectories with n programs, it will test m+n items for either a file, a *.c program or
a directory. The conditional test for 'ls -l' status is O(1), but the total number of conditional
tests would be:

(m+n)*O(1) ~ O(m+n), where m - number of subdirectories, n - number of files

Hence, O(n) ~ O(m+n)
            ~ O(n) 

Time complexity: O(n)

###### Space Complexity
The space complexity is the list of directories, housing the *.c programs. Therefore, it is simply
a list of O(n) space.

Space complexity: O(n)



#################################################
##
## huffman_code.py
##
##
#################################################

###### Design
The huffman code takes a string and converts it into a binary code based on the frequency of each
character. To this, the algorithm has HeapNode() class construct to store the character value
and its respective frequency. Another construct, called class HuffmanCode() creates the
heap tree to store the HeapNode according to frequency weights. It first assigns all
individual characters with its respective frequency weight into a priority Queue. Then,
it merges the HeapNodes, taking two at a time and building the Huffman Tree, which is
essentially a binary tree of nodes. After the tree is completed, the huffman code and decoding
functions can tranverse the tree and perform the compression and decompression of a
given text string.


###### Time Complexity
Construction the frequency dictionary take O(n).

Constructing the heap tree takes O(n). To compress, it is literally traversing the tree and
encoding the text into binary code. Tree traversal for a binary tree is O(nlogn).

Deconstructing the code involves parsing out the coded text which O(n) for each character. However, the lookup
for the code in the decodes_dict() takes O(1).

Breakdown
O(nlogn) for tree traversal
O(n) for dictionary creation: character frequency, code and decode lookups
O(1) for lookup
------------------

O(n) + O(nlogn) + O(1)
O(n)

Time Complexity: O(n)
     		      


###### Space Complexity
Breakdown
 O(n) for character frequency lookup, including spaces
 O(n*k) for code and decode, where k = number of bits to represent the text character
 O(n) for binary tree to encapsulate all the characters in the text.
------------
O(n) + O(n*k) + O(n)

Space Complexity: O(n)


#################################################
##
## active_directory.py
##
##
#################################################


###### Design
This program asks if a user is part of a group and returns a boolean, indicating true if user is in group,
and false otherwise. The program creates tree whose parent includes child nodes. The child node may under
another parent node.

###### Time Complexity
Breakdown
O(1) -         Constructing the graph user by user, which is just appending to the list
O(1) -	       Getting or retrieving group/user list information will take anywhere between
               best case lookup of only one retrieval in the list, or O(n) going to the last
	       item of the list. 
O(1) to O(n) - Querying if user is in group list may be constant time retrieval - depending if it's
     	       the only user in the group or user list. However, if it's not found in its most
	       immediate group, it will check all the other groups' group lists, which the number of groups
	       can vary. Worst case, it will check all groups to find user in that list.
----------
O(n) + O(1) + O(1)



Time Complexity: O(n) 


###### Space Complexity
The class Group object has two lists: groups and users and just a variable to store the
user's name. The list can vary by size n items.

O(n) for users
O(n) for groups
----------------
O(n) + O(n)

Some users may overlap in several groups, so the total isn't 2*n. However,
O(n) + O(n) ~ 2*O(n) ~ O(n)

Space Complexity: O(n)


#################################################
##
## blockchain.py
##
##
#################################################

###### Design
This program implements single linked list but with the head pointing to the
most recent added Block Node. The tail points to the oldest Block Node.

To append, we add to the head node in O(1). When we want to print the node
to a particular index, we traverse the BlockChain starting at the tail. This
take O(n) to get to the nth node

###### Time Complexity
For the individual methods, the time complexity will differ. Here is the summary for each
method:
Block::calc_hash - O(1)	  // This is because it just takes one item and does a mathematical
	    		     conversion of the input.
Block::_print()  - O(1)   // This is constant time for each item
Block::__init__  - O(1)   // This is constant time for each item


BlockChain::__init__ - O(1)  // This is constant time for each item
BlockChain::append   - O(n)  // For worse case, it will have to traverse n-items to place the
                                last node on the chain
		     - O(1)  // For best case, if no node exists, it is a one-time operation to
		       	     	create the node
BlockChain::print    - O(n)  // For worse case, it will have to traverse n-items to place the
                                last node on the chain
		     - O(1)  // For best case, if no node exists, it is a one-time operation to
		       	     	create the node
				
###### Space Complexity
For n-nodes in the BlockChain,

Space complexity: O(n) 


#################################################
##
## unions_and_intersections.py
##
##
#################################################

###### Design

The program performs union and intersection computation according to set theory.
Given two linked lists, the union() function will return the total *unique*
elements in the two lists. The intersection() function returns the *common*
elements in the two lists. These functions are bundled in the unions_and_intersectons python script.

The design is to use linked lists. A class linkedlistNode is created to contain
the value. The class linkedList creates a link of these basic nodes of N-size.
To do the calculation, convert the linked lists to python lists []. Then, type-cast to sets and perform
the python set operations: union and intersection.

Convert the results back into a linked list.

###### Time Complexity
The time complexity to compute the set operations is converting the m-elements
of one list to sets and the other n-elements list to another [set].
This conversion will take O(m+n) ~ O(n). Then, one converts the list[] into a set,
which under the hood, the conversion takes O(n) because it cycles through
all the n-elements.

For the set operations, finding the union() of the two lists is simple use of set
operation in python. Likewise, for the intersection of the two lists uses the set
operation in python.

For union(), O(n) ~ O(m) + O(n) ~ O(m+n) ~ O(n'), where n'~ m+n as we traverse
the two lists and eliminate any duplicates for the return list.

For intersection(), the operation is the same O(n), applying the same logic.
This operation will take what's common from both lists, which results in
smaller 'sub-setted' list.

Time Complexity: O(n)

###### Space Complexity
The Space Complexity is similiar in logic to the time complexity.

When converting the list, we're making a copy of the total elements,
n' = m+n, therefore, O(n')
When returning union(), this will still be O(n''), n'' = n' minus duplicates
When return intersection(), this will be O(n'''), n''' < n''' unique elements
and n''' < n'

Therefore, total space complexity:
O(n) + O(m) : Original lists
O(n'): Set conversion
O(n''): union
O(n''') intersection
-----------------------
O(n)
n~ n+m+n'+n''+n''' ~ n

Space Complexity: O(n)
