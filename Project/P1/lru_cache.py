###################################
## P1: lru_cache.py
## 
##     
###################################
from collections import OrderedDict

import pdb

debug = 0

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
        self.capacity = 0
        self.num_entries = 0
        self.head = None
        self.tail = None

        
    def get(self, key):
        
        if self.hmap.get(key) is not None:
            return self.hmap[key].value

        return -1

    def set(self, key, value):
       
       if self.hmap.get(key) is not None:
           self.hmap[key].value = value
           self.hmap[key].key = key
       else:
           new_node = LRU_Node(key, value)
           print("Checking for entries: {}".format(self.num_entries))
           if self.num_entries  > self.capacity:
               #remove LRU node (tail of linked list)
               self.removeTail()
               
       # adding the new node to the head of the list
       self.enQueue(new_node)
       self.hmap[key] = new_node
           
           
    def removeTail(self):

        if self.tail:
            print("removing tail.value: {}".format(self.tail.value))
            prev_node = self.tail.prev
            tail = prev_node
            del self.hmap[tail.key]
            self.num_entries -= 1
            print("now at num_etries: {}".format(self.num_entries))

    def enQueue(self, node):
        
        if self.head:
            second_node = self.head
            self.head = node
            node.prev = second_node
            second_one.next = node
        else:
            self.head = node

            
        self.num_entries += 1
           


################## Main #############################

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's
                         # capacity and 3 was the least recently used entry

