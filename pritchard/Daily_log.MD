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

### Week 3: 6/20 to 6/24 ###
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

### Week 3: 6/27 to 6/31 ###
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


