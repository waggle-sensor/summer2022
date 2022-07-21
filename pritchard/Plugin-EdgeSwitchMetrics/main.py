#from sqlite3 import TimestampFromTicks
from threading import Thread
import myconfig
import statisticgetter
import secondarys
import password
from queue import Queue, Empty
from collections import deque
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from ubnt import UnifiSwitchClient
import json
import time
import requests
#import csv
from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def Read(frequency_read, queues):
        while True:
                starttime=time.time()
                try:
                        with UnifiSwitchClient(
                                host='https://192.168.0.5',
                                username='ubnt',
                                password=password.password) as client:#password is from another not included file
                                info = client.get_statistic_info()
                                dumpedjson=json.dumps(info)
                                variabletype, timestamp=statisticgetter.noIndexGetter(dumpedjson, 'timestamp')#gets timestamp from within json
                                for queue in queues:
                                        queue.put((timestamp, dumpedjson))
                                endtime=time.time()
                                if (frequency_read-(endtime-starttime))>0:     
                                        time.sleep(frequency_read-(endtime-starttime))
                except:
                        print("warning! switch not connected!")
                        endtime=time.time()
                        if (30-(endtime-starttime))>0:     
                                time.sleep(frequency_read-(endtime-starttime))
                        
def Trigger(execution_check, bufferlength, queue):
             buffer = deque()
             connectionStatus= [[0,'off'] for i in range(myconfig.numberofports)]#(poe wattage, 'on' if port is currently recieving data)
             while True:
                starttime=time.time()
                try:
                        item = queue.get(timeout=60)
                        buffer.append(item)
                except Empty:
                        print("warning! no switch data!")
                while len(buffer) > bufferlength:
                        buffer.popleft()
                print("updated trigger buffer")

                if (len(buffer)!=0):
                        timestamp, currentjson=buffer[-1]
                        for i in range(8):#number of iterations not adjustable upwards as it is reliant on boundaries set in config
                                Ratevariable, indexstring, currentrxRate= statisticgetter.withIndexGetter(currentjson, i,'rxRate')                            
                                if currentrxRate== myconfig.rxOnBoundary:#this threshold can be changed in config
                                        connectionStatus[i][1]='off'
                                else:
                                        connectionStatus[i][1]='on'
                                POEvariable, indexstring, currentPOE= statisticgetter.withIndexGetter(currentjson, i,'poePower')                            
                                connectionStatus[i][0]=currentPOE
                                for key in myconfig.variableboundaries[i]:
                                        currentvalue=statisticgetter.withIndexGetter(currentjson, i, key)[2]#[2] is becuase statisticgetters return tuples beyond just the value
                                        check=secondarys.isnormalcheck(key, i, currentvalue)
                                        if(check!=None):#check= low if below boundaries, high if above
                                                pair= str(i+1), key, check 
                                                stringoutput=','.join(pair)
                                                with Plugin() as plugin:
                                                        #timestamp =time.time_ns()#if uncommented, plugin will be sent current time as timestamp rather than the timestamp of the json
                                                        plugin.publish("test.bytes", stringoutput, timestamp=timestamp)
                                                        if key!= 'value':
                                                                plugin.publish("test.bytes", str(connectionStatus[i]), timestamp=timestamp)
                endtime=time.time()
                if (execution_check-(endtime-starttime))>0:     
                        time.sleep(execution_check-(endtime-starttime))      
def Write(frequency_write, queue):
        while True:
                starttime=time.time()
                try:
                        item=queue.get(timeout=60)
                        timestamp, jsonobject=item
                        #as this is implemented currently it cannot connect and publish to beehive,
                                #instead it publishes to a local directory through a changed environmental variable which is altered via "PYWAGGLE_LOG_DIR=runlog python3 Main.py"
                        with Plugin() as plugin:
                                rightnow =time.time_ns()
                                #plugin.upload_file('edgeswitch.csv')# this is for future use when beehive is accessible
                                plugin.publish("test.bytes", str(jsonobject), timestamp=rightnow)
                        '''this allows for writing to a csv file
                        with open('edgeswitch.csv', 'a', encoding='UTF8') as f:
                                writer = csv.writer(f)
                                writer.writerow(pair)
                        '''
                except Empty:
                        print("warning! no switch data!")
                        continue  
                endtime=time.time()
                if (frequency_write-(endtime-starttime))>0:     
                        time.sleep(frequency_write-(endtime-starttime))           
def Main():
        writer_queue =Queue()
        Thread(target=Write, args=(myconfig.frequency_write, writer_queue,), daemon=True).start()
        
        trigger_queue =Queue()
        Thread(target=Trigger, args=(myconfig.execution_check, myconfig.buffer_length, trigger_queue,), daemon=True).start()
        #by passing out two seperate queues, the risk of the two action threads is minimized
        Read(myconfig.frequency_read,[writer_queue, trigger_queue])
       
if __name__=="__main__":
        Main()                     
