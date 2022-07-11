from ubnt import UnifiSwitchClient
import json
import time
import requests
import collections
import csv
import datetime
#import multiprocessing
from threading import Thread
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import queue
import pprint
#from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
numberiterations = 2 #iterations set to 30 in fianl project
frequency_read = 1
frequency_write = 2
execution_check =2
testingtimestamp =0
#Totaltime=frequency_read*numberiterations
Totaltime= 7 #due to how long the parts take if set normally there will not be enough time for all iterations

numberofports= 1
starttime = time.time()
Queofjson= queue.Queue()#maxsize=numberiterations)
#Queofjson=collections.deque(maxlen=numberiterations)
def getJson(Timestamp):
        temp=Queofjson.queue #this makes a copy of the given que in dque format which makes it possible to operate on its individual members
        for x in range(len(temp)):
                time, json=temp[x]
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        return json 
        return ('error submitted timestamp too low')
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        Timestamp=data[0]['timestamp']
        return(Timestamp)
#pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
def getStatistics(jsonObject,portnumber,variable):# ex: 3 'poePower'
        data=json.loads(jsonObject)
        Statistic=data[0]['interfaces'][portnumber]['statistics'][variable]#port= 0-15, 
        #variable= dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower
        #print('from statistic')
        #print(Statistic, data[0]['timestamp'])
        return(Statistic,data[0]['timestamp'])#return as tuple with timestamp
def getRaminfo(jsonObject,variable):
        data=json.loads(jsonObject)
        RamInfo=data[0]['device']['ram'][variable]#variable = usage, free, total
        return(RamInfo,data[0]['timestamp'])
def getTempinfo(jsonObject,area,variable):#area= 0-3, 
        #variable= name, value, as well as type which is always other
        data=json.loads(jsonObject)
        TempInfo=data[0]['device']['temperatures'][area][variable]
        return(TempInfo,data[0]['timestamp'])
def getProcessorUsage(jsonObject):
        data=json.loads(jsonObject)
        ProcessorUsage=data[0]['device']['cpu'][0]['usage'] #second zero might be cpu
        return(ProcessorUsage,data[0]['timestamp'])
def getUptime(jsonObject):
        data=json.loads(jsonObject)
        Uptime=data[0]['device']['uptime']
        return(Uptime,data[0]['timestamp'])
def getPOEAverages(jsonqueue):
        #Averages = [0] * numberofports
        #Averages= [0.0 for i in range(numberofports)]
        Averages =[(0,0)*numberofports]# error creates (0, 0, 0, 0, 0, 0)
        #print (type(Averages[0]))
        for y in range(numberiterations):
                jsonObject=jsonqueue.get()
              
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        poePower, time = getStatistics(jsonObject,1,'poePower')
                        temp =Averages[x][0]+(poePower-Averages[x][0])/(y+1) #rolling average calculation
                        Averages[x]=(temp, time)
        return (Averages)                       
def getPOEMaxes(jsonqueue):
        #timestamps = [0] * 8#not sure how to initialize list of timestamps want 
        #Maximums = [0] * 8
        print('max was called')
        Maximums =[(0,0)*numberofports]
        for y in range(numberiterations):
                print(y)
                jsonObject=jsonqueue.get()
                print('max should end')
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        poePower, time= getStatistics(jsonObject,1,'poePower')
                        if poePower>Maximums[x][0]:
                                Maximums[x]=(poePower,time)
        
        return (Maximums)
def getPOEMins(jsonqueue):  
        #timestamps = [0] * 8#not sure how to initialize list of timestamps
        Minimums =[(150,0)*numberofports]
        #Minimums = [0] * 8
        #Minimums = [150 for i in range(8)]#assumes that no port will have a higher minimum then 150 watts
        for y in range(numberiterations):
                jsonObject=jsonqueue.get()
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        poePower, time= getStatistics(jsonObject,1,'poePower')
                        if poePower<Minimums[x][0]: #compars and sets maximums and mins per port
                                Minimums[x]=(poePower,time)                    
        return (Minimums)
def getquetimestamps():
        Timestamps= [0 for i in range(Queofjson.qsize())]
        temp=Queofjson.queue
        for x in range(Queofjson.qsize()):
                Timestamps[x], json = temp[x]
        print(Timestamps)
        return (Timestamps)
def Read(threadname, Queofjson):
        #global Queofjson
        while (time.time()-starttime)<Totaltime:
                
                #print('read called')
                with UnifiSwitchClient(
                        host='https://192.168.0.5',
                        username='ubnt',
                        password='why1not2') as client:
                        info = client.get_POE_info()
                if Queofjson.qsize()==numberiterations:#this makes the que circular might be unneeded due to maxlength
                         Queofjson.get()
                Timestamp=getTimestamp(json.dumps(info))
                testingtimestamp= Timestamp
                Queofjson.put(( Timestamp,json.dumps(info)))
                print(Queofjson.qsize())
                #print(Queofjson[-1])
                time.sleep(frequency_read)
def Dostuff(threadname, Queofjson):
        #global Queofjson
        while (time.time()-starttime)<Totaltime:
                if(Queofjson.qsize()==1):
                        print('there are 1 jsons')
                #print(len(Queofjson))
                time.sleep(execution_check)
def Write(threadname, Queofjson):
        while (time.time()-starttime)<Totaltime:
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
        
'''''
def getonoff(jsonqueue): #there is o logic flaw in here that only takes note of the first time the value of isonrecent is changed
        onoff =[(True,time.time())]
        isoncurrent =  [False for i in range(numberofports)] 
        isonrecent =  [False for i in range(numberofports)]
        for y in range(numberiterations):
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        time, poePower = getStatistics(jsonObject,1,'poePower')
                        if poePower!=0:#checks to see if anything currently plugged in
                                isoncurrent[x]= True
                        else:
                                isoncurrent[x]= False
                        if y==0|isonrecent[x]!=isoncurrent[x]:#checks to make sure that either this is the first iteration or something has been unplugged/pluggedin
                                wattagerecorders[x].put(datetime.datetime.now())#stores the changes with when they occured
                                wattagerecorders[x].put(isoncurrent[x])
                                print(y)
                        isonrecent[x]=isoncurrent[x]   
  '''        
def Main():
        #ReadingProcess =multiprocessing.Process(target=Read, args=("thread-1", Queofjson))
        ReadingProcess =Thread(target=Read, args=("thread-1", Queofjson)) 
        WritingProcess =Thread(target=Write, args=("thread-2", Queofjson))
        OtherProcess =Thread(target=Dostuff, args=("thread-3", Queofjson))
        ReadingProcess.start()
        WritingProcess.start()
        OtherProcess.start()
        ReadingProcess.join()
        WritingProcess.join()
        OtherProcess.join()
        print('ending main')
        print(getJson(testingtimestamp))
Main()
'''
functionqueue1= copy.copy(Queofjson)
print(getPOEAverages(functionqueue1))#there is definitly a way to set the functions to static



functionqueue= copy.copy(Queofjson)
print(getPOEMaxes(functionqueue))





functionqueue2= copy.copy(Queofjson)
print(getPOEMins(functionqueue2))
#onoffs(functionqueue= Queofjson)
jsonObject=Queofjson.get()
print('stat','port0','varPoe')
print(getStatistics(jsonObject,1,'poePower'))
print('ram','usage')
print(getRaminfo(jsonObject,'usage'))
print('temp','0','value')
print(getTempinfo(jsonObject,0,'value'))
print('timestamp')
print(getTimestamp(jsonObject))
print('Uptime')
print(getUptime(jsonObject))
print('processor usage')
print(getProcessorUsage(jsonObject))
# questions about  if os.path.exists('testing.0.0.0'):

with Plugin() as plugin:
        plugin.upload_file('edgeswitch', timestamp=str(datetime.now()))
"""
# Plugin.publish('test.bytes',self.parse())

"""
[{'device': {'cpu': [{'identifier': 'ARMv7 Processor rev 1 (v7l)',
                      'usage': 54}],
             'fanSpeeds': [],
             'power': [],
             'ram': {'free': 69324800, 'total': 262553600, 'usage': 73},
             'storage': [],
             'temperatures': [{'name': 'TEMP-1',
                               'type': 'other',
                               'value': 61.0},
                              {'name': 'TEMP-2',
                               'type': 'other',
                               'value': 64.0},
                              {'name': 'PoE-01',
                               'type': 'other',
                               'value': 49.0},
                              {'name': 'PoE-02',
                               'type': 'other',
                               'value': 51.0}],
"""
'''
