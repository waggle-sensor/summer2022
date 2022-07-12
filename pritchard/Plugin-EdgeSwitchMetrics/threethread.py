#three threads
import json
import time
import secondarys
import statisticgetter
from ubnt import UnifiSwitchClient
import json
import math
import time
import requests
import csv
import statisticgetter
'''
#pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
#getStatistics(jsonObject,portnumber,variable):# ex: 3 'poePower'
#getRaminfo(jsonObject,variable):
#getTempinfo(jsonObject,area,variable):#area= 0-3, 
#getProcessorUsage(jsonObject):
#getUptime(jsonObject):
'''
import secondarys
'''
def getPOEAverages(jsonqueue):      
def getPOEMaxes(jsonqueue):
def getPOEMins(jsonqueue):  
'''
import threethread
from threading import Thread
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import queue
#from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


frequency_read = 2 #time in seconds
frequency_write = 4 #time in seconds
buffer_timeperiod = 60 # time in seconds
execution_check = 4

buffer_length = math.ceil(int(buffer_timeperiod/frequency_read))
total_time= 7 #due to how long the parts take if set normally there will not be enough time for all iterations

testingtimestamp =0
#total_time=frequency_read*buffer_length
numberofports= 1

starttime = time.time()
Queofjson= queue.Queue()#maxsize=buffer_length)

#Queofjson=collections.deque(maxlen=buffer_length)
def getJson(Timestamp):
        temp=Queofjson.queue #this makes a copy of the given que in dque format which makes it possible to operate on its individual members
        for x in range(len(temp)):
                time, json=temp[x]
                print(time, (time-Timestamp))
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        break
        return json
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        Timestamp=data[0]['timestamp']
        return(Timestamp)

def getquetimestamps():
        Timestamps= [0 for i in range(Queofjson.qsize())]
        temp=Queofjson.queue
        #print(temp)
        for x in range(Queofjson.qsize()):
                Timestamps[x], json = temp[x]
        #print(Timestamps)
        return (Timestamps)



def Read(threadname, Queofjson):
        #global Queofjson
        #while (time.time()-starttime)<total_time:
        while True:
                #print('read called')
                with UnifiSwitchClient(
                        host='https://192.168.0.5',
                        username='ubnt',
                        password='why1not2') as client:
                        info = client.get_POE_info()
                if Queofjson.qsize()==buffer_length:#this makes the que circular might be unneeded due to maxlength
                         Queofjson.get()
                Timestamp=statisticgetter.getTimestamp(json.dumps(info))
                testingtimestamp= Timestamp
                Queofjson.put(( Timestamp,json.dumps(info)))
                print(Queofjson.qsize())
                #print(Queofjson[-1])
                time.sleep(frequency_read)
def Dostuff(threadname, Queofjson):
             while True:
                time.sleep(execution_check)
                print(int(time.time()*1000)-10000)
                print("----")
                print(getJson(int(time.time()*1000)-10000))
def Write(threadname, Queofjson):
        while True:
        #while (time.time()-starttime)<total_time:
                #pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
                #print('write called')
                timestamps=getquetimestamps()
                #print(timestamps)
                header = ['timestamps']
                Port1 = [timestamps]
                #header2 = ['what time started', 'started on', 'every time it changed', 'what it changed to each time']
                with open('edgeswitch.csv', 'w', encoding='UTF8') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerow(Port1)
                time.sleep(frequency_write)       