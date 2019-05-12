#!/usr/bin/env python
# coding: utf-8

# # Reversing a linked list exercise
# 
# Given a singly linked list, return another linked list that is the reverse of the first.

# In[ ]:


# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


# In[ ]:


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    # TODO: Write your function to reverse linked lists here
    
    pass


# In[ ]:


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

print ("Pass" if (llist == reverse(llist)) else "Fail")


# <span class="graffiti-highlight graffiti-id_o7ebglo-id_s2dtp8f"><i></i><button>Show Solution</button></span>
