# Zoe Snead Daily Activity Log  
My daily activity! Thoughts, questions, quick links. Most recent additions are at the top <3

## Week 4: 7/5 to 7/8

### Thursday 7/7

- Tried logging into Nokia DAC and I get rejected
  - I am working from home this week so I will try it again on the Argonne WiFi and see
- Checked the RAN and UE connection methods for each 5G core (this took longer than expected, documentation is a little convoluted)
  - Magma and OAI seem to rely exclusively on their internal RANs, and I'm unsure if you can connect your own COTS systems
- Working on decision matrix

#### To Do
- doooowwwnliiinnk
- Try Nokia DAC on Monday

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
