def getPOEAverages(jsonqueue):
        #Averages = [0] * numberofports
        #Averages= [0.0 for i in range(numberofports)]
        Averages =[(0,0)*numberofports]# error creates (0, 0, 0, 0, 0, 0)
        #print (type(Averages[0]))
        for y in range(buffer_length):
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
        for y in range(buffer_length):
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
        for y in range(buffer_length):
                jsonObject=jsonqueue.get()
                for x in range(numberofports): #iterates through each port, 8-15 in final
                        poePower, time= getStatistics(jsonObject,1,'poePower')
                        if poePower<Minimums[x][0]: #compars and sets maximums and mins per port
                                Minimums[x]=(poePower,time)                    
        return (Minimums)
'''''
def getonoff(jsonqueue): #there is o logic flaw in here that only takes note of the first time the value of isonrecent is changed
        onoff =[(True,time.time())]
        isoncurrent =  [False for i in range(numberofports)] 
        isonrecent =  [False for i in range(numberofports)]
        for y in range(buffer_length):
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