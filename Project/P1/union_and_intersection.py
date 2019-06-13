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

    print("\t[[union]]: size of l1: {}".format(l1.size()))
    print("\t[[union]]: size of l2: {}".format(l2.size()))
    union_list = None
    
    value_dict = {}
    node_l1 = l1.head
    node_l2 = l2.head

    if l1.size() == l2.size():
        while node_l1:
            element_l1 = node_l1.value
            element_l2 = node_l2.value
            print("element_l1: {}, element_l2: {}".format(element_l1, element_l2))
            if element_l1 not in value_dict.keys():
                value_dict[element_l1] = 1
                union_list = node_l1
                union_list.next = None
            else:
                print("Skipping element_l1: {}".format(element_l1))
                value_dict[element_l1] += 1

            
            if element_l2 not in value_dict.keys():
                value_dict[element_l2] = 1
                union_list = node_l2
            else:
                print("Skipping element_l1: {}".format(element_l1))
                value_dict[element_l2] += 1

            # Advance the node in the list    
            node_l1 = node_l1.next
            node_l2 = node_l2.next
    else:
        print("Skipping union of lists")

        
    return 

        

def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


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
print (union(linked_list_1,linked_list_2))
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

print("Test Case 2")
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

