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
        self.end  = True
      
        
    def insert(self, character):
        ## Add a child node in this Trie

        if self.children.get(character) is None:
            self.children[character] = TrieNode()
            self.chr = character

    def suffixes(self, suffix = '', word = '', words=[]) -> list::
        
        # Base Case
        if suffix:
            self = self.children.get(suffix)
            
        for letter in self.children.keys():
            self.suffixes(letter, word + letter, words)
                
            if sfx not in self.word:
                self.word.append(letter)
                    
            if self.end and word:
                words.append(word)
            
        return words

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    
    def insert(self, word):
        ## Add a word to the Trie

        current_node = self.root
        
        for char in word:
            current_node.children.insert(char)
            current_node = current_node.children[char]
            
        current_node.end = True

        
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        current_node = self.root
        
        if current_node.children.get(char) is None:
            return None
        
        for char in prefix:
            current_node = current_node.children[char]
            
        # current_node will be at the position of the last character in
        # prefix node
        if current_node:
            return current_node.suffixes(current_node.chr)
            
        
    
#MyTrie = Trie()
#wordList = [
#    "ant", "anthology", "antagonist", "antonym", 
#    "fun", "function", "factory", 
#    "trie", "trigger", "trigonometry", "tripod"
#]
#for word in wordList:
#    MyTrie.insert(word)

#from ipywidgets import widgets
#from IPython.display import display
#from ipywidgets import interact
#def f(prefix):
#    if prefix != '':
#        prefixNode = MyTrie.find(prefix)
#        if prefixNode:
#            print('\n'.join(prefixNode.suffixes()))
#        else:
#            print(prefix + " not found")
#    else:
#        print('')
#interact(f,prefix='');



tn = TrieNode()
print("print tn: {}".format(tn))

tn.insert('a')

print("Suffixes for 'a': {}".format(tn.suffixes('a')))
print("inserting X")

#tn.end = False   # Reseatting end boolean, due to insert below

#tn.children['a'].insert('x')
#print("Suffixes for 'a': {}".format(tn.suffixes('a')))

#print("inserting T")
#tn.children['a'].insert('t')

#print("Suffixes for 'a': {}".format(tn.suffixes('a')))
#tn.children['a'].children['t'].end = False
#tn.children['a'].children['t'].insert('e')
#print("Suffixes for 'a': {}".format(tn.suffixes('a')))




















