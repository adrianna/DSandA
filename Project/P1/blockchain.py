##################################
# P1: blockchain.py
#
# WIP (work in progress)
# Feel free to comment
# Also run-time error: b2.append(b1)
#
##################################


import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.prev = None
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)

    def calc_hash(self, string):
      sha = hashlib.sha256()

      self.string = string
      hash_str = self.string.encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()
  

    def _print(self):
      print("Printing: timestamp, data, previous_hash, hash_code")
      print(self.timestamp)
      print(self.data)
      print(self.previous_hash)
      print(self.hash)

class BlockChain:

    def __init__(self):
        self.head = None
            
            
          
    def append(self, timestamp, data, previous_hash):
            
        if self.head is None:
            self.head = Block(timestamp, data, previous_hash)
        else:
            new_node = Block(timestamp, data, previous_hash)
            new_node.prev = self.head
            self.head = new_node
                  
            return self.head

    def print(self, index=0):
        if index == 0: 
            self.head._print()
        else:
            node = self.head
            idx = 0
            while node != None:
                if idx == index:
                    node.print()
                node = node.next
                idx +=1
   

####### Main ############
b1 = BlockChain()
b1.append('0612_1950', "N1", None)
b1.print()
b1.append('0612_2042', "N2", None)
b1.print(1)

#print("appending b2 to b1")
#b2.append(b1.timestamp, b1.data, b1.previous_hash)





#Finally you need to link all of this together in a block chain, which you will
#be doing by implementing it in a linked list. All of this will help you build
#up to a simple but full blockchain implementation!
