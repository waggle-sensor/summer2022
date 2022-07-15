import queue
import matplotlib.pyplot as plt
import myconfig
import statisticgetter
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
    #print(Timestamps)
    #print(values)
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

def getJson(Timestamp):
        for x in range(len(myconfig.Listofjson)):
                time, json=myconfig.Listofjson[x]
                #print(time, (time-Timestamp))
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        break
        return json


def getPOEAverages():
        #Averages = [0] * numberofports
        #Averages= [0.0 for i in range(numberofports)]
        Averages =[(0,0)*myconfig.numberofports]# error creates (0, 0, 0, 0, 0, 0)
        #print (type(Averages[0]))
        for y in range(len(myconfig.Listofjson)):
                time, jsonObject=myconfig.Listofjson[y]
              
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final
                        poePower, time = statisticgetter.getStatistics(jsonObject,1,'poePower')
                        temp =Averages[x][0]+(poePower-Averages[x][0])/(y+1) #rolling average calculation
                        Averages[x]=(temp, time)
        return (Averages)                       
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
def getPOEMins():  
        #timestamps = [0] * 8#not sure how to initialize list of timestamps
        Minimums =[(150,0)*myconfig.numberofports]
        #Minimums = [0] * 8
        #Minimums = [150 for i in range(8)]#assumes that no port will have a higher minimum then 150 watts
        for y in range(len(myconfig.Listofjson)):
                jsonObject=myconfig.Listofjson[y]
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final
                        poePower, time= statisticgetter.getStatistics(jsonObject,1,'poePower')
                        if poePower<Minimums[x][0]: #compars and sets maximums and mins per port
                                Minimums[x]=(poePower,time)                    
        return (Minimums)
'''''
def getonoff(Listofjson): #there is o logic flaw in here that only takes note of the first time the value of isonrecent is changed
        onoff =[(True,time.time())]
        isoncurrent =  [False for i in range(numberofports)] 
        isonrecent =  [False for i in range(numberofports)]
        for y in range(buffer_len(myconfig.Listofjson)):
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
