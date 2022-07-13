from threading import Thread
import threethread #haven't been able to get threading to talk with other 
#files well, so temporarily usless
'''error message
File "/home/isaiah/code/main.py", line 3, in <module>
    Queofjson= queue.Queue()#maxsize=buffer_length)
NameError: name 'queue' is not defined

'''
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
import password
import queue
Queofjson= queue.Queue()#maxsize=buffer_length)



from requests.packages.urllib3.exceptions import InsecureRequestWarning
from ubnt import UnifiSwitchClient
import json
import math
import time
import requests
import csv




from waggle.plugin import Plugin
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
def getJson(Timestamp):
        temp=Queofjson.queue #this makes a copy of the given que in dque format which makes it possible to operate on its individual members
        for x in range(len(temp)):
                time, json=temp[x]
                #print(time, (time-Timestamp))
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
                        password=password.password) as client:#password is from another not included file
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
             #with Plugin() as plugin:
                #plugin.subscribe("LengthEdgeSwitchQue") #still non-functional
             while True:
                time.sleep(execution_check)
                #msg= plugin.get()
                #print("recieved from database", msg.value)
                
                '''
                print(int(time.time()*1000)-10000)
                print("----")
                print(getJson(int(time.time()*1000)-10000))
                
                '''
def Write(threadname, Queofjson):
        while True:
        #while (time.time()-starttime)<total_time:
                #pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
                timestamps=getquetimestamps()
                #print(timestamps)
                header = ['timestamps']
                Port1 = [timestamps]
                #header2 = ['what time started', 'started on', 'every time it changed', 'what it changed to each time']
                
                with Plugin() as plugin:
                        rightnow=time.time_ns()
                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                        plugin.publish("test.bytes", 1234, timestamp=rightnow)#,timestamp=rightnow)
                #can likly use 'edgeswitch' to publish edgeswitch contents
                
                with open('edgeswitch.csv', 'w', encoding='UTF8') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)
                        writer.writerow(Port1)
                time.sleep(frequency_write)           

def Main():
        #ReadingProcess =multiprocessing.Process(target=Read, args=("thread-1", Queofjson))
        ReadingProcess =Thread(target=Read, args=("thread-1", Queofjson)) 
        WritingProcess =Thread(target=Write, args=("thread-2", Queofjson))
        OtherProcess =Thread(target=Dostuff, args=("thread-3", Queofjson))
        ReadingProcess.start()
        WritingProcess.start()
        OtherProcess.start()
        #ReadingProcess.join()
        #WritingProcess.join()
        #OtherProcess.join()
        #print(getJson(testingtimestamp))
Main()
'''
with Plugin() as plugin:
        plugin.upload_file('edgeswitch', timestamp=str(datetime.now()))

Plugin.publish('test.bytes',self.parse())

'''
