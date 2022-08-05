# Zoe Snead Daily Activity Log  
My daily activity! Thoughts, questions, quick links. Most recent additions are at the top <3

## Week 8: 8/1 to 8/5

### Thursday 8/3

- Met with Raj and tried connecting again to 5G using his phone SIM card
  - succesfuly connects to 4G, speeds are meh
  - you can force the modem to only work on 5G but then it just disconnects
  - using `sudo qmicli -d /dev/cdc-wan0 --device-open-proxy --nas-get-signal-info` it will list the connection speeds for 4G and 5G. It shows it can check the quality of the 5G signal but for some reason can't connect to that signal
  - we saw that we were connected to LTE band 30, which isn't anywhere near the possible overlap between 4G and 5G
  - Raj is going to put the SIM card back in his phone and try to see wat 5G band his phone connects to because his phone can definitely connect
  - Raj thinks there might be some firmware update we could put onto the modem, if the modem is the problem (maybe?)  
- Returned older blue modem to 446

- Write-Up/White Paper Goals:
  - Detail what we have tried regarding connecting to 4G/5G and what has and hasn't worked. A what-not-to-do is just as valuable as a what-to-do
  - list helpful debugging tips and things to try
  - Explain 5G Core Decision Matrix  

### Wednesday 8/3

- I got the NX to register the device so it can set up the ttyUSB connection, but now it's having trouble with data overruns (the buffer fills with new information before it can read what it has)
  - Raj is going to see if we can update the the NX system. No success there today, but we might be able to try again Thursday?
- updated the [decision matrix](https://github.com/waggle-sensor/summer2022/blob/main/snead/5GCoreDecisionMatrix_8-3-2022.pdf) with new information
- Using Raj's 5G enabled phone SIM, we were able to connect the modem and computer (just regular Linux laptop) to 4G!!
  - you have to send the modem an AT command `AT+CGDCONT?` and replace it's initial bearer APN (initial bearer is listed in the `mmcli` output)
  - might try tomorrow to go off campus and connect to 5G, because apparently the SIM cards I've been using aren't 5G equipped even though we were told they were? booo

#### To Do

- downlink, I think the lab is almost ready?
- start on whitepaper
- update the NX and try to get it connecting to the modem
- take the old blue modem back to the lab and plug it back into the server
- go off campus with 5G enabled SIM and try to connect

### Monday 8/1 and Tuesday 8/2

- Very frustrating, I have spent these past two days trying to figure out why the Nano drops its connection with the modem after connecting
  - it was a problem with the ModemManager driver, since the nano runs on Ubuntu 18.04, the mmcli was out of date. Follow this [link](https://launchpad.net/~aleksander-m/+archive/ubuntu/modemmanager-bionic) to get a PPA that's a newer versionn (not the newest but still)
  - problems: the driver isn't the most up to date, so qmicli doesn't work, but that is manageable
  - connection is extremely slow over 4G (~1Mbps uploads and downloads), whereas on my laptop it is extremely fast (100 Mbps upload and 200 Mbps download)
- Raj set me up with a Jetson NX to try the same thing
  - can't get the computer to establish a ttyUSB connection 

## Week 7: 7/25 to 7/29

### Friday 7/29

- Went to lab, radios are installed, but something is wrong with the radio SFP, so that will need to be worked by the fiber guys :(
- The problem was with the SIM card, it was older than we thought and it had been deactivated
- Got a new SIM card that can connect to 4G!
  - I scanned the networks around Argonne and outside of Argonne (in a Starbucks) and did not find any 5G signals, so will have to wait until our core is back up to work with that
  - I can access the internet and ping my phone using the modem, but cannot ping Ziad's computer
  - I tried connecting the modem to the Nano, and it kept losing connection to the modem. Not just a faltering connection to 4G, but to the modem itself. I want to bring this up with Raj/Joaquin. I have a feeling this Nano can only handle 3G data? Based on the network set up wizard...

#### To Do

- Troubleshoot connecting with the Nano (computer can do fine)
- maybe write up a how-to type guide on how I would troubleshoot connecting to 5G? Because we are getting close to the end of the internship and  haven't been able to do that yet
- all other compounding To Do's

### Thursday 7/28

- Went to starbucks in the morning to try connecting to the modem, still no luck. It could be an issue with the home network not being present, maybe the SIM card, or maybe an OS problem. I don't think it's a problem with the modem because it talks and responds properly, it's just a matter of not being able to connect the computer to the data of the modem. Doesn't work on Windows or Linux, so I don't think it's the OS but still...
  - SIM Card's home network is AT&T with MCCMNC=310170, but that network isn't present in network scans  

### Wednesday 7/27

- issues connecting to the LTE served by the Telit modems. Raj and I tried mmcli, qmicli, and a couple other things. it doesn't connect to my Linux computer, the nano, nor my Windows computer
  - When I tried connecting via Windows, I ran a troubleshooting wizard and it says that there's just no service to connect to

#### To Do

- first thing tomorrow I am going to drive out of Argonne campus and try to connect from a starbucks or something to see if no service truly is the issue. I don't know what to do after that... more help on forums I guess
- All previous To Dos...

### Tuesday 7/26

- Met with Raj to sort out project plans
  - Gave me an Edge AI Device that Waggle runs on so I can try connecting it to the Telit modem
  - Gave me an AT&T SIM card so I can connect to that 5G network rather than to our own (will have to leave Argonne campus to connect). This way I can still run tests that we can use to verify our own 5G network if that construction finishes up
  - He's talking with Argonne tech about giving us access to the internet
- Getting my Telit modem from the lab to start testing that ^^ 

#### To Do

- previous unresolved to dos
- ask Raj about AT&T config settings

### Monday 7/25

- Met with Joaquin to check in about progress
  - it's looking like a demonstration of information flow from a Waggle Node over 5G is not going to be possible given the delays with the fiber installation, so we might look into other avenues for research
  - asking Raj about the Waggle desktop, seeing if doing something with that would be possible
- finished looking into UPF implementation and edge computing in 5G cores
  - ONAP and SD-Core seem to be the only ones with current ability to support edge computing (ONAP a little vague on that front)
  - Magma has plans for it in the future

#### To Do

- email ONAP, ask about hardware scaling and possible their ability to support EC
- update decision matrix to include EC info and R&D interest 
- maybe start on white paper? would basically be the decision matrix then an explanation of each of it's boxes
- next monday's check in we'll ask about other things I can do with my last two weeks

## Week 6: 7/18 to 7/22

- in and out of ability to work due to COVID
- added info about contributors and members of each 5G core, I'm unsure how to tell which is biggest in the R&D community
  - [NSF](https://www.prnewswire.com/news-releases/national-science-foundation-funded-platforms-for-advanced-wireless-research-project-office-announces-launch-of-openairx-labs-oax-to-accelerate-development-and-testing-of-an-open-source-5g-standalone-software-stack-301304723.html) has partnered with OAI????
- started looking into edge computing abilities of each 5G core org

#### To Do

- contact ONAP
- Research how they implement UPF to check for edge computing ability
- what is the biggest R&D group in NSF community

## Week 5: 7/11 to 7/15

### Friday 7/15

- had meeting with advisors about 5G decision matrix
  - we (Raj) are going to reach out to other organization that have O-RAN running to set up calls
  - I sent a list of questions I would have for those orgs if they have 5G cores
  - Seems like our best bet is to move forward with ONAP

#### To Do

- Email someone at ONAP and ask if we could scale down their hardware requirements, also ask what deployment would look like, etc.
- downlink, debug, etc.
- Nokia DAC

### Wednesay 7/13 & Thursday 7/14

- out with COVID-19

### Tuesday 7/12
- finished current version of [decision matrix](https://github.com/waggle-sensor/summer2022/blob/main/snead/5GCoreDecisionMatrix_7-12-2022.pdf)
  - setting up a meeting with Very Important People (just Raj, Randy, and Joaquin) to discuss!
- Also found out OAI has another project group that manages their core network, so that changes some things (it's still not as ready in my opinion)
  - added that information to the 5G core notes file

#### To Do
- one of these days we'll downlink and debug Linux, but the lab is indefinitely under construction sooo
- Get in person help with logging into/getting access to the Nokia DAC
- meet with people about decision matrix and get next steps, if needed

### Monday 7/11

- Met with Joaquin to check in on decision matrix
  - Need to add a row about simulated UE/RAN that each core has used
  - find use cases of them connecting real hardware, especially with Nokia products
  - go back and check if Magma has closed-loop control and double check hardware requirements
  - double check that I can delete the OAI column

#### To Do

- implement decision matrix notes and email Raj, Joaquin, and Randy when finished to set up meeting to discuss!
- downlink, debug Linux
- Get in person help with logging into/getting access to the Nokia DAC

## Week 4: 7/5 to 7/8

### Friday 7/8

- Went to Wavelabs' monthly 5G Magma update meeting
  - Magma core is implemented in GenXComm's 5G testbed and it was _**shown to work with commercial gNBs and UEs**_ (I think they were using Samsung UEs, unsure about the brand of gNB)
  - Demo-ed a Docker containerized version of their Access Gateway, which is not yet ready for release, but is on their GitHub
    - Showed the Docker AGW being connected through the Orch8r portal, then connected a gNB/UE simulator to that AGW
  - Showed other features that will be part of the current 1.8 release
- I wanna say the decision matrix is ready for feedback?
- Went through Linux-Telit manual and I have some [ideas for debugging](https://github.com/waggle-sensor/summer2022/blob/main/snead/README.md#linux-and-telit) our shotty connection to the modules

#### To Do

- .....downlink :) I'm especially thinking about the SIM cards that can't connect to our computers. They are assigned an IP address, but the computer isn't connected to the cellular network, so what would downlinking do?
- also as soon as our lab is functional, would love to try connecting to Linux again
- get feedback on 5G core decision matrix

### Thursday 7/7

- Tried logging into Nokia DAC and I get rejected
  - I am working from home this week so I will try it again on the Argonne WiFi and see
- Checked the RAN and UE connection methods for each 5G core (this took longer than expected, documentation is a little convoluted)
  - Magma and OAI seem to rely exclusively on their internal RANs, and I'm unsure if you can connect your own COTS systems. Magma talks about 3GPP compliance a lot
- Working on decision matrix, almost finished with rough draft??
- Added glossary to 5G research page

#### To Do
- doooowwwnliiinnk
- Try Nokia DAC on Monday
- Talk to Joaquin about rough draft of decision matrix

### Wednesday 7/6

- researched [Magma core](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#magma)
  - meant to interface with existing 4G systems, would need to work with 3rd party developer to use the architecture for 5G
  - the 3rd party isn't as developed as other 5G cores
  - extensive documentation, though!
- researched [OAI 5G CN](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#open-air-interface-5g-core-network)
  - little to no documentation
  - not all 5G functions are developed yet
  - would not recommend
- started on comparison matrix, very much a WIP
  - thinking about what charcteristics/features should be prioritized, maybe want two matricies? One for logistics end and one for cool features and capabilities?
- started looking into the specifics of how these cores will talk to pre-existing RAN, needs more research
- There are almost literally no user reviews of these cores, we will have to go on inflated org. language alone

#### To Do

- daily reminder to try downlinking...... _soon..._
- look into 3GPP interface between core and RAN
- continue on comparison matrix and discuss the rough draft with Joaquin
- Log into Nokia DAC OSS

### Tuesday 7/5
- morning!
- Joaquin is checking in with Nokia about the phones and Linux. Radios are down, not sure when I'll get back into the lab
- Aether is if you want to run your own mobile core as a service, but its component, SD-Core, can be run independently as a 5G/4G Core
- Met with Joaquin to check in about core research, new ToDos!
- Gathered more info on free5GC and 
#### To Do
- Downlink!!! When in the lab!! Eventually! Radios are down!
- [Open5GCore](https://www.open5gcore.org/) as another avenue to look into for Core research? Just kidding it's not open source
- [Open Air Interface 5G CN](https://openairinterface.org/oai-5g-core-network-project/)
- [Magma](https://magmacore.org/learn-the-technology/)
- Maybe look and find public reviews of each? Get some unbiased descriptions/information on each organization
- free5GC is dev'ed by china, will we want to pursure that?
- prepare a matrix of options vs their features
  - make sure to include price points
  - maybe who it's developed by? Linux Foundation for Magma and ONAP
- what is the 3GPP interface to communicate btwn core and RAN?
- Nokia RAN thing from Joaquin

## Week 3: 6/27 to 7/1
### Friday 7/1
- Went to Active Shooter training... not a fan...
- Started researching [Aether](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#aether-onf)
  - looks like it uses the free5GC 5G base to build something as extensive as ONAP, if not more extensive. I'm not sure if we need something this big?
- Looked into .NET for fun! (at Billy Kihei's suggestion)
- found [gNB Simulator](https://docs.sd-core.opennetworking.org/master/developer/gnbsim.html) hosted by ONF
#### To Do
- Talk with Jaoquin about 5G core research to gain more direction
- Research more on Kubernetes and understand our current setup
- Continue getting into Aether/SD-Core functionality. Still haven't found how to install it...
- try downlinking in the lab!

### Thursday 6/30
- Researched free5GC, check out the [notes!](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#free5gc)
  - seems more lean, and less robust than ONAP, but just as accessible
  - the software itself is free, but the technical support is behind a membership paywall
  - not too many services, and no network slicing
  - has a backlog of versions that are non-standalone, standalone, and fully 5G depending on our infrastructure needs
- Found [UERANSIM](https://github.com/aligungr/UERANSIM) which could simulate a 5G phone and base station if core testing needed
- Helped give Randy Berry a tour of our lab
- I was able to connect my Linux computer to the modem that got a ping on [6/22](https://github.com/waggle-sensor/summer2022/blob/main/snead/daily_log.md#wednesday-622) but ONLY this modem. Are you only able to connect to *one* modem from your Linux system? Still doesn't explain the 5g phones being unable to connect. My ModemManager was able to talk to it, but the mobile network couldn't connect... ( ._.)
#### To Do
- Look into Aether (ONF) and other open source cores
- Dive deeper with free5GC
- Research more on Kubernetes and understand our current setup
- Try to downlink from the server to a modem if we're in the lab tomorrow (randy's idea!) Can you downlink to the modem when the computer is not connected?
  - How do we know the packets aer transmitting over 5G? When we get it up and running, I guess...

### Wednesday 6/29
- Career day!! Figured out how to play Carcassonne, did NOT figure out how to kayak properly

### Tuesday 6/28
- Researched ONAP ([README Notes](https://github.com/waggle-sensor/summer2022/tree/main/snead#onap))
  - Developed understanding of their 5G Core architecture and made notes
  - Found specific plug-in that would allow control of our COTS radios
  - Depending on the hardware we have and where we want to host this core, it seems pretty plug-and-play
#### To Do 
- Research more on Kubernetes and understand our current setup (the Waggle Nodes already run using Kubernetes, right?)
- Look into other OpenSource 5G setups, like free5GC or Aether (ONF)

### Monday 6/27
- Met with Dr. Kihei and his associates (Mfon and Luanne)
  - Discussed Vehicle to Vehicle capabilities of 5G with Mfon
  - Ran some tests with their Python [5G Tool Kit](https://github.com/Intelligent-Mobile-Device-Lab-at-KSU/5gtoolkit)
    - We were achieving typical speeds with UE to UE communication (~40-50ms delays)
    - Jitter test had very low delays because we are alone on our network (~5ms)
  - Tried running their [Latency Tools](https://github.com/Intelligent-Mobile-Device-Lab-at-KSU/wireless_latency_tools) but the read outs were not making sense
- Installed and started configuring the Blade Edge Server
#### To Do
- No access to the lab tomorrow, begin looking into opensource 5G technology 

## Week 2: 6/20 to 6/24
### Friday 6/24
- happy friday!! I forgot to bring my tea
- trying to run Waggle stack
- Testing connectivity of modem
  - we are shut out of WiFi connectivity
  - something is wrong and our Linux computers can no longer connect to our cellular. Could have something to do with Docker?

### Thursday 6/23
- fiddled with Screen
  - it's a little finnicky to get the terminal open to send AT commands to the modem
  - use mmcli -m # to see what USB connection to call
- Picked up Blade from the 240 lab
- Starting Waggle Edge Stack deployment on loaner computer to test interface with modem
#### To Do 
- take Waggle Blade to 446 and install it
- install Waggle Edge Stack!

### Wednesday 6/22
- Found a couple methods to control and talk to EVBs
  - Python window automation library and TeraTerm GUI
  - looking into ModemManager ([mmcli](https://www.freedesktop.org/software/ModemManager/man/1.0.0/mmcli.8.html#:~:text=DESCRIPTION,different%20connection%20managers%2C%20like%20NetworkManager.))
- Got a loaner laptop to use to interface with modems and servers 
- Went to 446 lab and was able to connect modem to 4G and set up an HTTP server from the Base Station
#### To Do
- install and fiddle with Screen for Ubuntu as a means of controlling the modem
- look into Waggle Node architecture to figure how to integrate the 5G modem

### Tuesday 6/21
- Helped Ziad fiddle with connecting to and hosting servers
  - found out my personal laptop will have trouble connecting to certain servers because of Argonne's firewall
- Researched Raspberry Pi and connection to Telit EVB
- Got my Docker and DockerHub to work
#### To Do
- Look into remote control and automation of Telit

### Monday 6/20
- Went through Telit AT Commands and User Guides to find 5G configuration and diagnostic information commands. The goal is to possibly automate/attach AI to be checking in on the status of the UE to make transmission decisions
  - In terms of power consumption monitoring, an Arduino can be programmed to monitor current, but at this time unsure if that would interfere with remote controlling
  - *AT#BND:* selects band for 3G, 4G, and 5G [(command help)](https://techship.com/faq/how-to-use-atbnd-to-select-active-bands-on-telit-modules/)
  - *AT+WS46:* selects cellular network
  - *AT#5GCTL:* enable NSA FR1/FR2 and SA FR1/FR2
  - *AT+CIND?:* returns some status updates, like battery charge, signal quality, and RSSI
  - *AT+CESQ:* returns RSRQ, RSRP, and SNR for 5G signals, will give parameters for 3G and 4G if those are enabled 
  - *AT#TEMPSENS* gives current temperature and *AT#TMLVL?* gives temperature mitigation level
  - *AT#CSURV:* performs network survey, but possibly only finds 3G and 4G networks
  - *AT#TESTMODE* and *AT#MIMOSTS* are also possibly useful
  - GNSS information can give us date, time, location, and ground speed information if we want to look into that
  - Found some GPIO pin commands if we want to connect a Raspberry Pi, I2C, or possibly have analog data flow
- Met with Wildebeest team to give some updates
- Experiemented with Ziad to try to set up HTTP server
- Talked with Joaquin and Ziad about next steps for server
#### To Do
- Possibly try connecting Telit over 4G and transmit data as a tester until we get the 5G network running 

## Week 1: 6/13 to 6/17  
### Friday 6/17
- Continued learning about Linux
  - [Helpful site for learning basics] (https://linuxjourney.com/)
  - Some discussion on here about network sharing that will be useful
- Went to 446 Lab and reconnected to the 4G network
#### Next Steps
- talk to advisors about Telit manual findings
- get Telit Arduino manual and read through
- talk about bigger picture next steps!

### Thursday 6/16
- Read Telit FN980 Manuals
  - Learned HW/SW capabilities
    - Attach Arduino for remote control? (A-star 32U4 microcontroller board)
    - It's got a battery and can have GPS capabilites!
  - Learned AT Commands
- Finished 5G network courses
- Found a quick [CBRS resource](https://www.fiercewireless.com/private-wireless/what-cbrs)
- started learning more about Linux
#### To Do / Questions to be Answered
- tinker with our Telit units
  - interested in SMS capabilities, and transmitting data
  - looks like these things just function like phones, can we just use it as an antenna to pass data through
- discuss with supervisors about next steps

### Wednesday 6/15
- Set up GitHub and other needed accounts  
- Learned about Scrum and Docker
- Started LinkedIn Learning Course on 5G  
#### To Do
- Read Telit manuals :)
- finish second 5G course

### Tuesday 6/14
-  Finished TMS training
-  Toured building 446 and 485
-  Met with Raj, Joaquin, and Randy Berry to discuss project plans
-  Connected to Telit board and connected to server
#### To Do
- Learn about Scrum
- Learn about Docker
- Set up GitHub
- Read up on 5G
- Read up on Telit radio manuals

### Monday 6/13
- Went to orientation
- started TMS training 
#### To Do
- Finish TMS training
