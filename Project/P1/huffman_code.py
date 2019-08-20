##################################
# P1: huffman_code.py
#
##################################


from DataStructures import *
import heapq as h
import pdb
import sys

class HeapNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.right = None
        self.left = None
        
    def __lt__(self, other):
        return self.frequency < other.frequency
        
    #    def __str__(self):
    #        return str("{} : {}".format(self.char, self.frequency))
    
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.char)+"\n"
        #for child in self.right:
        #    ret += child.__str__(level+1)
        #level = 0    
        #for left in self.left:
        #    ret += child.__str__(level+1)

            
        return ret

    def __repr__(self):
        #        return '<tree node representation>'
        return self.frequency
    
        
class HuffmanCode:
    def __init__(self, text):
        self.text = text
        self.huff_tree = []
        self.codes = dict()
        self.decodes = dict()
        
    
    def createFrequencyDict(self):

        # Create Hash Counter for character frequency
        freq_dict = dict()
        for char in self.text:
            #            if ' ' not in char:
            if char not in freq_dict.keys():
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
                    
        return freq_dict

    def createTree(self, freq_dict):

        #        pdb.set_trace()
        for char in freq_dict.keys():
            char_node = HeapNode(char, freq_dict[char])
            h.heappush(self.huff_tree, char_node)

        # merging nodes in Heap    
        while len(self.huff_tree) > 1:
            node1 = h.heappop(self.huff_tree)
            node2 = h.heappop(self.huff_tree)

            # Creating new node with "empty" character value, but combining frequency weights
            # Set pointer to child nodes, left child < right child
            merged_node = HeapNode(None, node1.frequency + node2.frequency)
            merged_node.left = node1
            merged_node.right = node2

            # Push merged_node back into the heap
            h.heappush(self.huff_tree, merged_node)



    def createCodeDict_helper(self, root, current_code):
        if root == None:
            return
        
        if root.char != None:
            self.codes[root.char] = current_code
            self.decodes[current_code] = root.char
            return
        
        self.createCodeDict_helper(root.left, current_code + "0")
        self.createCodeDict_helper(root.right, current_code + "1")
        
        
    def createCodeDict(self):
        root = h.heappop(self.huff_tree)
        current_code = ""
        self.createCodeDict_helper(root, current_code)


    def encodeText(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text


    def decodeText(self, encoded_text):
        
        current_code = ""
        decoded_text = ""
        
        for bit in encoded_text:
            current_code += bit
            if(current_code in self.decodes):
                character = self.decodes[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text

    
    def printTree(self):

        for node in self.huff_tree:
            print(node)
#            print("char: {}, frequency: {}".format(node.char, node.frequency))
        
        

############ Main Routines: Huffman encode/decode ###############

def huffman_encoding(data):
    # Traverse the tree and create the code
    
    hcode = HuffmanCode(data)
    frequency_dict = hcode.createFrequencyDict()
    hcode.createTree(frequency_dict)
    hcode.createCodeDict()

    huff_code = hcode.encodeText(data)

    return huff_code, hcode


def huffman_decoding(data,tree):
    # Traverse the tree in prefix order to decode    

    text = tree.decodeText(data)
    
    return text


################## Main ###########################################

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



    


    
