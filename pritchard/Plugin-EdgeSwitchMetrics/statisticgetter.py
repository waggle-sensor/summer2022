import json
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
def getProcessorUsage(jsonObject):
        data=json.loads(jsonObject)
        ProcessorUsage=data[0]['device']['cpu'][0]['usage'] #second zero might be cpu
        return(ProcessorUsage,data[0]['timestamp'])
def getUptime(jsonObject):
        data=json.loads(jsonObject)
        Uptime=data[0]['device']['uptime']
        return(Uptime,data[0]['timestamp'])
def getTimestamp(jsonObject):
        data=json.loads(jsonObject)
        print('gettingtimestamp')
        Timestamp=data[0]['timestamp']
        return(Timestamp)