import math
frequency_read = 5 #time in seconds
frequency_write = 60 #time in seconds
buffer_timeperiod = 60 # time in seconds
execution_check = 5


buffer_length = math.ceil(int(buffer_timeperiod/frequency_read))


testingtimestamp =0
numberofports= 8
numberofareastemp= 4
""" gettable index variables
    withIndexGetter(jsonObject, index, variable):
        if('name' or 'value' or 'type'):#this triggers if temperature info is requested, max index of 3
        else:dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower, max index 15  
        return(variable, indexstring, value)
"""
variableboundaries = [ {'value': (0,0), 'poePower':(1,50),'rxRate':(0,100)},#port 1 (lowerboundary,upperboundary)
{'value': (50,80), 'poePower':(1,50),'rxRate':(0,100)},#port 2 or area2 depending on whether checking temp or ports
{'value': (100,500), 'poePower':(0,50),'rxRate':(0,7000)},
{'value': (0,0), 'poePower':(0,50),'rxRate':(0,7000)},
{'poePower':(0,50),'rxRate':(0,100)},#there are only 4 areas temperatures that can be read
{'poePower':(0,50),'rxRate':(0,100)},
{'poePower':(0,50),'rxRate':(0,100)},
{'poePower':(0,50),'rxRate':(0,5000)}
]
rxOnBoundary=0 #this is the boundary on which a port is concidered on based on received packages


#for unused proportion function
POEwarningproportion = 1.5
Errorwarningproportion= 1.5
Tempwarningproportion= 1.5
Ratewarningproportion= 3
