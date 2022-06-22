# Zoe Snead Daily Activity Log  
My daily activity! Most recent additions are at the top  
  
## Week 2: 6/20 to 6/24
### Wednesday 6/22
- Found a couple methods to control and talk to EVBs
  - Python window automation library and TeraTerm GUI
  - looking into ModemManager (mmcli)
- Got a loaner laptop to use to interface with modems and servers 
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
