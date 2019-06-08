#!/usr/bin/env python
# coding: utf-8

# # Building a Red-Black Tree

class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
        
    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')
        
    def __iter__(self):
        yield from self.root.__iter__()
        
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):    
        # Case 1
        if node.parent == None:
            return
        
        # Case 2
        if node.parent.color == 'black':
            return
        
        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        
        gp = grandparent(node)        
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp == None:
            return
        
        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p


# ### Testing
# 
# We've written a lot of code. Let's see how the tree mutates as we add nodes.
# 
# First, we'll need a way to visualize the tree. The below will nest, but remember the first child is
# always the left child.

def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


# For cases 1 and 2, we can insert the first few nodes and see the tree behaves the same as a BST.

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)


# Inserting 13 should flip 6 and 19 to black, as it hits our Case 3 logic.

tree.insert(13)
print_tree(tree.root)


# Observe that 13 was inserted as red, and then because of Case 3, 6 and 19 flipped to black. 9 was also
# assigned red, but that was not a net change. Because we're not enforcing the optional "root is
# always black rule", this is acceptable.
# 
# Now let's cause some rotations. When we insert 16, it goes under 13, but 13 does not have a red sibling.
# 16 rotates into 13's spot, because it's currently an _inside_ sub-tree. Then 16 rotates into 19's spot. After
# these rotations, the ordering of the BST has been preserved _and_ our tree is balanced.

tree.insert(16)
print_tree(tree.root)


# # 👏👏👏👏👏
# 
# You've done it! Go ahead and pat yourself on the back! This is a complex use of a data structure that has significant power.
# It uses _O(n)_ space and insertions and search perform in _O(log n)_ time.

# ## Further Exercises
# 
# To continue exploring our red-black tree implementation, you might try the following.
# * Observe that our current implementation will add duplicates of the same value. Is that desirable? How would you expect
#   that to behave? Change the implementation to mark how many times the same value has been inserted.
# * Implement search and see how it remains logarithmic for large data sets
# * Tinker with the rotations and early escapes to see how they break (use `print_tree`)
# * Consider adding deletion or sketching out how it should work

