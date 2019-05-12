"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def isEmpty(call_item):
    return not bool(call_item)

def hashInstantiate(key_entry, data_hash):
    if isEmpty(data_hash):
        data_hash[key_entry] = 1
    elif (key_entry not in data_hash):
        data_hash[key_entry] = 1
    else:
        data_hash[key_entry] += 1
    return data_hash


def createHash(call_log, text_log):
    
    max_lines = numTexts = len(text_log)
    numCalls = len(call_log)
    if numCalls > numTexts:
         max_lines = numCalls
         
    calls_out = {}
    texts_out = {}
    calls_in = {}
    texts_in = {}
    known_telemarketers = []
    
 #   print("createHash")
    for line_item in range(max_lines):
        if (line_item <= numTexts):
            text_outgoing, text_incoming = text_log[line_item][0], text_log[line_item][1]
 #           print("{}, {} ".format(text_outgoing, text_incoming))
            texts_out.update(hashInstantiate(text_outgoing, texts_out))
            texts_in.update(hashInstantiate(text_incoming, texts_in))

        if (line_item <= numCalls):
            call_outgoing, call_incoming = call_log[line_item][0], call_log[line_item][1]
  #          print("{}, {} ".format(call_outgoing, call_incoming))
            if call_outgoing.startswith("140"):
                known_telemarketers.append(call_outgoing)
            else:
                calls_out.update(hashInstantiate(call_outgoing, calls_out))
            calls_in.update(hashInstantiate(call_incoming, calls_in))


    potential_telemarketers = []
    telemarketers_match = True
 #   print("Before, {}" .format(telemarketers_match))
    for key_item in calls_out.keys():
#        print("key_item: {} ".format(key_item))
        telemarketers_match = texts_out.get(key_item) == None and texts_in.get(key_item) == None and calls_in.get(key_item) == None
#        print("After, {}" .format(telemarketers_match))
#        print("texts_out.get( {} ): {}".format(key_item, texts_out.get(key_item)))
#        print("texts_in.get( {} ): {}".format(key_item, texts_in.get(key_item)))
#        print("calls_in.get( {} ): {}".format(key_item, calls_in.get(key_item)))
#        print("###")  
        if telemarketers_match: 
            potential_telemarketers.append(key_item)
            
#    print(potential_telemarketers)        

#    print("###")

#    print("KNOWN_TELEMARKETERS")
#    print(known_telemarketers)
#    print("CALLS_OUT")
#    print(calls_out)
#    print("CALLS_IN")
#    print(calls_in)
#    print("TEXTS_IN")
#    print(texts_in)
#    print("TEXTS_OUT")
#    print(texts_out)
    
   # print(known_telemarketers)
    
   
    return potential_telemarketers


def printList(call_list):
    for call in call_list:
        print(call)
        
potential_tmkters = createHash(calls, texts)
print("These numbers could be telemarketers:")
printList(potential_tmkters)



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

