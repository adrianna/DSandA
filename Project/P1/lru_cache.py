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
        
        if self.hmap.get(key) is not None:
            node = self.hmap[key]
            if node == self.tail:
                self.tail = node.next    # Set tail pointer to more recent node
            self.enQueue(node)
            
            return node.value

        return -1

    # set(key,value)
    def set(self, key, value):

        if debug:
            print("set {}: {}".format(key, value))
            pdb.set_trace()
            
        if self.hmap.get(key) is not None:
            node = self.hmap[key]
            node.value = value
            node.key = key
            enQueue(node)
        else:
            new_node = LRU_Node(key, value)
            if debug: print("Checking for entries: {}".format(self.num_entries))
            if self.num_entries == self.capacity:
		#remove LRU node (tail of linked list)
                self.removeTail()
		
		# adding the new node to the head of the list
            self.enQueue(new_node)
            self.hmap[key] = new_node
	    
    # removeTail()
    def removeTail(self):

        if debug:
            pdb.set_trace()
            print("removing tail.value: {}".format(self.tail.value))

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
#our_cache.set(4, 4);


print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

#if debug:
#    pdb.set_trace()
#    print("pause, before setting new node to 3")
print(our_cache.get(3))  # returns -1 because the cache reached it's
                         # capacity and 3 was the least recently used entry

