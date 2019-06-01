class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.access_cnt = 0
        self.next = None
            

class LRU_Cache(object):

    def __init__(self, capacity):
        ''' #Initialize LRU_Cache node  '''
        self.p = 100
        self.bucket_array = [ None for _ in range(capacity) ]
        self.capacity = 0
        self.access = 0
        
        return None
    

    def get(self, key):
        '''# Retrieve item from provided key. Return -1 if nonexistent.'''
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                head.capacity += 1
                head.access -= 1
                return head.value
            head = head.next
        return -1
            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        bucket_index = self.get_hash_code(key)
        newNode = LinkedListNode(key,value)

        # if key exists, traverse bucket until key is found and return value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
                
            
#        if self.capacity == capacity
        self.remove_node(key)

        # Add node regardless if removal took place
        self.bucket_array[bucket_index] = newNode

                                         
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
        #        hash_code = ord(key[0])*self.p + ord(key[1])
        #        hash_code = 0
        #return hash_code
        return
        

        

        
    
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
