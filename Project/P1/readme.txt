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


###### Space Complexity



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


###### Time Complexity


###### Space Complexity



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



###### Space Complexity



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
To do the calculation, convert the linked lists to python lists []. Then, type-cast to sets and perform the python set operations: union and intersection.

Convert the results back into a linked list.

###### Time Complexity
The time complexity to compute the set operations is converting the m-elements
of one list to sets and the other n-elements list to another [set].
This conversion will take O(m+n) ~ O(n). To convert back from list to 

###### Space Complexity
