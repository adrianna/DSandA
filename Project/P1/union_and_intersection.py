##################################
# P1: union_and_intersection.py
#
# This union() function is working, needs minor cleanup. The intersection()
# function is
# WIP (work in progress)
# Feel free to comment
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

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    l1 = llist_1
    l2 = llist_2

    union_list = []

    l1_size = l1.size()
    l2_size = l2.size()
    max_size = max(l1_size, l2_size)
    
    value_dict = {}
    node_l1 = l1.head
    node_l2 = l2.head

    for idx in range(max_size):

        if node_l1:
            element_l1 = node_l1.value

            if idx <= l1.size():
                if element_l1 not in value_dict.keys():
                    value_dict[element_l1] = 1
                    union_list.append(node_l1)
                else:
                    value_dict[element_l1] += 1
                
                node_l1 = node_l1.next
                
        if node_l2:
            element_l2 = node_l2.value

            if idx <= l2.size():
                if element_l2 not in value_dict.keys():
                    value_dict[element_l2] = 1
                    union_list.append(node_l2)
                else:
                    value_dict[element_l2] += 1
                    
                node_l2 = node_l2.next                
                    
        idx += 1
                    
    return union_list


def intersection(llist_1, llist_2):

    l1 = llist_1
    l2 = llist_2

    intersection_list = []

    max_size = max(l1.size(), l2.size())
    
    l1val_dict = {}
    l2val_dict = {}
    
    node_l1 = l1.head
    node_l2 = l2.head

    for idx in range(max_size):

        if node_l1:
            element_l1 = node_l1.value
            print("e1: {}".format(element_l1))
            
        if node_l2:
            element_l2 = node_l2.value
            print("e2: {}".format(element_l2))

        print("idx: {}, l1.size: {}, l2.size: {}".format(idx, l1.size(), l2.size()))
        if idx <= l1.size():

            print("l1 eval")
            # always check if element_l1 is in l1val dictionary; assign or
            # increment dictionary element depending on its existence
            if element_l1 not in l1val_dict.keys():
                print("\te1 not in l1val_dict, set element in dictionary")
                l1val_dict[element_l1] = 1

            else:
                print("\te1  in l1val_dict, increment count")
                l1val_dict[element_l1] += 1
                
            # Both elements in the lists match:
            if element_l1 == element_l2:

                print("\te1 = e2")
                #  check if element_l1 is in l2val dictionary, assign element 
                if element_l1 not in l2val_dict.keys():

                    #  append node_l1 to the intersection list, since elements match    
                    intersection_list.append(node_l1)

                    print("\tprinting intersection list")
                    print(intersection_list)
                
            else:
                # elements don't match

                print("\te1 != e2")
                # check if element_l1 is in the other list (l2) l2val dictionary 
                if element_l1 in l2val_dict.keys():
                    
                    # therefore it is a common element, append to intersection list
                    intersection_list.append(node_l1)

                    print("printing intersection list")
                    print(intersection_list)
                    
            # increment node_n1 to the next element            
            if node_l1: node_l1 = node_l1.next

            printDict("\tl1", l1val_dict)
            
        if idx <= l2.size():

            print("l2 eval")
            # always check if element_l1 is in l1val dictionary; assign or
            # increment dictionary element depending on its existence
            if element_l2 not in l2val_dict.keys():
                print("\te2 not in l2val_dict?, assign count 1")
                l2val_dict[element_l2] = 1
            else:
                print("\te2 in l2val_dict? now increment counter")
                l2val_dict[element_l2] += 1
                

            # Both elements in the lists match:                
            if element_l2 == element_l1:
                
                print("\te1 = e2")
                # check if element_l2 is in l1val dictionary, assign element
                if element_l2 not in l1val_dict.keys():
                    
                    # append node_l1 to the intersection list, since elements match                        
                    intersection_list.append(node_l2)
                    
                    print("\tprinting intersection list")
                    print(intersection_list)
                
            else:
                # elements don't match
                print("\te1 != e2")

                # check if element_l2 is in the other list (l1) l1val dictionary
                if element_l2 in l1val_dict.keys():

                    # therefore it is a common element, append to intersection list
                    intersection_list.append(node_l2)

                    print("\tprinting intersection list")
                    print(intersection_list)    
                        
            if node_l2: node_l2 = node_l2.next                

            printDict("\tl2", l2val_dict)
        idx += 1

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

