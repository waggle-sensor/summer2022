from sqlite3 import TimestampFromTicks
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
import csv
from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
starttime = time.time()

def Read(frequency_read, queues):
        while True:
                with UnifiSwitchClient(
                        host='https://192.168.0.5',
                        username='ubnt',
                        password=password.password) as client:#password is from another not included file
                        info = client.get_POE_info()
                """
                if len(myconfig.Listofjson)==buffer_length:#this makes the que circular might be unneeded due to maxlen(myconfig.Listofjson)
                         myconfig.Listofjson.pop(0)
                
                """
                dumpedjson=json.dumps(info)
                #print(dumpedjson) 
                variabletype, timestamp=statisticgetter.noIndexGetter(dumpedjson, 'timestamp')#gets timestamp from within json
                for queue in queues:
                        queue.put((timestamp, dumpedjson))
                time.sleep(frequency_read)

"""
def noIndexGetter(jsonObject, variable):
        if(variable=='timestamp'):
        elif(variable=='uptime'):
        elif(variable=='processor usage'):
        elif(variable=='usage' or variable=='free' or variable=='total'):(ram)
        return(variable, value)
def withIndexGetter(jsonObject, index, variable):
        if(variable=='name' or variable=='value' or variable=='type'):#this triggers if temperature info is requested, max index of 3
        else:
              #this triggers if portsinformation is requested, port= 0-15
              #variable= dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower  
        return(variable, indexstring, value)

def isnormalcheck(variable, standardvalue, currentvalue)
"""


def Trigger(execution_check, bufferlength, queue):
             #with Plugin() as plugin:
                #plugin.subscribe("len(myconfig.Listofjson)EdgeSwitchQue") #still non-functional
             buffer = deque()
             previousvalues= [0]*myconfig.numberofports#expand to different type as we test more variables
             while True:
                try:
                        item = queue.get(timeout=60)
                except Empty:
                        print("warning! no switch data!")
                buffer.append(item)
                while len(buffer) > bufferlength:
                        buffer.popleft()
                print("updated trigger buffer")
                if (len(buffer)==1):
                        firsttimestamp, firstjsonobject=buffer[0]
                        originaluptime=statisticgetter.noIndexGetter(firstjsonobject, 'uptime')

                elif(len(buffer)>1):
                        currenttimestamp, currentjsonobject=buffer[-1]
                        pasttimestamp, pastjsonobject=buffer[-2]
                        currentuptime=statisticgetter.noIndexGetter(currentjsonobject, 'uptime')
                        if(currentuptime < originaluptime):#there might be a problem with this implemetation not triggering becuase too much delay
                                print(currenttimestamp, "the switch has restarted")
                                originaluptime=currentuptime                      
                        
                        for i in range(myconfig.numberofports):
                                POEvariable, indexstring, currentvalue= statisticgetter.withIndexGetter(currentjsonobject, i,'poePower')# return(Statistic,data[0]['timestamp'], portnumber, variable, 'basicstatis')
                                #print(currentvalue, i)
                                POEvariable, indexstring, pastvalue= statisticgetter.withIndexGetter(pastjsonobject, i,'poePower')
                                normalcheck=secondarys.isnormalcheck(POEvariable, pastvalue, currentvalue)
                                if normalcheck is not None:
                                        print(currenttimestamp,indexstring, normalcheck)#return(variable,"dropped is now this fraction of former value:",proportion)
                    
                #for i, item in enumerate(buffer):
                        #print(i, item)
                time.sleep(execution_check)
                #msg= plugin.get()
                #print("recieved from database", msg.value)

def Write(frequency_write, queue):
        while True:
                try:
                        item=queue.get(timeout=60)
                        timestamp, jsonobject=item
                        for i in range(myconfig.numberofports):
                                variablecalled, indexstring, value= statisticgetter.withIndexGetter(jsonobject, i,'poePower')# return(Statistic,data[0]['timestamp'], portnumber, variable, 'basicstatis')
                                pair= str(timestamp), variablecalled, indexstring, str(value) 
                                #isdropped, indexstring, value= statisticgetter.withIndexGetter(jsonobject, i,'dropped')# return(Statistic,data[0]['timestamp'], portnumber, variable, 'basicstatis')
                                #print(isdropped, indexstring)
                                stringoutput=','.join(pair)
                                
                                with open('edgeswitch.csv', 'a', encoding='UTF8') as f:
                                        writer = csv.writer(f)
                                        writer.writerow(pair)
                                
                                """   with Plugin() as plugin:
                                        rightnow =time.time_ns()
                                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                                        plugin.publish("test.bytes", stringoutput, timestamp=rightnow)#,timestamp=rightnow) """
                                
                                #can likly use 'edgeswitch' to publish edgeswitch contents
                                #print(timestamps)
                                #if(len(myconfig.Listofjson)!=0):
                                        #print(myconfig.Listofjson[0])
                except Empty:
                        print("warning! no switch data!")
                        continue  
                time.sleep(frequency_write)           

def Main():
        #ReadingProcess =multiprocessing.Process(target=Read, args=("thread-1", Listofjson))
        writer_queue =Queue()
        Thread(target=Write, args=(myconfig.frequency_write, writer_queue,), daemon=True).start()
        
        trigger_queue =Queue()
        Thread(target=Trigger, args=(myconfig.execution_check, myconfig.buffer_length, trigger_queue,), daemon=True).start()

        Read(myconfig.frequency_read,[writer_queue, trigger_queue])
       
if __name__=="__main__":
        Main()                     
        #ReadingProcess.join()
        #WritingProcess.join()
        #OtherProcess.join()
        #print(getJson(testingtimestamp))


