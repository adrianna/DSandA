###################################
## P1: lru_cache.py
## 
##     
###################################
from collections import OrderedDict

import pdb

debug = 0

################################
#    5 -> prev 2
#      <- next 2
#    H


class LRU_Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
            

class LRU_Cache:
    def __init__(self, capacity = 5):
        ''' #Initialize LRU_Cache node  '''
        
        self.hmap = dict()
        self.capacity = capacity
        self.num_entries = 0
        self.head = None
        self.tail = None
    
        
    # get(key)    
    def get(self, key):
        
        if self.capacity == 0:
            print("Warning: Can't perform get() operation when LRU capacity is 0")

        # Check for key in hash map
        if self.hmap.get(key) is not None:
            node = self.hmap[key]
            
            # Update tail pointer if item removed is tail node
            if node == self.tail:
                self.tail = node.next
                
            # Move updated node to front of queue    
            self.enQueue(node)
            return node.value

        return -1

    # set(key,value)
    def set(self, key, value):
        
        if self.capacity == 0:
            print("Warning: Can't perform set() operation when LRU capacity is 0")
        
        if debug:
            print("set {}: {}".format(key, value))
            pdb.set_trace()

        # Check if key is in map, update or append new node to the front of the queue
        if self.hmap.get(key) is not None:
            node = self.hmap[key]
            node.value = value
            node.key = key
            # enQueue(node)
        else:
            if debug: print("Checking for entries: {}".format(self.num_entries))            

            # check if LRU is full, remove least used node (tail) from queue
            node = LRU_Node(key, value)
            if self.num_entries == self.capacity:
                self.removeTail()
		
	        # add new node to the head of the list
                #            self.enQueue(node)
            self.hmap[key] = node
        self.enQueue(node)
        
    # removeTail()
    def removeTail(self):

        if debug:
            pdb.set_trace()
            print("removing tail.value: {}".format(self.tail.value))

        # Check if tail node exists, remove node from queue and hash map
        # Update num_entries to reflect number of items in queue
        if self.tail:
            next_node = self.tail.next
            del self.hmap[self.tail.key]
            self.tail = next_node
            self.num_entries -= 1

            if debug: print("removed tail, now at num_etries: {}".format(self.num_entries))

    # enQueue(node)
    def enQueue(self, node):

        if debug:
            pdb.set_trace()
            print("moving node {} up front".format(node.value))

        # Append node to front of the list, and set tail node to head if new node
        # Update num_entries
        if self.head:
            node_tmp = self.head
            self.head = node
            node.prev = node_tmp
            node_tmp.next = node
        else:
            self.head = node
            self.tail = self.head    

        self.num_entries += 1
        if debug: print("Updating num_entries: {}".format(self.num_entries))
	    


################## Main #############################

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

# Test Case #1: Boilerplate 
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's
                         # capacity and 3 was the least recently used entry

# Test Case #2: Warning issued for Zero Capacity LRU
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# returns warning
print(our_cache.get(1))
# should return -1

# Test Case 3 - updating existing key
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# returns 10
print(our_cache.get(2))
# returns 2

