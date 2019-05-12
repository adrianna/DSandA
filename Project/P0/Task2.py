"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def formatDate(call_item):
    date_time_str = call_item
    date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M:%S').strftime('%B')
    #print(date_time_obj)

    return date_time_obj

def maxCallDuration(call_log):
    
    max_duration = 0
    for call_item in range(len(call_log)):
        duration = int(call_log[call_item][len(call_log[call_item]) - 1])
        date = call_log[call_item][len(call_log[call_item]) - 2]
        month = formatDate(date)
        if month == 'September':
            #print("Month: {}".format(month))
            if max_duration < duration:
                max_duration = duration
                phone_number = call_log[call_item][0]
                # print("Duration: {}".format(duration))
                # print("Max_Duration: {}".format(max_duration))
                # print("Phone Number: {}".format(phone_number))
           
    return max_duration, phone_number


max_duration, phone_number = maxCallDuration(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, max_duration))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

