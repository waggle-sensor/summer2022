from ubnt import UnifiSwitchClient
import json
import time
import requests
import csv
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import queue
import pprint
#from waggle.plugin import Plugin
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
numberiterations = 5 #iterations set to 30 in fianl project
Queofjson= queue.Queue(numberiterations)
wattagerecorders=[queue.Queue(maxsize=numberiterations) for i in range(8)] #ceates list of 8 ques for different ports
isoncurrent =  [False for i in range(8)] 
isonrecent =  [False for i in range(8)]
Averages = [0] * 8
Averages= [0.0 for i in range(8)]
Minimums = [0] * 8
Minimums = [150 for i in range(8)]#assumes that no port will have a higher minimum then 150 watts
Maximums = [0] * 8
Maximums = [0 for i in range(8)]
#pp = pprint.PrettyPrinter(indent=2, width=30, compact=True) #read when pretty print is desired
def getStatistics(jsonObject,portnumber,variable):# ex: 3 'poePower'
        data=json.loads(jsonObject)
        Statistic=data[0]['interfaces'][portnumber]['statistics'][variable]#port= 0-15, 
        #variable= dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower
        print(Statistic)
def getRaminfo(jsonObject,variable):
        data=json.loads(jsonObject)
        RamInfo=data[0]['device']['ram'][variable]#variable = usage, free, total
        print(RamInfo)
def getTempinfo(jsonObject,area,variable):#area= 0-3, 
        #variable= name, value, as well as type which is always other
        data=json.loads(jsonObject)
        TempInfo=data[0]['device']['temperatures'][area][variable]
        print(TempInfo)
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        Timestamp=data[0]['timestamp']
        print(Timestamp)
def getProcessorUsage(jsonObject):
        data=json.loads(jsonObject)
        ProcessorUsage=data[0]['device']['cpu'][0]['usage'] #second zero might be cpu
        print(ProcessorUsage)
def getUptime(jsonObject):
        data=json.loads(jsonObject)
        Uptime=data[0]['device']['uptime']
        print(Uptime)
for y in range(numberiterations): #iterations set to 30 in fianl project
        with UnifiSwitchClient(
                host='https://192.168.0.5',
                username='ubnt',
                password='why1not2') as client:
                info = client.get_POE_info()
        Queofjson.put(json.dumps(info))
        if y ==0:
                print(json.dumps(info)) #prints json in format that is readable
        data=json.loads(json.dumps(info))
        #pp.pprint(data) #prints json prettily to screen
        '''''
        first_elem= data[0]
        interfaces =first_elem['interfaces']
        for x in range(3): #iterates through each port, 8 in final
                poePower = interfaces[x]['statistics']['poePower']
                print (interfaces[x]['statistics']['poePower']) #this is the first POE reading, so 2.58
                if poePower!=0:#checks to see if anything currently plugged in
                        isoncurrent[x]= True
                else:
                        isoncurrent[x]= False
                if y==0|isonrecent[x]!=isoncurrent[x]:#checks to make sure that either this is the first iteration or something has been unplugged/pluggedin
                        wattagerecorders[x].put(datetime.datetime.now())#stores the changes with when they occured
                        wattagerecorders[x].put(isoncurrent[x])
                        print(y)
                isonrecent[x]=isoncurrent[x]     
                if poePower<Minimums[x]: #compars and sets maximums and mins per port
                        Minimums[x]=poePower
                if poePower>Maximums[x]:
                        Maximums[x]=poePower
                Averages[x]=Averages[x]+(poePower-Averages[x])/(y+1) #rolling average calculation
                #print ("port", x+1)
        '''
        #print ("iterations=", y+1)
        time.sleep(1) #set to 10 in final project 
jsonObject=Queofjson.get()
print('stat','port0','varPoe')
getStatistics(jsonObject,0,'poePower')
print('ram','usage')
getRaminfo(jsonObject,'usage')
print('temp','0','value')
getTempinfo(jsonObject,0,'value')
print('timestamp')
getTimestamp(jsonObject)
print('Uptime')
getUptime(jsonObject)
print('processor usage')
getProcessorUsage(jsonObject)

'''''
print (Averages[0])
print (Maximums[0])
print (Minimums[0])
header = ['minimums', 'maximums', 'averages']
Port1 = [Minimums[0], Maximums[0], Averages[0]]
header2 = ['what time started', 'started on', 'every time it changed', 'what it changed to each time']
que = list(wattagerecorders[0].queue)
with open('edgeswitch.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(Port1)
        writer.writerow(header2)
        writer.writerow(que)
'''''
# questions about  if os.path.exists('testing.0.0.0'):

"""
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
             'uptime': 84676},
  'interfaces': [{'id': '0/1',
                  'name': '',
                  'statistics': {'bytes': 0,
                                 'dropped': 0,
                                 'errors': 0,
                                 'packets': 0,
                                 'poePower': 2.58,
                                 'pps': 0,
                                 'rate': 0,
                                 'rxBytes': 0,
                                 'rxErrors': 0,
                                 'rxPPS': 0,
                                 'rxPackets': 0,
                                 'rxRate': 0,
                                 'txBytes': 0,
                                 'txErrors': 0,
                                 'txPPS': 0,
                                 'txPackets': 0,
                                 'txRate': 0}},
"""
