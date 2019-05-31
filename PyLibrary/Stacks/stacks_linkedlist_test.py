class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

        print(new_node.value)
        
    def pop(self):
        
        if self.head is None:
            return -1
        else:
            last_value = self.head.value
            print("Assigning {}".format(last_value))
            self.head = self.head.next
            self.num_elements -= 1
            return last_value

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def sPrint(stack):
    for element in range(stack.size()):
        node = stack.pop()
        print(node)
        
    

stack = Stack()
stack.push(1)
stack.push(3)
stack.push(5)
#stack.push(7)
print("Stack size is: {}".format(stack.size()))

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack size is: {}".format(stack.size()))

#while not stack.is_empty():
#    popped = stack.pop()
#    print(popped)
    

