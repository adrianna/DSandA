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

def firstRecord( record_list ):
    return (record_list[0]) 

def lastRecord( record_list ):
    return record_list[len(record_list)-1]

## Main
[outgoing_text, incoming_text, timestamp] = firstRecord(texts)
print("First record of texts, {} texts {} at time {}".format(outgoing_text, incoming_text, timestamp))

[outgoing_call, incoming_call, timestamp, duration] = lastRecord(calls)
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(outgoing_call, incoming_call, timestamp, duration))

##########################################################
##### Tests 
###
#def test(record, expected_record):
#    if record == expected_record:
#        return True
#    return False

#listA = ['abc', 'def', 'ghi']
#listB = ['zyx', 'wvu', 'tsq']

#print(test(firstRecord(listA), 'abc'))
#print(test(firstRecord(listB), 'zyx'))
#print(test(lastRecord(listA), 'ghi'))
#print(test(lastRecord(listB), 'tsq'))


    
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

