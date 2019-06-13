############################################
### Doubly Linked List
############################################

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head

            return
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        return

    #   if self.head is None:
    #       self.head = DoubleNode(value)
    #       self.head.previous = self.head
    #       return
    #  else:
    #       node = self.head
    #       while node.next:
    #           node = node.next
    #       node.next = DoubleNode(value)
    #       node.next.prev = node
    #       node = node.next
    #    return
        








