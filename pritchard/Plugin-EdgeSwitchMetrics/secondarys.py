import queue
import matplotlib.pyplot as plt
import myconfig
import statisticgetter
import csv
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


"""
def RecordBigChanges(change): 
        with open('bigchanges.csv', 'a', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(change)


def Getshortenedlist(firsttimestamp, secondtimestamp):
    shortlist =[]
    for i in range(len(myconfig.Listofjson)):
        timestamp, json= myconfig.Listofjson[i]
        if(timestamp>=firsttimestamp):
            shortlist.append((timestamp, json))
        if(timestamp>secondtimestamp):
            break
    return(shortlist)


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
"""
def getAverages(variable):
        #Averages = [0] * numberofports
        #Averages= [0.0 for i in range(numberofports)]
        Averages =[(0,0)]*myconfig.numberofports# error creates (0, 0, 0, 0, 0, 0)
        #print (type(Averages[0]))
        for y in range(len(myconfig.Listofjson)):
                time, jsonObject=myconfig.Listofjson[y]
              
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        temp =Averages[x][0]+(value-Averages[x][0])/(y+1) #rolling average calculation
                        Averages[x]=(temp, time)#this needs to be fixed to give the closest time to when the average occured
        return (Averages, variable)
def isnormalcheck(variable, standardvalue, currentvalue):#later add in details on acceptable ratio
        if standardvalue== 0 and currentvalue==0:
                proportion=1
        elif standardvalue== 0:
                proportion= 1.5*currentvalue#this has the possibility of making a bug
        else: proportion=currentvalue/standardvalue
        if variable== 'poePower':
                if(proportion>myconfig.POEwarningproportion):
                        return(variable,"raised is now this fraction of former value:",proportion)
                elif(proportion<1/myconfig.POEwarningproportion):
                        return(variable,"dropped is now this fraction of former value:",proportion)
                else: return None
        elif variable== 'errors':
                if(proportion>myconfig.Errorwarningproportion):
                        return(variable,"raised is now this fraction of former value:",proportion)
                elif(proportion<1/myconfig.Errorwarningproportion):
                        return(variable,"dropped is now this fraction of former value:",proportion)
                else: return None
        elif variable== 'temperature':
                if(proportion>myconfig.Tempwarningproportion):
                        return(variable,"raised is now this fraction of former value:",proportion)
                elif(proportion<1/myconfig.Tempwarningproportion):
                        return(variable,"dropped is now this fraction of former value:",proportion)
                else: return None
        elif variable== 'rate':
                if(proportion>myconfig.Ratewarningproportion):
                        return(variable,"raised is now this fraction of former value:",proportion)
                elif(proportion<1/myconfig.Ratewarningproportion):
                        return(variable,"dropped is now this fraction of former value:",proportion)
                else: return None
def getMaxes(variable):
        Maximums =[(0,0)]*myconfig.numberofports
        for y in range(len(myconfig.Listofjson)):#I previously passed in a copy of the Que of Jsons
                print(y)
                time, jsonObject=myconfig.Listofjson[y]
                print('max should end')
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final, I previously stored the number of ports locally
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        if value>Maximums[x][0]:
                                Maximums[x]=(value,time)
        return (Maximums, variable)
def getMins(variable):  
        #timestamps = [0] * 8#not sure how to initialize list of timestamps
        Minimums =[(150,0)]*myconfig.numberofports
        #Minimums = [0] * 8
        #Minimums = [150 for i in range(8)]#assumes that no port will have a higher minimum then 150 watts
        for y in range(len(myconfig.Listofjson)):
                time, jsonObject=myconfig.Listofjson[y]
                for x in range(myconfig.numberofports): #iterates through each port, 8-15 in final
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        if value<Minimums[x][0]: #compars and sets maximums and mins per port
                                Minimums[x]=(value,time)                    
        return (Minimums, variable)

"""
    def getStatisticPlot(variable, index, firsttimestamp, secondtimestamp):
    shortlist=Getshortenedlist(firsttimestamp, secondtimestamp)
    Timestamps=[0]*len(shortlist)
    values=[0]*len(shortlist)
    for x in range(len(shortlist)):
        Timestamps[x], json = shortlist[x]
        values[x], othertimestamps=statisticgetter.withIndexGetter(json,index,variable)
    #print(Timestamps)
    #print(values)
    plt.plot(Timestamps, values)
    plt.xlabel('Timestamps')
    plt.ylabel('variable')
    plt.title('variable Vs Time')
    plt.show()
    
def getPlotofbufferStatistic(variable, index):
    Listoftimestamps=getlisttimestamps()
    firsttimestamp=Listoftimestamps[0]
    lasttimestamp=Listoftimestamps[-1]
    getStatisticPlot(variable, index, firsttimestamp, lasttimestamp)
    """
'''''
def getonoff(Listofjson): #there is o logic flaw in here that only takes note of the first time the value of isonrecent is changed
        onoff =[(True,time.time())]
        isoncurrent =  [False for i in range(numberofports)] 
        isonrecent =  [False for i in range(numberofports)]
        for y in range(buffer_len(myconfig.Listofjson)):
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        time, value = getStatistics(jsonObject,1,'value')
                        if value!=0:#checks to see if anything currently plugged in
                                isoncurrent[x]= True
                        else:
                                isoncurrent[x]= False
                        if y==0|isonrecent[x]!=isoncurrent[x]:#checks to make sure that either this is the first iteration or something has been unplugged/pluggedin
                                wattagerecorders[x].put(datetime.datetime.now())#stores the changes with when they occured
                                wattagerecorders[x].put(isoncurrent[x])
                                print(y)
                        isonrecent[x]=isoncurrent[x]   
  '''        
