import json
def withIndexGetter(jsonObject, index, variable):
        data=json.loads(jsonObject)
        if(variable=='name' or variable=='value' or variable=='type'):#this triggers if temperature info is requested, max index of 3
                value=data[0]['device']['temperatures'][index][variable]
                variable='temperature info'+ variable
                indexstring= 'area:'+str(index)
        else:  #variable= dropped errors txErrors rxErrors rate txRate rxRate bytes txBytes rxBytes packets txPackets rxPackets pps txPPS rxPPS poePower
              value=data[0]['interfaces'][index]['statistics'][variable]#this triggers if ports information is requested, port= 0-15
              indexstring= 'port:'+str(index+1)  
        return(variable, indexstring, value)

def noIndexGetter(jsonObject, variable):
        data=json.loads(jsonObject)
        if(variable=='timestamp'):# if the variable requested is timestamp
                value=data[0]['timestamp']
        elif(variable=='uptime'):
                value=data[0]['device']['uptime']
        elif(variable=='processor usage'):
                value=data[0]['device']['cpu'][0]['usage']
        elif(variable=='usage' or variable=='free' or variable=='total'):#if ram information is requested
                value=data[0]['device']['ram'][variable]#variable = usage, free, total
                variable='ram '+variable# this makes the requested variable clear in read out
        else:
                print("variable not correct")
        return(variable, value)

