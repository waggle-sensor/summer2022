#import queue
#import matplotlib.pyplot as plt
import myconfig
import statisticgetter
#import time
"""getter functions for reference
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
#many of these functions rely on the buffer being passed to them, if the project expanded to require these functions it would be best to move the buffer created in Trigger to myconfig

def Getshortenedlist(firsttimestamp, secondtimestamp, buffer):
    shortlist =[]
    for i in range(len(buffer)):
        timestamp, json= buffer[i]
        if(timestamp>=firsttimestamp):
            shortlist.append((timestamp, json))
        if(timestamp>secondtimestamp):
            break
    return(shortlist)


def getlisttimestamps(buffer):
        Timestamps= [0 for i in range(len(buffer))]
        for x in range(len(buffer)):
                Timestamps[x], json = buffer[x]
        return (Timestamps)

def getJson(Timestamp,buffer):
        for x in range(len(buffer)):
                time, json=buffer[x]
                if time>=Timestamp:#returns if timestamp is equal or has already been passed by iteration
                        break
        return json

def isnormalcheck(variable, index, currentvalue):
        lowerboundary, upperboundary=myconfig.variableboundaries[index][variable]
        if(currentvalue>upperboundary):
                return("High")
        elif(currentvalue<lowerboundary):
                return("Low")
        else: return(None)

def getAverages(variable,buffer):
        Averages =[(0,0) for i in range(myconfig.numberofports)]
        for y in range(len(buffer)):
                time, jsonObject=buffer[y]
              
                for x in range(myconfig.numberofports): #iterates through each port, 8 currently
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        temp =Averages[x][0]+(value-Averages[x][0])/(y+1) #rolling average calculation
                        Averages[x]=(temp, time)#this can be fixed to give the closest time to when the average occured
        return (Averages, variable)

def getMaxes(variable,buffer):
        Maximums =[(0,0) for i in range(myconfig.numberofports)]
        for y in range(len(buffer)):
                print(y)
                time, jsonObject=buffer[y]
                for x in range(myconfig.numberofports): #iterates through each port, 8 currently
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        if value>Maximums[x][0]:
                                Maximums[x]=(value,time)
        return (Maximums, variable)
def getMins(variable,buffer):  
        Minimums =[(150,0) for i in range(myconfig.numberofports)]
        for y in range(len(buffer)):
                time, jsonObject=buffer[y]
                for x in range(myconfig.numberofports): #iterates through each port, 8 currently
                        variable, indexstring, value= statisticgetter.withIndexGetter(jsonObject,x,variable)
                        if value<Minimums[x][0]: #compars and sets maximums and mins per port
                                Minimums[x]=(value,time)                    
        return (Minimums, variable)

def isproportionalcheck(variable, standardvalue, currentvalue):#due to implementation change related config variables no longer exist
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

#relies on commented library
def getStatisticPlot(variable, index, firsttimestamp, secondtimestamp, buffer):
    shortlist=Getshortenedlist(firsttimestamp, secondtimestamp,buffer)
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
    
def getPlotofbufferStatistic(variable, index, buffer):
    Listoftimestamps=getlisttimestamps(buffer)
    firsttimestamp=Listoftimestamps[0]
    lasttimestamp=Listoftimestamps[-1]
    getStatisticPlot(variable, index, firsttimestamp, lasttimestamp,buffer)
