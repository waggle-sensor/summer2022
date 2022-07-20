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
                        info = client.get_statistic_info()
                        #print("trying to close")
                        #A=client.close()#because most information doesn't refresh within same session 
                dumpedjson=json.dumps(info)
                #print(dumpedjson) 
                variabletype, timestamp=statisticgetter.noIndexGetter(dumpedjson, 'timestamp')#gets timestamp from within json
                for queue in queues:
                        queue.put((timestamp, dumpedjson))
                time.sleep(frequency_read)
def Trigger(execution_check, bufferlength, queue):
             #with Plugin() as plugin:
                #plugin.subscribe("len(myconfig.Listofjson)EdgeSwitchQue") #still non-functional
             buffer = deque()
             previouspoes= [0]*myconfig.numberofports
             previousTemps= [0]*myconfig.numberofareastemp #need to do over temp areas
             previousRates= [0]*myconfig.numberofports
             previousErrors= [0]*myconfig.numberofports


             while True:
                try:
                        item = queue.get(timeout=60)
                except Empty:
                        print("warning! no switch data!")
                buffer.append(item)
                while len(buffer) > bufferlength:
                        buffer.popleft()
                print("updated trigger buffer")
                if (len(buffer)==1): #this provides the first values submitted into the que which will be the original values compared against
                        firsttimestamp, comparingjsonobject=buffer[0]
                        comparinguptime=statisticgetter.noIndexGetter(comparingjsonobject, 'uptime')
                        """
                        noIndexGetter(jsonObject, variable):
                                variable= 'timestamp' 'uptime' 'processor usage'):
                                'usage' or 'free' or 'total'):(ram)
                                return(variable, value)
                        """
                        for i in range(myconfig.numberofports):
                                Ratevariable, indexstring, originalvalue= statisticgetter.withIndexGetter(comparingjsonobject, i,'rate')
                                previousRates[i]= originalvalue
                                #if i ==1:print("this is the original rate", originalvalue)
                                POEvariable, indexstring, originalvalue= statisticgetter.withIndexGetter(comparingjsonobject, i,'poePower')
                                """
                                withIndexGetter(jsonObject, index, variable):
                                        if('name' or 'value' or 'type'):#this triggers if temperature info is requested, max index of 3
                                        else:dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower, max index 15  
                                        return(variable, indexstring, value)
                                """
                                previouspoes[i]= originalvalue
                                
                                Errorsvariable, indexstring, originalvalue= statisticgetter.withIndexGetter(comparingjsonobject, i,'errors')
                                previousErrors[i]= originalvalue
                        for i in range(myconfig.numberofareastemp):
                                Tempvariable, indexstring, originalvalue= statisticgetter.withIndexGetter(comparingjsonobject, i,'value')
                                previousTemps[i]= originalvalue      
                        
                                #Tempvariable, indexstring, originalvalue= statisticgetter.withIndexGetter(comparingjsonobject, i,'value')# need to alter this into a for loop to run through 4 temperatures
                elif(len(buffer)>1):
                        currenttimestamp, currentjsonobject=buffer[-1]
                        currentuptime=statisticgetter.noIndexGetter(currentjsonobject, 'uptime')
                      
                        if(currentuptime < comparinguptime):#there might be a problem with this implemetation not triggering becuase too much delay
                                print(currenttimestamp, "the switch has restarted")
                                comparinguptime=currentuptime                      
                        for i in range(myconfig.numberofareastemp):
                                Tempvariable, indexstring, currentTemp= statisticgetter.withIndexGetter(currentjsonobject, i,'value')
                                normalcheck=secondarys.isnormalcheck('temperature', previousTemps[i], currentTemp)#return(variable,"dropped is now this fraction of former value:",proportion)
                                #print(currentTemp, i)
                                
                                if normalcheck is not None:
                                        print(currenttimestamp,indexstring, normalcheck)
                                        previousTemps[i]=currentTemp
                                        
                        for i in range(myconfig.numberofports):
                                
                                Ratevariable, indexstring, currentRate= statisticgetter.withIndexGetter(currentjsonobject, i,'rate')                            
                                normalcheck=secondarys.isnormalcheck('rate', previousRates[i], currentRate)#return(variable,"dropped is now this fraction of former value:",proportion)
                                if normalcheck is not None:
                                        #print("pps recorded as", normalcheck)
                                        print(currenttimestamp,indexstring, normalcheck)
                                        string=currenttimestamp,indexstring,normalcheck
                                        if i==5:print("comparison rate should change")
                                        previousRates[i]=currentRate
                                        secondarys.RecordBigChanges(string)
                                        
                                if i== 5:print("when buffer is",len(buffer), "Rate is", currentRate, "compared rate is",previousRates[i])
                                
                                POEvariable, indexstring, currentPoe= statisticgetter.withIndexGetter(currentjsonobject, i,'poePower')
                                normalcheck=secondarys.isnormalcheck('poePower', previouspoes[i], currentPoe)#return(variable,"dropped is now this fraction of former value:",proportion)
                                if normalcheck is not None:
                                        print(currenttimestamp,indexstring, normalcheck)
                                        string=currenttimestamp,indexstring,normalcheck
                                        secondarys.RecordBigChanges(string)
                                        previouspoes[i]=currentPoe
                                Errorsvariable, indexstring, currentErrors= statisticgetter.withIndexGetter(currentjsonobject, i,'errors')
                                normalcheck=secondarys.isnormalcheck('errors', previousErrors[i], currentErrors)#return(variable,"dropped is now this fraction of former value:",proportion)
                                if normalcheck is not None:
                                        print(currenttimestamp,indexstring, normalcheck)
                                        previousErrors[i]=currentErrors
                                #if i==0 or i==5:
                                        #print(currentRate, i)
                                        #print(currentErrors, i)
                time.sleep(execution_check)
                #msg= plugin.get()
                #print("recieved from database", msg.value)

def Write(frequency_write, queue):
        while True:
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
                time.sleep(frequency_write)           
def Main():
        writer_queue =Queue()
        Thread(target=Write, args=(myconfig.frequency_write, writer_queue,), daemon=True).start()
        
        trigger_queue =Queue()
        Thread(target=Trigger, args=(myconfig.execution_check, myconfig.buffer_length, trigger_queue,), daemon=True).start()

        Read(myconfig.frequency_read,[writer_queue, trigger_queue])
       
if __name__=="__main__":
        Main()                     

