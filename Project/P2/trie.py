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
        self.chr = '0000'
        self.sfx = ''
        self.word = []
        
    def insert(self, character):
        ## Add a child node in this Trie

        if character in self.children.keys():
            for chr_key in self.children.keys():
                print("\t[[insert]] for each chr_key: {}".format(chr_key))
               # node = self.children[chr_key] 
                if chr_key == character:
                    node = self.children[chr_key]
                    print("\t\t[[insert]] Updating self.end: {}, not self.chr: {}".format(self.end, self.chr))
                    node.children[character] = TrieNode()
                    print("\t\t[[insert]] inserted character {} at node.children {}".format(character, node.children))
                    node = node.children[character]
                    node.chr = character
                    node.end = False
                    print("\t\t**** [[insert]] PAUSE**** ")
        else:
            self.children[character] = TrieNode()
            self.chr = character
            #self.end = False
               
    def suffixes(self, suffix = ''):
        
        # Base Case
        if suffix is None:
            return []

        
        if self.end:
            print("\t\t[[suffixes]]: self.end: {} for self.chr: {}".format(self.end, self.chr))
            self = self.children[suffix]
            for letter in self.children.keys():
                
                sfx = self.suffixes(letter)
                
                if sfx not in self.word:
                    self.word.append(letter)
                    
            return self.word
            
        else:
            
            if len(self.children.keys())== 0:
                   return self.chr
                   
        return []

        
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
            
        current_node.end = True
    
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
print("print tn: {}".format(tn))

tn.insert('a')

#print("Suffixes for 'a': {}".format(tn.suffixes('a')))
#print("inserting X")

tn.end = False   # Reseatting end boolean, due to insert below

#tn.children['a'].insert('x')
#print("Suffixes for 'a': {}".format(tn.suffixes('a')))

print("inserting T")
tn.children['a'].insert('t')

#print("Suffixes for 'a': {}".format(tn.suffixes('a')))
tn.children['a'].children['t'].end = False
tn.children['a'].children['t'].insert('e')
print("Suffixes for 'a': {}".format(tn.suffixes('a')))





















#print("tn.children[a].end: {} and chr: {}".format(tn.end, tn.chr))
#print("tn.children: {}".format(tn.children))
#print("tn.children['a']: {}".format(tn.children['a']))
#print("tn.children['a'].chr: {}".format(tn.children['a'].chr))
#print(tn.suffixes('a'))


#print("inserting E")
#tn.children['a'].children['x'].insert('e')
#if tn.suffixes('a') is not NONE: print(tn.suffixes('a'))
#print("PAUSE")
#tn = TrieNode()
#tn.insert('a')
#print("current TN.chr: {} ".format(tn.chr))
#print("*** PAUSE ***")
#print()      
#tp = tn
#tp.insert('b')
#print("current TP.chr: {} ".format(tp.chr))
#print("current TP.children: {} ".format(tp.children))
#print("\n")
#print("**** TN post-TP insert ***")
#print("current TN.children: {} ".format(tn.children))
#tr = tp
#tr.insert('b')
#print("current TR.chr: {} ".format(tr.chr))
#print("current TR.children: {} ".format(tr.children))
#print("current TR.children['b'].children['b'].chr: {} ".format(tr.children['b'].children['b'].chr))
#print("\n")
#tr.insert('a')


#tn.insert('c')
#tn.printNode()

#print(tn.end)
#print(tn.children['a'])
#print(tn.children['a'].end)
#print(tn.children['a'].children)
#print(tn.children['a'].insert('b'))
#print(tn.children['a'].end)
#print(tn.children['a'].children['b'])
#print(tn.children['a'].children['b'].end)
#print(tn.children['a'].children['b'].children)
#print(tn.children['a'].children['b'].insert('c'))
#print(tn.children['a'].children['b'].end)
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

