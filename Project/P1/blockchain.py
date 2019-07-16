##################################
# P1: blockchain.py
#
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
        self.tail = None     
            
          
    def append(self, timestamp, data, previous_hash):
            
        if self.head is None:
            #print("head is none, instantiate Block()")
            self.head = Block(timestamp, data, previous_hash)
            #self.head._print()
            self.tail = self.head
        else:
            #print("head exists, instantiate new node to  Block()")
            new_node = Block(timestamp, data, previous_hash)
            #new_node._print()
            self.head.prev = new_node
            #self.tail = self.head
            #print("new_node: {}".format(new_node))
            #print("self.head.prev: {}".format(self.head.prev))
            #print("self.tail: {}".format(self.tail))
            #print("before update, self.head: {}".format(self.head))
            self.head = new_node
            #print("after update, self.head: {}".format(self.head))
            

    def print(self, index=0):
        #print("[[print]]")
        if index == 0: 
            if self.tail is not None:
                self.tail._print()
        else:
         #   print("[[Passed arg]] index: {}".format(index))
            node = self.tail
            idx = 0
            while node != None:
                #print("idx: {}".format(idx))
                if idx == index:
                    node._print()
                    return
                node = node.prev
                idx +=1
                #print("increment idx: {}".format(idx))
   

####### Main ############
b1 = BlockChain()
b1.append('0612_1950', "N1", None)
b1.print()
#Printing: timestamp, data, previous_hash, hash_code
#0612_1950
#N1
#None
#b79f477f6d435116155b1121455748240bb5e7c81f7043519980df21a8167ca1


print("***")
b1.append('0612_2042', "N2", "b1")
b1.print(1)
#Printing: timestamp, data, previous_hash, hash_code
#0612_2042
#N2
#b1
#2a5f06422d35ac8977cbf311a3178de243428e2c1ca836ed16477cac024360ec


print("***")
b1.append('0623_2331', "N3", "b2")
b1.print(2)
#Printing: timestamp, data, previous_hash, hash_code
#0623_2331
#N3
#b2

