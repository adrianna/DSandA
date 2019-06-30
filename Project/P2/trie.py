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
        self.is_word  = False
        self.chr = ''              # Do I need to keep the value of the character?
        
    def insert(self, character):
        ## Add a child node in this Trie
        print("\t[[insert]]: character = {}".format(character))
        print("\t[[insert]]: current node at self.chr: {}".format(self.chr))

        if character in self.children.keys():
            for chr_key in self.children.keys():
                print("\t[[insert]] for each chr_key: {}".format(chr_key))
                node = self.children[chr_key] 
                if chr_key == character:
                    print("\t\t[[insert]] when chr_key: {} equals character: {}".format(chr_key, character))
                    node.children[character] = TrieNode()
                    print("\t\t[[insert]] inserted character {} at node.children {}".format(character, node.children))
                    node = node.children[character]
                    node.chr = character
                    node.is_word = True
                    print("\t\t**** [[insert]] PAUSE**** ")
        else:
            self.children[character] = TrieNode()
            self.is_word = True
            self.chr = character
       
               
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
print("current TN.chr: {} ".format(tn.chr))
print("*** PAUSE ***")
print()      
tp = tn
tp.insert('b')
print("current TP.chr: {} ".format(tp.chr))
print("current TP.children: {} ".format(tp.children))
print("\n")
print("**** TN post-TP insert ***")
print("current TN.children: {} ".format(tn.children))
tr = tp
tr.insert('b')
print("current TR.chr: {} ".format(tr.chr))
print("current TR.children: {} ".format(tr.children))
print("current TR.children['b'].children['b'].chr: {} ".format(tr.children['b'].children['b'].chr))
print("\n")
#tr.insert('a')


#tn.insert('c')
#tn.printNode()

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

