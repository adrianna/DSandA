#!/usr/bin/env python
# coding: utf-8

# # Build a queue using a linked list
# 
# By now, you may be noticing a pattern. Earlier, we had you implement a stack using an array and a linked list. Here, we're doing the
# same thing with queues: In the previous notebook, you implemented a queue using an array, and in this notebook we'll implement one using
# a linked list.
# 
# It's good to try implementing the same data structures in multiple ways. This helps you to better understand the abstract concepts behind
# the data structure, separate from the details of their implementation—and it also helps you develop a habit of comparing pros and cons of
# different implementations.
# 
# With both stack and queues, we saw that trying to use arrays introduced some concerns regarding the time complexity, particularly when
# the initial array size isn't large enough and we need to expand the array in order to add more items.
# 
# With our stack implementation, we saw that linked lists provided a way around this issue—and exactly the same thing is true with queues.

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
        


#### Tests
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")


# ## Time Complexity
# 
# So what's the time complexity of adding or removing things from our queue here?
# 
# Well, when we use `enqueue`, we simply create a new node and add it to the tail of the list. And when we `dequeue` an item,
# we simply get the value from the head of the list and then shift the `head` variable so that it refers to the next node over.
# 
# Both of these operations happen in constant time—that is, they have a time-complexity of O(1).


####################################################################################
# Notes:
#
# 1. For dequeue, check if queue is_Empty(). Return None, if true. Else,
# 2. Pop and store the value at the head node.
# 3. Advance head node to head.next
# 4. Decrement size counter and return stored value
#
