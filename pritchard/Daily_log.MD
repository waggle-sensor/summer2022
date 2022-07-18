# Daily Progress Report
----------------------------------------------
### Week 1: 5/31 to 6/3 ###
#### Tuesday May 31th ####
- [ ] Attended the first introduction session
- [ ] Got workday details in order, including banking

#### Wednesday June 1th ####
- [ ] Attended the second introduction session
- [ ] Obtained Argonne badge
- [ ] Took mandatory TMS courses

#### Thursday June 2th ####
- [ ] Gained access to teams channel
- [ ] Gained access to email/authenticator app
- [ ] Gained access to my.anl.gov
- [ ] Made Github account/practiced making files and editing them
- [ ] Met with Abayomi to learn about Summer2022 slack and the tutorials we are supposed to go through 
- [ ] Went through pywaggle code base, compiled questions on portions I didn't understand

Things to do: 
- [ ] Ask Raj about Taylor University supervisor agreement
- [ ] Get github permission to edit Summer2022
- [ ] Figure out how to record daily logs on github
- [ ] Gather all questions together for eventual meeting with Raj
- [ ] Conduct basic research on "LoRaWan"

#### Friday June 3th ####
- [ ] Looked through Summer 2020 repo
  - [ ] Followed through tutorials 
  - [ ] Setup required accounts
  - [ ] Found bugs in repo links

Things to do:
- [ ] Talk with Raj about questions, bugs in Summer2022 repo and supervisor agreement

### Week 2: 6/6 to 6/10 ###
#### Monday June 6th ####
- [ ] Made a word doc containing previous python issues and repo bugs
- [ ] Messaged Raj about bugs in 
- [ ] Organized list of questions
- [ ] Worked out much of prevoius pywaggle related questions for Raj

Things to do:
- [ ] Talk with Raj about pywaggle and basic project questions, bugs in Summer2022 repo and supervisor agreement

#### Tuesday June 7th ####
- [ ] Met with Raj to talk about what I will be doing in the project, clarified that I can get my pywaggle questions ansewered later n project
- [ ] Received WisGate, Rakpi, Nvidea nano, partialy broken mini router, and ethernet cabels 
- [ ] Began process of getting received devices all connected through ethernet
- [ ] Got firmware images of Nvidea nano and RAKpi updated

Things to do:
- [ ] Re-do supervisor agreement and get signature
- [ ] Finish setting up and connecting to recevied devices

#### Wednesday June 8th ####
- [ ] Attended the required participation wedsday lecture
- [ ] Learned linux commands for accessing devices over ethernet 
- [ ] Finished connecting to and initializing all devices
- [ ] Got Github access aproved

Things to do:  
- [ ] Re-do supervisor agreement and get signature
- [ ] Create virtual daily log
- [ ] Prepare for presentation on friday about WisGate VS RAZPi

#### Thursday June 9th ####
- [ ] Attended AI seminar
- [ ] Attended workplace violence seminar
- [ ] Rewrote supervisor agreement
- [ ] Joined sage slack
- [ ] Finished pre-hire survey
- [ ] Researched for presentation on friday about WisGate VS RAZPi

Things to do: 
- [ ] Re-do supervisor agreement and get signature
- [ ] Create virtual daily log
- [ ] Prepare for presentation on friday about WisGate VS RAZPi

#### Friday June 10th ####
- [ ] Rewrote paper and recived signature
- [ ] Finished updating to current Waggle daily journal
- [ ] Researched for presentation
- [ ] Gave presentation

Things to do:
- [ ] Fix broken WisGateway

### Week 3: 6/13 to 6/17 ###
#### Monday June 13th ####
- [ ] Fixed broken WisGateway by using recovery software and redownloading firmware
- [ ] Attended writing workshop introduction
- [ ] Talked to Raj about buying senors to act as end nodes: he agreed
- [ ] Reiceved instruction: Raj wants me and other interns to set up bike racks for sensor testing, some week not 100F

Things to do:
- [ ] Update daily journal
- [ ] Talk to Raj about setting up Creat robot
- [ ] Make shopping list of sensors and needed parts

#### Tuesday June 14th ####
- [ ] Make shopping list of sensors and needed parts
- [ ] Updated daily journal
- [ ] Attended student connection group session
- [ ] Presented shopping list to Raj-> Decided we would use arduinos instead of RAK based WisBlock

Things to do:
- [ ] Find antenna for MKR WAN 1300 Arduino

#### Wednesday June 15th ####
- [ ] Found antenna for MKR WAN 1300 Arduino
- [ ] Updated daily log
- [ ] Attended seminar on graduate studies options
- [ ] Met with Andre (over slack) to bring him up to speed
- [ ] Applied for Waggle summer get together
- [ ] Met with Raj about purchasing anntena
- [ ] Found some related tutorials and information on using MKR Wan 1310 chips
- [ ] Completed Student Pulse survey
- [ ] Did some more Lora vs Lora Wan research

Things to do:  
- [ ] Improve Daily Log quality
- [ ] Read and take notes on four acamemic articles relevant to LoRa/LoRaWAN
- [ ] Make slide presentation on project relevant information from articles 
- [ ] Experiment with nano

#### Thursday June 16th ####
- [ ]  Read and took notes on four acamemic articles relevant to LoRa/LoRaWAN
- [ ]  Spoke to Raj about what he cared about for the research presentation
- [ ]  Helped settle Andre into project

Things to do: 
- [ ] Finishing the presentation on LoraWAN research

#### Friday June 17th ####
- [ ] Finished the presentation
- [ ] Presented the presentation
- [ ] Found space on 7th floor where I could work

Things to do:
- [ ] Setup linux laptop so I can use it as my main computer at work
- [ ] Talk to Raj about: when arduinos will be in, when I will set up bike racks, how I should go about setting up a network server,

### Week 4: 6/20 to 6/24 ###
#### Monday June 20th ####
- [ ] Got outlook/Github/slack/setup on linux computer
- [ ] Talked with Raj about: arduino arrvial date, when we would be setting up bike racks to act as testing rigs, how I should go a bout testing the nano's interaction with the WisGate
- [ ] setup LoRaWAN server on Nano so as to communicate with WisGate acting as a gateway

Things to do:
- [ ] Talk about future project steps with Raj and Andre

#### Tuesday June 21th ####
- [ ] Met with Raj and Andre, clarified that we want the gateway to also act as a network server, and verified that the next step will be to figure out how to communicate with Nvidia Nano
- [ ] researched how we can get data from the network server on the WisGate to the Nano, two feasable methods were grabbing off the local api or via the built in mqtt broker
- [ ] participated in required weekly student meeting

Things to do:
- [ ] make the Nano talk with the WisGate via the MQTT broker which includes figuring out how to setup a mqtt client on the nano

#### Wednesday June 22th ####
- [ ] setup bike raks outside as testing rigs for nodes
- [ ] helped setup 4th floor lab
- [ ] did research on how to register with and recieve messages from Wisgate MQTT broker

Things to do:  
- [ ] settle the communication path with the broker

#### Thursday June 23th ####
- [ ]  Rediscovered Ip adress of WisGate
- [ ]  reconnected everything to Wireless
- [ ]  decided on using Paho library in Python to make barebones client
- [ ]  successfully sent message to WisGate MQTT broker

Things to do: 
- [ ] get WisGate to send message through MQTT broker from its inputs

#### Friday June 24th/weekend ####
- [ ] unsussessfully tried to connect WisGate to home router for serveral hours
- [ ] discoered that WisGate cannot send broker messages over self generated Wifi network
- [ ] did some research on RAK serial port tool

Things to do:
- [ ] Get WisGate to accept some fake data via RAK serial port tool 

### Week 5: 6/27 to 6/31 ###
#### Monday June 27th ####
- [ ] discovered that RAK serial port tool can only be used on "devices" that are sensors
- [ ] messed up wireless network while trying to implement previous test
- [ ] figured out workaround for notation problem when labling MQTT topics/ topics san be refered to using "wildcards" like "+" in wisGate terminal, but will still update from messages from the Nano client that fall within a smaller domain 
- [ ] Began working on EdgeSwitch project, goal: to monitor specific conditions of particular ports via automated ssh and activly display said data in local system
- [ ] Found related commands to display required data over ssh

Things to do:
- [ ] write python file to monitor specific conditions of particular ports via automated ssh and activly display said data in local system

#### Tuesday June 28th ####
- [ ] made some progress on writing automated ssh code
- [ ] learned of previously made repo that spits out slightly different data from that what I am looking for from same edge switch
- [ ] upon further analysis found that repo used the locally hosted api
- [ ] with Raj's help got a basic main.py to print out large section of port data
- [ ] spent time learing about parsing json
- [ ] made initial testing file that relied upon a .JSON file filled with the contents of what was originally spit out by the main.py to attempt to parse said printed out data for what we want

Things to do:
- [ ] parse data

#### Wednesday June 29th ####
- [ ] went to summer meetup
- [ ] did an hour of research on the error I got the day before

Things to do:  
- [ ] parse .Json data

#### Thursday June 30th ####
- [ ]  discovered that error resulted from the printing of the data which converts the data to something unreadable to parsing methods
- [ ]  began working in original main.py file 
- [ ]  discovered that the file that is imported into main.py is in the form of a list instead of a JSON object and attempts to convert said list to Python dictionary or JSON result in a single member list

Things to do: 
- [ ] figure out how to get an output that can be read as a python dictionary

#### Friday June 31th ####
- [ ] switched laptops after repeated crashing
- [ ] Raj decided we will move forwards with rack pie and leave WisGate behind for now
- [ ] successfully accessed and parsed data from EdgeSwitch 8
- [ ] ![image](https://user-images.githubusercontent.com/106760508/176968684-959c4733-54df-4bb4-a4a6-b44d601e7a6f.png)
- [ ] ![image](https://user-images.githubusercontent.com/106760508/176968819-f7d14522-4b78-4139-b6a8-c742f23132e3.png)
- [ ] my code essentially excepts a passed list, which is obtained from a local api using the given credentials, reformats it, then accesses the first element of it which is actually a python dictionary
- [ ] after that a specific section of that library that conatins details useful to us, (interfaces), is taken and then sliced again to find the specific value we are looking for, in this case the first poe wattage value

### Week 6: 6/27 to 6/31 ###
#### Monday June 27th ####
- [ ] discovered that RAK serial port tool can only be used on "devices" that are sensors
- [ ] messed up wireless network while trying to implement previous test
- [ ] figured out workaround for notation problem when labling MQTT topics/ topics san be refered to using "wildcards" like "+" in wisGate terminal, but will still update from messages from the Nano client that fall within a smaller domain 
- [ ] Began working on EdgeSwitch project, goal: to monitor specific conditions of particular ports via automated ssh and activly display said data in local system
- [ ] Found related commands to display required data over ssh

Things to do:
- [ ] write python file to monitor specific conditions of particular ports via automated ssh and activly display said data in local system

#### Tuesday June 28th ####
- [ ] made some progress on writing automated ssh code
- [ ] learned of previously made repo that spits out slightly different data from that what I am looking for from same edge switch
- [ ] upon further analysis found that repo used the locally hosted api
- [ ] with Raj's help got a basic main.py to print out large section of port data
- [ ] spent time learing about parsing json
- [ ] made initial testing file that relied upon a .JSON file filled with the contents of what was originally spit out by the main.py to attempt to parse said printed out data for what we want

Things to do:
- [ ] parse data

#### Wednesday June 29th ####
- [ ] went to summer meetup
- [ ] did an hour of research on the error I got the day before

Things to do:  
- [ ] parse .Json data

#### Thursday June 30th ####
- [ ]  discovered that error resulted from the printing of the data which converts the data to something unreadable to parsing methods
- [ ]  began working in original main.py file 
- [ ]  discovered that the file that is imported into main.py is in the form of a list instead of a JSON object and attempts to convert said list to Python dictionary or JSON result in a single member list

Things to do: 
- [ ] figure out how to get an output that can be read as a python dictionary

#### Friday June 31th ####
- [ ] switched laptops after repeated crashing
- [ ] Raj decided we will move forwards with rack pie and leave WisGate behind for now
- [ ] successfully accessed and parsed data from EdgeSwitch 8
- [ ] ![image](https://user-images.githubusercontent.com/106760508/176968684-959c4733-54df-4bb4-a4a6-b44d601e7a6f.png)
- [ ] ![image](https://user-images.githubusercontent.com/106760508/176968819-f7d14522-4b78-4139-b6a8-c742f23132e3.png)
- [ ] my code essentially accepts a passed list, which is obtained from a local api using the given credentials, reformats it, then accesses the first element of it which is actually a python dictionary
- [ ] after that a specific section of that library that conatins details useful to us, (interfaces), is taken and then sliced again to find the specific 
 
### Week 7: 7/5 to 6/31 ###
#### Tuesday July 5 ####
- [ ] WFH due to family member catching covid
- [ ] wrote basic code for prcessing POE outputs by minimum maximum and average in file over 5min interval
- [ ] ![image](https://user-images.githubusercontent.com/106760508/177434446-c4205417-51d2-46cf-9c7b-288f0c5cc0fb.png)



Things to do:
- [ ] fix bugs in code
- [ ] create system for reognizing consistent change in POE levels
- [ ] figure out how to write outputs to CSV file


#### Wednesday June 29th ####
- [ ] Attended seminar on how our oral and postor presentations will work
- [ ] Fixed a bug in code that created a delay after each port read rather than after each iteration of reading all the ports
```
          print ("port", x+1)#line of code was here
        print ("iterations=", y+1)
        time.sleep(1) #set to 10 in final project # is now here

```
- [ ] Adjusted code for testing purposes: added testing print outs and decreased the delay, number of iterations and number of ports tested
```
for y in range(5): #iterations set to 30 in fianl project
 for x in range(3): #iterates through each port, 8 in final
 time.sleep(1) #set to 10 in final project
 
 print (Averages[0])
print (Maximums[0])
print (Minimums[0])
print (pluggschanged[0])
```
- [ ] Added code to allow for notation to determine if port had a power consuming device plugged in or unplugged during testing period
```
if pluggschanged[x]==0: #checks to make sure nothing was plugged into or unplugged from this port since beggining of test
                        if poePower!=0:#checks to see if anything currently plugged in
                                isoncurrent[x]= 'True'
                        else:
                                isoncurrent[x]= 'False'
                        if y==0:
                                isonoriginal[x]=isoncurrent[x]
                        elif isonoriginal[x]!=isoncurrent[x]:
                                if isonoriginal[x]== True:
                                        pluggschanged[x]= 2 #something was unplugged at this port
                                else:
                                        pluggschanged[x]= 1 #something was plugged in at this port
```
- [ ] Added code to write results to csv file
```
header = ['minimums', 'maximums', 'averages', 'pluggschanged', 'Started plugged in']
Port1 = [Minimums[0], Maximums[0], Averages[0], pluggschanged[0], isonoriginal[0]]
with open('edgeswitch.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(Port1)
```
- [ ] Added code to ignore Insecure request warning
```
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```
- [ ] Spoke with Raj about current progress in project, was directed to focus on using a que to record events
- [ ] Created new file caled Plugin-EdgeSwitchMetrics in repo to contain current progress in project, as well as a readme to describe that progress
- [ ] Spoke to Abayomi about how to use the pywaggle system to set up ifrustructure to send data while still being able to see it locally by setting up a local directory and directing pywaggle to send its logs there via command line, plugin-logls is the name of the directory
```
env PYWAGGLE_LOG_DIR=/plugin-logls 
```

Things to do:  
- [ ] Talk with Raj about which additional variables we want take from api
- [ ] Get Docker fully functional on loaned computer 
- [ ] Set up a working heap system for event notifications
- [ ] Ask about whether I need to use docker
- [ ] Set up connection to Github repo from loaned computer for easy commits
- [ ] look into "warning keyring is skipped, failed to download keyring error"

#### Thursday June 30th ####
- [ ] Recorded previous day's journal
- [ ] Added List of queues system to store events
 ```
import queue
wattagerecorders=[queue.Queue() for i in range(8)] #ceates list of 8 ques for different ports
 ```
- [ ] Altered input testing logic to better fit new storing system
 ```
   if poePower!=0:#checks to see if anything currently plugged in
                        isoncurrent[x]= True
                else:
                        isoncurrent[x]= False
                if y==0|isonrecent[x]!=isoncurrent[x]:#checks to make sure that either this is the first iteration or something has been unplugged/pluggedin
                        wattagerecorders[x].put(datetime.datetime.now())#stores the changes with when they occured
                        wattagerecorders[x].put(isoncurrent[x])
                isonrecent[x]=isoncurrent[x]     
 ```
- [ ] Added code to identify and store date and time per event occurance
 ```
 wattagerecorders[x].put(datetime.datetime.now())#stores the changes with when they occured
 ```
- [ ] Added code to print individual que to csv file by first converting it to a list
 ```
 header2 = ['started on', 'every time it changed', 'what it changed to each time']
que = list(wattagerecorders[0].queue)
with open('edgeswitch.csv', 'A', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(Port1)
        writer.writerow(header2)
        writer.writerow(que)
 ```
- [ ] Displayed demo of progress to Raj
- [ ] Talked to Raj about what he wants in project: whole json objects stored in que and then parsed as we need from buffer


Things to do: 
- [ ] Add previous WisGate work to Github
- [ ] Link up local repo for easy commits
- [ ] figure out full system of storing json objects, then recalling and analizing them

#### Friday June 31th ####
- [ ] Made list of all availible values accessible on api page 
```
0.timestamp
0.device.0.identifier
0.device.0.usage
0.device.ram.usage
0.device.ram.free
0.device.ram.total

x is between 0 and 3
0.device.temperatures.x.name
0.device.temperatures.x.type 
0.device.temperatures.x.value
  #two lower ports are poe ports, all types are other
0.device.uptime

x is between 0 and 15
0.interfaces.x.statistics.dropped
0.interfaces.x.statistics.errors
0.interfaces.x.statistics.txErrors
0.interfaces.x.statistics.rxErrors
0.interfaces.x.statistics.rate
0.interfaces.x.statistics.txRate
0.interfaces.x.statistics.rxRate
0.interfaces.x.statistics.bytes
0.interfaces.x.statistics.txBytes
0.interfaces.x.statistics.rxBytes
0.interfaces.x.statistics.packets
0.interfaces.x.statistics.txPackets
0.interfaces.x.statistics.rxPackets
0.interfaces.x.statistics.pps
0.interfaces.x.statistics.txPPS
0.interfaces.x.statistics.rxPPS
0.interfaces.x.statistics.poePower
```
- [ ] Made functions to return particular specified values after receiving the json of a particular iteration
```
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
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        Timestamp=data[0]['timestamp']
        return(Timestamp) 
def getProcessorUsage(jsonObject):
        data=json.loads(jsonObject)
        ProcessorUsage=data[0]['device']['cpu'][0]['usage'] #second zero might be cpu
        return(ProcessorUsage,data[0]['timestamp'])
def getUptime(jsonObject):
        data=json.loads(jsonObject)
        Uptime=data[0]['device']['uptime']
        return(Uptime,data[0]['timestamp'])
```
- [ ] Figured out how make que of json objects as well as how to run through that que when doing processing for a particular value
```
Queofjson.put(json.dumps(info))
jsonObject=Queofjson.get()
```
- [ ] Figured out how to send out and receive all values in the form of tuples which contain the wanted value as well as the timestamp of when that value occured
```
 Averages =[(0,0)*numberofports]# error creates (0, 0, 0, 0, 0, 0)
temp =Averages[x][0]+(poePower-Averages[x][0])/(y+1) #rolling average calculation
                        Averages[x]=(temp, time)
```
- [ ] Made new versions of previous average, minimum and maximum value finders, sussessfully got average function fully operational
```
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
output:functions
functionqueue1= copy.copy(Queofjson)
print(getPOEAverages(functionqueue1))#there is definitly a way to set the functions to static
functionqueue= copy.copy(Queofjson)
print(getPOEMaxes(functionqueue))
output:
python3 main.py
[(0.96, 1657550520513)]
max was called
0

```

Things to do
- [ ] Fix bug that occures when passing queue to max function
- [ ] Fix Average value function so it doesn't just return the last timestamp it received
- [ ] Add previous WisGate work to Github
- [ ] Link up local repo for easy commits
- [ ] make function to return any specific value of a specific iteration given the full json que

### Week 8: 7/11 to 7/15 ###
#### Monday June 13th ####
- [ ] Talked with Raj, he wants: circular buffer, three threads that operate at smae time-> reading standard writing and intercetion writing, three variables to control-> the total time the function is active, the delay between occurances of reading as well as writing
- [ ] Wrote code for the three basic threads as separate functions
```
def Read(threadname, Queofjson):
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
```
- [ ] Created Cycling Queue system primarily within Read function
```
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
```
- [ ] Changed the libraries used by Queue so as to allow the threads to act opon common variables
```
#import multiprocessing
from threading import Thread
import queue
```
- [ ] Added function to return respective timestamps for all jsons currently in que
```
def getquetimestamps():
        Timestamps= [0 for i in range(Queofjson.qsize())]
        temp=Queofjson.queue
        for x in range(Queofjson.qsize()):
                Timestamps[x], json = temp[x]
        print(Timestamps)
        return (Timestamps)
```
- [ ] Added funtion to return a json from Queue given its timestamp, this timestamp is currently automatically called
```
def getJson(Timestamp):
        temp=Queofjson.queue #this makes a copy of the given que in dque format which makes it possible to operate on its individual members
        for x in range(len(temp)):
                time, json=temp[x]
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        return json 
        return ('error submitted timestamp too low')
```
output:
```
[]
1
there are 1 jsons
[1657577106639]
2
[1657577106639, 1657577108339]
2
[1657577108339, 1657577110282]
2
ending main
[{"timestamp": 1657577110282, "device":......
```


Things to do:
- [ ] Write code to improve getaverage() function to return timestamp of when output closest to average ocuured

#### Tuesday June 14th ####
- [ ] Talked with and provided demo of current process to Raj, 
he wants:
- [ ] login password removed from commited file and password changed in device
  - [ ] My solution: storing the password in a noncommited python file as a variable
```
 with UnifiSwitchClient(
                        host='https://192.168.0.5',
                        username='ubnt',
                        password=password.password) as client:#password is from another not included file
                        info = client.get_POE_info()
```
- [ ] Current main Python file broken up into multiple other files
  - [ ] Unfortunatly I ran into significant trouble trying to divide out the three threads into thier own file apart from main, with variables not passing themselves over and between the threads correctly, so for now the threethreads.py file is nonfuctional, instead the three threads are located within main.py
```
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
```
- [ ] Initial plugin setup to publish to local filesystem
  - [ ] I eventually got the basic plugin to run without errors, but ran into problems getting input to download to the directory designated by:
```
 commmand line: env PYWAGGLE_LOG_DIR=/plugin-log

```
```
with Plugin() as plugin:
                        rightnow=time.time_ns()
                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                        plugin.publish("plugin.log", 1234, timestamp=rightnow)#,timestamp=rightnow)
```
![image](https://user-images.githubusercontent.com/106760508/178788373-ae196cda-59f1-4948-9360-bc2245290393.png)
- [ ] His edits during demo commited into main file
  - [ ] Removed time limit set on threads so they continue until ended by keyboard input
  - [ ] Discovered my functions are reading miliseconds instead of seconds
```
 while True:
        #while (time.time()-starttime)<total_time:
```
- [ ] Recorded unkown popup that briefly covered my screen a few occasions
![image](https://user-images.githubusercontent.com/106760508/178789956-ab9e3120-4bec-4c88-b221-6973da52c761.png)
- [ ] Got basic plugin to run without errors, but ran into problems getting input to download to directory
- [ ] Notes on plugin
  - [ ] As beehive is currently not accessible, we have to test our code via pushes to local directories,
  - [ ] Although any local file that refernces waggle.plugin can run the necessary plublish functions, the documentation to be submitted to the edge database is somewhat extensive and is to be contained on Github

Things to do:
- [ ] Get threading to work in multiple files
- [ ] Write code to improve getaverage() function to return timestamp of when output closest to average ocuured
- [ ] Add previous WisGate work to Github
- [ ] Link up local repo for easy commits
- [ ] Look into possible sources of pop up to ensure it is not part of something malicious

#### Wednesday June 15th ####
- [ ] Attended mandatory meeting on how "on the lawn" and "off the lawn" will work
- [ ] Went outside due to fire drill
- [ ] Looked into white pop-up and confirmed it is part of the gnome network connectivity manager, which continued to fail as I do not actually have gnome installed
- [ ] Talked to Sean about how to publish data from the .py file my project is in
- [ ] Successfully published an arbitrary value
```
 with Plugin() as plugin:
                        rightnow=time.time_ns()
                        #plugin.upload_file('edgeswitch.csv')#, timestamp=rightnow)
                        plugin.publish("test.bytes", 1234, timestamp=rightnow)#,timestamp=rightnow)
                #can likly use 'edgeswitch' to publish edgeswitch contents
```                
![image](https://user-images.githubusercontent.com/106760508/179076564-2bf7df2e-88c6-4d05-a012-2b132ffd4c68.png)

- [ ] Talked to Sean about my code: he reccomended not using multiple threads
- [ ] Talked to Raj, he clarified the reasoning on why we need to use different reoccurring delays for each thread,also gave me a written version of previously expressed requirements
```
This is what we need in terms of capabilities:
We should be able to read and store in memory (transient/RAM/Variables) values that we can get from the Switch. These values should ideally be in the original form they were received and in full. Don't waste resources converting, don't loose data because we did not have a clear understanding of what it could be used for. Filtering can happen later. The read rate should be definable.
We should be able to write the raw values read to Beehive using pywaggle. We should also be able to write secondary digested values based on the buffer of values we have collected in our reading and buffering process. This can happen periodically, and we should be able to set the rate.
We should be able to catch when some event happens, and report it to beehive. The latency in detecting an event is ideally less that the latency of the periodic process. I.e. We may periodically report every 5 min, our buffer may be 10 min long, read every 1 second and want to report the events ASAP ( of course there is a latency Vs Performance trade off).
After having completed a single sequential loop, design a program that can do the above.
```
- [ ] Began reforming my code aroud a List of Jsons instead of a Queue, so as to avoid potential problems stemming from how I would have to access a value within the queue by altering the queue from multiple threads and functions    

Things to do:  
- [ ] Write code to improve getaverage() function to return timestamp of when output closest to average ocuured
- [ ] Add previous WisGate work to Github
- [ ] Link up local repo for easy commits
- [ ] Complete transformation of code to safer List focussed version
- [ ] Create functionality to make a graph of changes in a given value over a time period

#### Thursday June 16th ####
- [ ]  Finished reforming project to use a large list instead of a queue
```
if len(myconfig.Listofjson)==buffer_length:#this makes the que circular might be unneeded due to maxlen(myconfig.Listofjson)
                         myconfig.Listofjson.pop(0)
                dumpedjson=json.dumps(info)
                Timestamp=statisticgetter.getTimestamp(dumpedjson)
                myconfig.Listofjson.append(( Timestamp,dumpedjson))
                            
                

```
instead of having to make a copy which I wold then edit, I could now look directly at values that were within the Listofjsons
```
def getJson(Timestamp):
        for x in range(len(myconfig.Listofjson)):
                time, json=myconfig.Listofjson[x]
                #print(time, (time-Timestamp))
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        break
        return json
```
- [ ]  Eliminated unnessary passed variables, instead referencing them within a new config file
```
def getPOEMaxes():
        Maximums =[(0,0)*myconfig.numberofports]
        for y in range(len(myconfig.Listofjson)):#I previously passed in a copy of the Que of Jsons
                print(y)
                jsonObject=myconfig.Listofjson[y]
                print('max should end')
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final, I previously stored the number of ports locally
                        poePower, time= statisticgetter.getStatistics(jsonObject,1,'poePower')
                        if poePower>Maximums[x][0]:
                                Maximums[x]=(poePower,time)
        
        return (Maximums)
```
- [ ]  Hunted down a now unneeded print that originated from a statisticsgetters function, in the process re-discovering the 'find' command
```
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        Timestamp=data[0]['timestamp']
        #print(Timestamp) #this is the offending print statement
        return(Timestamp)
```
- [ ]  Printed out a graph of poe values over the timeperiod contained within the buffer using a few new functions
```
def Getshortenedlist(firsttimestamp, secondtimestamp):
    shortlist =[]
    for i in range(len(myconfig.Listofjson)):
        timestamp, json= myconfig.Listofjson[i]
        if(timestamp>=firsttimestamp):
            shortlist.append((timestamp, json))
        if(timestamp>secondtimestamp):
            break
    return(shortlist)
def getStatisticPlot(variable, port, firsttimestamp, secondtimestamp):
    shortlist=Getshortenedlist(firsttimestamp, secondtimestamp)
    Timestamps=[0]*len(shortlist)
    Poes=[]
    values=[0]*len(shortlist)
    for x in range(len(shortlist)):
        Timestamps[x], json = shortlist[x]
        values[x], othertimestamps=statisticgetter.getStatistics(json,port,variable)
    print(Timestamps)
    print(values)
    plt.plot(Timestamps, values)
    plt.xlabel('Timestamps')
    plt.ylabel('variable')
    plt.title('variable Vs Time')
    plt.show()
def getPlotofbufferStatistic(variable, port):
    Listoftimestamps=getlisttimestamps()
    firsttimestamp=Listoftimestamps[0]
    lasttimestamp=Listoftimestamps[-1]
    getStatisticPlot(variable, port, firsttimestamp, lasttimestamp)
def getlisttimestamps():
        Timestamps= [0 for i in range(len(myconfig.Listofjson))]
        for x in range(len(myconfig.Listofjson)):
                Timestamps[x], json = myconfig.Listofjson[x]
        return (Timestamps)
```
here is an example plot of the change in poe power draw from a dummy device over 29 iterations, which repersents roughly a 1 minute 
![image](https://user-images.githubusercontent.com/106760508/179082793-b77a4f80-8952-4a3a-af89-80c9af90f51e.png)

Things to do: 
- [ ] Write code to improve getaverage() function to return timestamp of when output closest to average ocuured
- [ ] Add previous WisGate work to Github
- [ ] Link up local repo for easy commits

#### Friday June 17th ####
- [ ] 

Things to do:
- [ ] 




