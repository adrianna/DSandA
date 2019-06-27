## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word  = False

        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children.keys():
            self.children[char] = TrieNode()
            self.is_word = True
            print("insert: {}".format(self.children[char]))
            
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        print(self.children)
        if len(suffix) == 0:
            return None

        if self.is_word:

            print("[[suffixes]] For char {}, is_word: {}".format(suffix, self.is_word))
            if suffix not in self.children:

                for char in suffix:
                    print("char: {} not found in self.children".format(char))
                    print(char)
                    self.children[char]
#                    return self.suffixes(self.children[char])
            else:
                print("suffix: {} found in self.children".format(suffix))
                return None    
        else:
            print("traversing... now at char: {}".format(char))
            return None        
            
    def print(self):
        print(self.children)
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        pass
    
    def insert(self, word):
        ## Add a word to the Trie
        pass
    
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
print(tn.is_word)
print(tn.children['a'])
print(tn.children['a'].is_word)
print(tn.children['a'].children)
print(tn.children['a'].insert('b'))
print(tn.children['a'].is_word)
print(tn.children['a'].children['b'])
print(tn.children['a'].children['b'].is_word)
print(tn.children['a'].children['b'].children)
print(tn.children['a'].children['b'].insert('c'))
print(tn.children['a'].children['b'].is_word)
print("recursing*****")
print(tn.suffixes('a'))
print("recursing TWO *****")
print(tn.suffixes('b'))

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

