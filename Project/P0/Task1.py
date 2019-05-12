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

def numUniquePhoneCalls(call_list):

    duplicates = {}
    unique_phone_numbers = 0
    num_calls = 0
    num_duplicates = 0
    total_calls = len(call_list)    # Number of call items times 2 for incoming and outgoing calls on same line.
    for item in range(total_calls):
        outgoing_call, incoming_call = call_list[item][0], call_list[item][1]
        if item >= 0:
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

    unique_phone_numbers = total_calls*2 - num_duplicates
#    print(num_calls)
    return unique_phone_numbers 

uniquePhoneNumbers = numUniquePhoneCalls(calls)
print("There are {} different telephone numbers in the records".format(uniquePhoneNumbers))
                 



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
