##################################
# P1: union_and_intersection.py
#
#
##################################

import pdb

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


def convertLList_to_PySet(llist):
    pylist = []

    node = llist.head
    while node:
        pylist.append(node.value)
        node = node.next

    pyset = set(pylist)
    return pyset

    
def union(llist_1, llist_2):

    l1 = convertLList_to_PySet(llist_1)
    l2 = convertLList_to_PySet(llist_2)

    union = l1 | l2

    llist = LinkedList()

    for value in union:
        llist.append(value)
        
    return llist


def intersection(llist_1, llist_2):

    l1 = convertLList_to_PySet(llist_1)
    l2 = convertLList_to_PySet(llist_2)

#    intersection = l1.intersection(l2)
    intersection = l1 & l2

    llist = LinkedList()
    for value in intersection:
        llist.append(value)

    return llist

def printList(llist):
    
    node = llist.head
    while node:
        print(node.value)
        node = node.next
        

############################## Main ###################################

#### Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1,2]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test Case 1")
print("union of l1 and l2")
printList(union(linked_list_1,linked_list_2))

print("intersection of l1 and l2")
printList(intersection(linked_list_1,linked_list_2))

#Union = [1,2,3,4,6,9,11,21,23,65]
#Intersection = [2,3,4,21]



#### Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 2")
print("Union of l1 and l2")
printList(union(linked_list_3,linked_list_4))
print("Intersection of l1 and l2")
printList(intersection(linked_list_3,linked_list_4))




#### Test case 3
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 3")
print("Union of l1 and l2")
printList(union(linked_list_3,linked_list_4))
print("Intersection of l1 and l2")
printList(intersection(linked_list_3,linked_list_4))

#### Test case 4
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 3")
print("Union of l1 and l2")
printList(union(linked_list_3,linked_list_4))
print("Intersection of l1 and l2")
printList(intersection(linked_list_3,linked_list_4))
