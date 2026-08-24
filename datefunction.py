import datetime

def print_current_timestamp():
    print(datetime.datetime.now())
---
print_current_timestamp()

for i in range(10):
    print_current_timestamp()
---
print(print_current_timestamp._doc_) 
curr_ts = print_current_timestamp
curr_ts()
help(curr_ts)
