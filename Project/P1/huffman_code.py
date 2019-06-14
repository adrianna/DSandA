##################################
# P1: huffman_code.py
#
# Question: I'm torn whether I should implement with
# a) heapq library or create linked list heap structure and the cbtree
# c) create ordered tuple of character frequencies and implement a trie

# Question: What would be the difference of using a heap to create the cbtree
# and using a tuple to create a trie?
#
# WIP (work in progress)
# Feel free to comment
#
##################################


from DataStructures import *
import heapq

class HeapNode:
    def __init__(self, char, frequency):
        self.char = ''
        self.frequency = 0
        self.right = None
        self.left = None

class HuffmanCode:

    
    def createFreqDict(self,string):

        # Create Hash Counter for character frequency
        freq_dict = {}
        for char in string:
            if ' ' not in char:
                if char not in freq_dict.keys():
                    freq_dict[char] = 1
                else:
                    freq_dict[char] += 1
                    
        return freq_dict

    def createHuffTree(self, freq_dict):
        
        huff_tree = heapq()
        for key in freq_dict.keys():
            character_node = HeapNode(key, freq_dict[key])
            heapq.heappush(huff_tree, character_node)

        return huff_tree    
    



def huffman_encoding(data):
    pass




def huffman_decoding(data,tree):
    pass






if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print(a_great_sentence)

    h = HuffmanCode()
    freq_dict = h.createFreqDict(a_great_sentence)
    print(freq_dict)
    print(h.createHuffTree(freq_dict))

#    print (char_frequency(a_great_sentence))
#    cf_list = char_frequency(a_great_sentence)
#    createHuffTree(cf_list)




    #    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#    print ("The content of the data is: {}\n".format(a_great_sentence))

#    encoded_data, tree = huffman_encoding(a_great_sentence)

#    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#    print ("The content of the encoded data is: {}\n".format(encoded_data))

#    decoded_data = huffman_decoding(encoded_data, tree)

#    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#    print ("The content of the encoded data is: {}\n".format(decoded_data))

    
