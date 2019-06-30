## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word  = False
        self.chr = ''              # Do I need to keep the value of the character?
        
    def insert(self, char):
        ## Add a child node in this Trie
        for char in self.children.keys():
            
            if char not in self.children.keys():
                self.children[char] = TrieNode()
                self.is_word = True
                self.chr = char
            self.children = self.children[char]
            print("inserted: {}".format(self.children[char]))
        self.chr = char
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        if self.children[suffix].is_word:
            return self.children[suffix].chr
        else:
            self.children = self.children[suffix]
            return suffixes(self.children.chr)
            
        return None

    
    def printNode(self):
        if len(self.children) == 0:
            print("chr: {}".format(self.chr))
            return 
        else:
            for chr in self.children.keys():
                self.children = self.children[chr]
                self.children.printNode()
                
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    
    def insert(self, word):
        ## Add a word to the Trie

        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            
        current_node.is_word = True
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        pass
        
        
    
#MyTrie = Trie()
#wordList = [
#    "ant", "anthology", "antagonist", "antonym", 
#    "fun", "function", "factory", 
#    "trie", "trigger", "trigonometry", "tripod"
#]
#for word in wordList:
#    MyTrie.insert(word)

tn = TrieNode()
tn.insert('a')
tn.insert('b')
tn.insert('c')
tn.printNode()

#print(tn.is_word)
#print(tn.children['a'])
#print(tn.children['a'].is_word)
#print(tn.children['a'].children)
#print(tn.children['a'].insert('b'))
#print(tn.children['a'].is_word)
#print(tn.children['a'].children['b'])
#print(tn.children['a'].children['b'].is_word)
#print(tn.children['a'].children['b'].children)
#print(tn.children['a'].children['b'].insert('c'))
#print(tn.children['a'].children['b'].is_word)
#print("recursing*****")
#print(tn.suffixes('a'))
#print("recursing TWO *****")
#print(tn.suffixes('b'))

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

