"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import re
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def isEmpty(call_item):
    return not bool(call_item)

def phoneType( phone ):
    match = re.match(r'[7|8|9]', phone )
    if match:
        return 'm'
    match = phone.startswith("(080)")
    if match:
        return 'f'
    match = phone.startswith("140")
    if match:
        return 't'

    return 'o'

def mobileCode(call):
    mobile_code = None
    
    if phoneType(call) == 'm':
        mobile_code = call[:4]
    
    return mobile_code


def phoneToPhone(outgoing, incoming):

    if phoneType(outgoing) == 'f' and phoneType(incoming) == 'f':
        return 'f2f'
    elif phoneType(outgoing) == 'f' and phoneType(incoming) != 'f':
        return 'f2o'
    elif phoneType(outgoing) != 'f' and phoneType(incoming) == 'f':
        return 'o2f'
    elif phoneType(outgoing) != 'f' and phoneType(incoming) != 'f':
        return 'o2o'



def BangaloreCalls(outgoing_call):

    bangalore_outgoing_calls = {}
    
    if phoneType(outgoing_call) == 'f':
        outgoing_080 = outgoing_call[:5]
        if isEmpty(bangalore_outgoing_calls):
            bangalore_outgoing_calls[outgoing_080] = 1
        elif outgoing_080 not in bangalore_outgoing_calls:
            bangalore_outgoing_calls[outgoing_080] = 1
        else:
            bangalore_outgoing_calls[outgoing_080] += 1
    elif phoneType(outgoing_call) == 't':
        outgoing_140 = outgoing_call[:3]
        if isEmpty(bangalore_outgoing_calls):
            bangalore_outgoing_calls[outgoing_140] = 1
        elif outgoing_140 not in bangalore_outgoing_calls:
            bangalore_outgoing_calls[outgoing_140] = 1
        else:
            bangalore_outgoing_calls[outgoing_140] += 1
    elif phoneType(outgoing_call) == 'm':
        mobile_code =  mobileCode(outgoing_call)
        if isEmpty(bangalore_outgoing_calls):
            bangalore_outgoing_calls[mobile_code] = 1
        elif outgoing_140 not in bangalore_outgoing_calls:
            bangalore_outgoing_calls[mobile_code] = 1
        else:
            bangalore_outgoing_calls[mobile_code] += 1

    #print(bangalore_outgoing_calls)
    
    return bangalore_outgoing_calls


def parsePhoneCallsType(call_log):

    call_hash = {}
    mobile_area_codes = {}
    
    for call_item in range( len(call_log) ):
        outgoing_call, incoming_call = call_log[call_item][0], call_log[call_item][1]
#        print(outgoing_call, incoming_call)

        call_type = phoneToPhone(outgoing_call, incoming_call)
        if isEmpty(call_hash):
            call_hash[call_type] = 1
           # print(call_hash)
        elif call_type not in call_hash:
            call_hash[call_type] = 1
           # print(call_hash)
        else:
            call_hash[call_type] += 1
           # print(call_hash)

        mobile_area_codes.update(BangaloreCalls(outgoing_call))
                   
    return call_hash, mobile_area_codes

def percentageOfCalls(call_hash, type1, type2):
#    print("Inputs")
#    print("Types: {} , {}".format(type1, type2))
#    print(call_hash)
#    print("##")
    for types in call_hash.keys():
        #print("Types {}".format(types))
        if types == type1:
            #print("if: {}".format(types))
            #print(call_hash[types])
            numCalls_type1 = call_hash[types]
            #print("numCalls1: {}".format(numCalls_type1))
        if types == type2:
            #print("if: {}".format(types))
            numCalls_type2 = call_hash[types]
            #print(call_hash[types])
            #print("numCalls2: {}".format(numCalls_type2))

    percentage = numCalls_type1 / (numCalls_type1 + numCalls_type2) * 100
   
    return percentage

def printCodes(code_hash):

    for keys in code_hash.keys():
        print(keys)

    
# PART A
print("The numbers called by people in Bangalore have codes:")
call_types, bangalore_codes = parsePhoneCallsType(calls)
printCodes(bangalore_codes)

# PART B
percent_of_f2f_calls = percentageOfCalls(call_types, 'f2f', 'f2o')
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent_of_f2f_calls))



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
