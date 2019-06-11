from DataStructures import *
import heapq

class HeapNode:
    def __init__(self, char, freq):
        self.char = ''
        self.freq = 0
        self.right = None
        self.left = None

class HuffmanCode:
        
    def char_frequency(string):
        
        # Create Hash Counter for character frequency
        char_freq = {}
        for chr in string:
            if ' ' not in chr:
                if chr not in char_freq.keys():
                    char_freq[chr] = 1
                else:
                    char_freq[chr] += 1
                    
                    # Convert to tuples, whose values are *immutable*
        char_freq_tuple = list()
        for chr, count in char_freq.items():
        char_freq_tuple.append((count, chr))
        
        ## Note: Do we skip spaces?
        ##       Are Character frequency case-sensitive?
        return sorted(char_freq_tuple)

    def createHuffTree(cf_list):
        
        huff_tree = heapq()
        for chr, freq in cf_list:
            print("chr: {}, freq: {}".format(chr, freq))
            
            char_node = HeapNode(chr, freq)
            heapq.heappush(huff_tree, char_node)
            
            
    



def huffman_encoding(data):
    pass




def huffman_decoding(data,tree):
    pass






if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print(a_great_sentence)
    print (char_frequency(a_great_sentence))
    cf_list = char_frequency(a_great_sentence)
    createHuffTree(cf_list)
#    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#    print ("The content of the data is: {}\n".format(a_great_sentence))

#    encoded_data, tree = huffman_encoding(a_great_sentence)

#    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#    print ("The content of the encoded data is: {}\n".format(encoded_data))

#    decoded_data = huffman_decoding(encoded_data, tree)

#    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#    print ("The content of the encoded data is: {}\n".format(decoded_data))

    
