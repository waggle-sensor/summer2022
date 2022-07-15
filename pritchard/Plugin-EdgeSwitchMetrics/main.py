from sqlite3 import TimestampFromTicks
from threading import Thread
#files well, so temporarily usless
'''error message
File "/home/isaiah/code/main.py", line 3, in <module>
    Listofjson= queue.Queue()#maxsize=buffer_len(myconfig.Listofjson))
NameError: name 'queue' is not defined

'''
import myconfig
import statisticgetter
'''
#pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
#getStatistics(jsonObject,portnumber,variable):# ex: 3 'poePower'
#getRaminfo(jsonObject,variable):
#getTempinfo(jsonObject,area,variable):#area= 0-3, 
#getProcessorUsage(jsonObject):
#getUptime(jsonObject):
#getTimestamp
'''
import secondarys
'''
def getPOEAverages(iListofjson):      
def getPOEMaxes(iListofjson):
def getPOEMins(iListofjson):  
'''
import password
#import queue
#Listofjson= queue.Queue()#maxsize=buffer_len(myconfig.Listofjson))
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from ubnt import UnifiSwitchClient
import json
import matplotlib.pyplot as plt
import time
import requests
import csv
from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
starttime = time.time()
def Read(threadname, frequency_read, buffer_length):
        while True:
                #print('read called')
                with UnifiSwitchClient(
                        host='https://192.168.0.5',
                        username='ubnt',
                        password=password.password) as client:#password is from another not included file
                        info = client.get_POE_info()
                if len(myconfig.Listofjson)==buffer_length:#this makes the que circular might be unneeded due to maxlen(myconfig.Listofjson)
                         myconfig.Listofjson.pop(0)
                dumpedjson=json.dumps(info)
                #print(dumpedjson)
                Timestamp=statisticgetter.getTimestamp(dumpedjson)
                #print(Timestamp)
                myconfig.Listofjson.append(( Timestamp,dumpedjson))
                #if(len(myconfig.Listofjson)<2):
                       #print(dumpedjson)
                time.sleep(frequency_read)
def Dostuff(threadname, execution_check):
             #with Plugin() as plugin:
                #plugin.subscribe("len(myconfig.Listofjson)EdgeSwitchQue") #still non-functional
             while True:
                #if len(myconfig.Listofjson)==29:
                        #secondarys.getPlotofbufferStatistic('poePower', 0)
                time.sleep(execution_check)
                #msg= plugin.get()
                #print("recieved from database", msg.value)
                
                '''
                print(int(time.time()*1000)-10000)
                print("----")
                print(getJson(int(time.time()*1000)-10000))
                
                '''
def Write(threadname, frequency_write):
        while True:
                timestamps=secondarys.getlisttimestamps()
                #print(timestamps)
                #header = ['timestamps']
                #Port1 = [timestamps]
                if(len(myconfig.Listofjson)!=0):
                        (timestamp, jsonobject)=myconfig.Listofjson[0]
                        #print(type(jsonobject))
                        poePower, now = statisticgetter.getStatistics(jsonobject, 0,'poePower')
                        pair= str(now), str(poePower)
                        with open('edgeswitch.csv', 'a', encoding='UTF8') as f:
                                writer = csv.writer(f)
                                writer.writerow(pair)
                                #writer.writerow(Port1)

                print(len(myconfig.Listofjson))
                #print(timestamps)
                #if(len(myconfig.Listofjson)!=0):
                        #print(myconfig.Listofjson[0])
                with Plugin() as plugin:
                        rightnow=time.time_ns()
                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                        plugin.publish("test.bytes", 1234, timestamp=rightnow)#,timestamp=rightnow)
                #can likly use 'edgeswitch' to publish edgeswitch contents
                
                time.sleep(frequency_write)           

def Main():
        #ReadingProcess =multiprocessing.Process(target=Read, args=("thread-1", Listofjson))
        ReadingProcess =Thread(target=Read, args=("thread-1", myconfig.frequency_read, myconfig.buffer_length)) 
        WritingProcess =Thread(target=Write, args=("thread-2", myconfig.frequency_write))
        OtherProcess =Thread(target=Dostuff, args=("thread-3", myconfig.execution_check))
        ReadingProcess.start()
        WritingProcess.start()
        OtherProcess.start()
"""
                        Listoftimestamps=secondarys.getlisttimestamps()
                        firsttimestamp=Listoftimestamps[0]
                        lasttimestamp=Listoftimestamps[-1]
                        shortlist=secondarys.Getshortenedlist(firsttimestamp, lasttimestamp)
                        Timestamps=[0]*len(shortlist)
                        values=[0]*len(shortlist)
                        for x in range(len(shortlist)):
                                Timestamps[x], json = shortlist[x]
                                values[x], othertimestamps=statisticgetter.getStatistics(json,0,'poePower')
                        print(Timestamps)
                        print(type(Timestamps))
                        print(type(Timestamps[0]))
                        print(values)
                        print(type(values))
                        print(type(values[0]))
                        plt.plot(Timestamps, values)
                        print('where bug')
                        plt.xlabel('Timestamps')
                        plt.ylabel('poePower')
                        plt.title('poePower Vs Time')
                        plt.show()  
                        
                        
                        
                        
"""
                        
        #ReadingProcess.join()
        #WritingProcess.join()
        #OtherProcess.join()
        #print(getJson(testingtimestamp))
Main()
