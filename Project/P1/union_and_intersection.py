##################################
# P1: union_and_intersection.py
#
# This union() function is working, needs minor cleanup. The intersection()
# function is not working.
#
# I have another simpler implementation in mind, but I wonder if
# my current potential solution may work
#
#
##################################

def printDict(type, common_dict):

    print("printing dictionary {}".format(type))
    for key in common_dict.keys():
        print("{}val_dict[{}]: {}".format(type, key, common_dict[key]))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        self.size += 1
        
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size



def convertLList_to_PyList(llist):

    pylist = []

    node = llist.head
    
    while node.next:
        pylist.append(node.value)
        node = node.next
        
    return pylist



        
    
def union(llist_1, llist_2):

    l1 = convertLList_to_PyList(llist_1)
    l2 = convertLList_to_PyList(llist_2)

    pylist = l1 + l2
    union_set = set(pylist)

    union_list = set(union_set)

    llist = None
    for value in range(len(union_list)):
        llist = Node(value)
        llist = llist.next
        
    return llist


def intersection(llist_1, llist_2):

    l1 = llist_1
    l2 = llist_2

    intersection_list = []


    return intersection_list

    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1,2]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test Case 1")
#print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#print("Test Case 2")
#print (union(linked_list_3,linked_list_4))
#print (intersection(linked_list_3,linked_list_4))

