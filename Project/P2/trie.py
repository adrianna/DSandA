##
## trie.py
##
## Issue: insert() does not nest the second TrieNode dict into the first TrieNode
##        self.children shows a hash table (basic dictionary), but not a nested dictionary
##


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.end  = False
        
        
    def insert(self, character):
        ## Add a child node in this Trie

        if self.children.get(character) is None:
            self.children[character] = TrieNode()
            #self.chr = character

            
    def suffixes(self, suffix = ''):
        retwords = []
        if self.end:
            if suffix != '':
                retwords.append(suffix)
                
        for letter in self.children.keys():    
            if self.children.get(letter) is not None:
                node = self.children[letter]
                retwords += node.suffixes(suffix+letter)
        return retwords    

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    
    def insert(self, word):
        ## Add a word to the Trie

        current_node = self.root
        
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.end = True

        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        current_node = self.root
        if current_node.children.keys() is None:
            return None
        
        for char in prefix:
            current_node = current_node.children[char]
            
        return current_node
        
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]


#wordList = [
#    "ant", "anthology"
#]


for word in wordList:
    MyTrie.insert(word)

#from ipywidgets import widgets
#from IPython.display import display
#from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(prefixNode.suffixes())
            #print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
#interact(f,prefix='ant');
f('ant')
#['', 'hology', 'agonist', 'onym']

# Test Case 1
#f('a')
#['nt', 'nthology', 'ntagonist', 'ntonym']

#Test Case 2
f('func')
#['tion']

#Test Case 3
#f('tripod')
#[]


















