import math
frequency_read = 1 #time in seconds
frequency_write = 10 #time in seconds
buffer_timeperiod = 60 # time in seconds
execution_check = 1


buffer_length = math.ceil(int(buffer_timeperiod/frequency_read))


testingtimestamp =0
numberofports= 8
numberofareastemp= 4

POEwarningproportion = 1.5
Errorwarningproportion= 1.5
Tempwarningproportion= 1.5
Ratewarningproportion= 3
