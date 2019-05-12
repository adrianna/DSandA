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

    duplicates = {}
    unique_phone_numbers = 0
    num_calls = 0
    num_duplicates = 0
    total_calls = len(call_list)    ## Number of call items in log. Each line has two numbers: outgoing and incoming number
    total_texts = len(text_list)    ## Number of text items in log. Likewise.

    total_items = max(total_calls, total_texts)
    for item in range(total_items):
        # Process outgoing calls first, make sure index is not out-of-bounds
        if item < total_calls:
            outgoing_call, incoming_call = call_list[item][0], call_list[item][1]
            if isEmpty(duplicates):
                duplicates[outgoing_call] = 1
                num_calls += 1
            elif outgoing_call not in duplicates:
                duplicates[outgoing_call] = 1
                num_calls += 1
            else:
                duplicates[outgoing_call] += 1
                num_duplicates += 1
            if incoming_call not in duplicates:
                duplicates[incoming_call] = 1
                num_calls +=1
            else:
                duplicates[incoming_call] = 1
                num_duplicates += 1
        # Process ougoing texts, no need to check if hash is empty.
        if item < total_texts:
            outgoing_text, incoming_text = text_list[item][0], text_list[item][1]
            if outgoing_text not in duplicates:
                duplicates[outgoing_call] = 1
                num_calls += 1
            else:
                duplicates[outgoing_call] = 1
                num_duplicates += 1
                    
            if incoming_text not in duplicates:
                duplicates[incoming_text] = 1
                num_calls +=1
            else:
                duplicates[incoming_text] = 1
                num_duplicates += 1
                    

    unique_phone_numbers = (total_calls + total_texts) * 2 - num_duplicates
    return unique_phone_numbers 

uniquePhoneNumbers = numUniquePhoneCalls(calls, texts)
print("There are {} different telephone numbers in the records".format(uniquePhoneNumbers))
                 



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
