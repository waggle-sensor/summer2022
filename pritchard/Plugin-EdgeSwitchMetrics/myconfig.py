import math
Listofjson =[]
frequency_read = 2 #time in seconds
frequency_write = 4 #time in seconds
buffer_timeperiod = 60 # time in seconds
execution_check = 1

buffer_length = math.ceil(int(buffer_timeperiod/frequency_read))
total_time= 7 #due to how long the parts take if set normally there will not be enough time for all iterations

testingtimestamp =0
numberofports= 1
