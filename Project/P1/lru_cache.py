##################################
# P1: lru_cache.py
#
# # WIP (work in progress)
# # Compile time error: LRU_Cache object has no attribute 'set'
# #Feel free to comment
#
##################################


class LRU_Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
            

class LRU_Cache(object):

    def __init__(self, capacity = 5):
        ''' #Initialize LRU_Cache node  '''
        self.bucket_array = [ None for _ in range(capacity) ]
        self.capacity = 0
        self.num_entries = 0
        self.p = 31
        self.head = None
        self.tail = None

    def get(self, key):
        '''# Retrieve item from provided key. Return -1 if nonexistent.'''
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                head.capacity += 1
                return head.value
            
            head = head.next
        return -1
            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        bucket_index = self.get_hash_code(key)
        new_node = LRU_Node(key,value)

        head = self.bucket_array[bucket_index]
        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1         
            
    def remove_node(self, key):
        bucket_index = self.get_hash_code(key)
        
        # Oldest node is assumed to be at the head, linked lists are FILO
        # FILO = first in/last out
        head = bucket_array[bucket_index]
        if head is not None:
            temp = head.next
            self.bucket_array[bucket_index] = temp
            head = self.bucket_array[bucket_index]
        

    def get_hash_code(self, key):
        key = str(key)
        print("key: {}".format(key))

        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets            # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets               

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def size(self):
        return 
    
our_cache = LRU_Cache(5)

print(our_cache.get_hash_code(1))
print(our_cache.get_hash_code(2))
print(our_cache.get_hash_code(3))
print(our_cache.get_hash_code(4))
print(our_cache.get_hash_code(5))
print(our_cache.get_hash_code(6))

#our_cache.set(1, 1)
#our_cache.set(2, 2)
#our_cache.get(1)       # returns 1
#our_cache.get(2)       # returns 2
#our_cache.get(3)       # return -1
