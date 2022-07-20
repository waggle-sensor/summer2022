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
                starttime=time.time()
                try:
                        with UnifiSwitchClient(
                                host='https://192.168.0.5',
                                username='ubnt',
                                password=password.password) as client:#password is from another not included file
                                
                                        info = client.get_statistic_info()
                                        if info!= 'Failed':
                                                dumpedjson=json.dumps(info)
                                                #print(dumpedjson) 
                                                variabletype, timestamp=statisticgetter.noIndexGetter(dumpedjson, 'timestamp')#gets timestamp from within json
                                                for queue in queues:
                                                        queue.put((timestamp, dumpedjson))
                                                endtime=time.time()
                                                if (frequency_read-(endtime-starttime))>0:     
                                                        time.sleep(frequency_read-(endtime-starttime))
                                        else: print("failed")
                except:
                                print("warning! switch not connected!")
                                endtime=time.time()
                                if (30-(endtime-starttime))>0:     
                                        time.sleep(frequency_read-(endtime-starttime))
                        
                        #print("trying to close")
                        #A=client.close()#because most information doesn't refresh within same session 
                
def Trigger(execution_check, bufferlength, queue):
             #with Plugin() as plugin:
                #plugin.subscribe("len(myconfig.Listofjson)EdgeSwitchQue") #still non-functional
             buffer = deque()
             portConnection=[]
             connectionStatus= [[0,'off'] for i in range(myconfig.numberofports)]#poe wattage, whether port is currently receiving data
             pastPOEstatus= ['off']*myconfig.numberofports
             #pastConnectionstatus= ['off']*myconfig.numberofports
             connectionComparer= ['off','off']
             """no unused variables
             previouspoes= [0]*myconfig.numberofports
             previousTemps= [0]*myconfig.numberofareastemp #need to do over temp areas
             previousRates= [0]*myconfig.numberofports
             previousErrors= [0]*myconfig.numberofports
             """
             
             while True:
                starttime=time.time()
                try:
                        item = queue.get(timeout=60)
                except Empty:
                        print("warning! no switch data!")
                buffer.append(item)
                while len(buffer) > bufferlength:
                        buffer.popleft()
                print("updated trigger buffer")
                
                if (len(buffer)!=0):
                        currenttimestamp, currentjson=buffer[-1]
                        for i in range(myconfig.numberofports):
                                Ratevariable, indexstring, currentrxRate= statisticgetter.withIndexGetter(currentjson, i,'rxRate')                            
                                if currentrxRate== 0:
                                        connectionComparer[1]='off'
                                else:
                                        connectionComparer[1]='on'
                                POEvariable, indexstring, currentPOE= statisticgetter.withIndexGetter(currentjson, i,'poePower')                            
                                if currentPOE== 0:
                                        connectionComparer[0]='off'
                                else:
                                        connectionComparer[0]='on'
                                
                                #print(type (connectionStatus[i]))
                                #print(type (connectionStatus[i][0]))
                                #print(type (connectionComparer[1]))
                                #if i==0:
                                        #print(connectionComparer[0])
                                        #print(pastPOEstatus[i], i)
                                        #print(currentPOE)
                                #print(i+1, currentrxRate)
                                #print(connectionStatus[i][1], i)
                                
                                if connectionComparer[1] is not connectionStatus[i][1]:
                                        #print("triggered")
                                        print(currenttimestamp,i+1,"connection changed connection is now ", connectionComparer[1])
                                        """
                                                string=currenttimestamp,indexstring,normalcheck
                                                if i==5:print("comparison rate should change")
                                                secondarys.RecordBigChanges(string)
                                        """
                                        #if i != 7:print("there is the connection status of next port is",connectionStatus[i+1][1])
                                        #print(connectionStatus)
                                        connectionStatus[i][1]=connectionComparer[1]
                                        #print(connectionStatus)
                                        #if(i==5):
                                        #print("here is the connection status",connectionStatus[i][1])
                                        #print("here is the connection status of next port is",connectionStatus[i+1][1])
                                        #print(connectionComparer[1])
                                
                                if connectionComparer[0] is not pastPOEstatus[i]:
                                        #print("triggered")
                                        print(currenttimestamp,i+1,'POE changed POE is now', connectionComparer[0])
                                        """
                                                string=currenttimestamp,indexstring,normalcheck
                                                if i==5:print("comparison rate should change")
                                                secondarys.RecordBigChanges(string)
                                        """
                                        pastPOEstatus[i]=connectionComparer[0]
                                connectionStatus[i][0]=currentPOE
                                        #print("pps recorded as", normalcheck)
                                endtime=time.time()
                                if (execution_check-(endtime-starttime))>0:     
                                        time.sleep(execution_check-(endtime-starttime))
                                        #msg= plugin.get()
                                        #print("recieved from database", msg.value)

def Write(frequency_write, queue):
        while True:
                starttime=time.time()
                try:
                        item=queue.get(timeout=60)
                        timestamp, jsonobject=item
                        for i in range(myconfig.numberofports):
                                variablecalled, indexstring, value= statisticgetter.withIndexGetter(jsonobject, i,'poePower')
                                """
                                withIndexGetter(jsonObject, index, variable):
                                        if('name' or 'value' or 'type'):#this triggers if temperature info is requested, max index of 3
                                        else:dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower, max index 15  
                                        return(variable, indexstring, value)
                                """
                                pair= str(timestamp), variablecalled, indexstring, str(value) 
                                with open('edgeswitch.csv', 'a', encoding='UTF8') as f:
                                        writer = csv.writer(f)
                                        writer.writerow(pair)
                                """   
                                stringoutput=','.join(pair)
                                with Plugin() as plugin:
                                        rightnow =time.time_ns()
                                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                                        plugin.publish("test.bytes", stringoutput, timestamp=rightnow)#,timestamp=rightnow) 
                                """
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

        Read(myconfig.frequency_read,[writer_queue, trigger_queue])
       
if __name__=="__main__":
        Main()                     
