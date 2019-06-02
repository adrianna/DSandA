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

###################################################
##
## isEmpty(call_item)
##    Checks if call_item hash dictionary is empty
##
###################################################
def isEmpty(call_item):
    return not bool(call_item)

###################################################
##
## numUniquePhoneCalls(call_list, text_list)
##    Checks if call_item hash dictionary is empty
##
###################################################
def numUniquePhoneCalls(call_list, text_list):

    complete_list = []
    unique_phone_numbers = 0
    # Store all numbers in list
    complete_list = call_list + text_list
    
    unique = set()
    for item in range(len(complete_list)):
        outgoing, incoming = complete_list[item][0], complete_list[item][1]
        unique.add(outgoing)
        unique.add(incoming)
    unique_phone_numbers = len(unique)
        
    return unique_phone_numbers

uniquePhoneNumbers = numUniquePhoneCalls(calls, texts)
print("There are {} different telephone numbers in the records".format(uniquePhoneNumbers))
                 



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
