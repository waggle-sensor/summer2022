# Daily Activity

My daily work on the NAISE 5G project 2022!


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

- first thing tomorrow I am going to drive out of Argonne campus and try to connect from a starbucks or something to see if no service truly is the issue. I don't know what to do after that... more help on orums I guess
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
## Week 3


### 25 June

- [X] Talked with Joaquin and Zoe about next steps for server
- [X] install ssh server
- [X] test ssh protocol with different users

### 26 June

- [X] install HTTP server
- [X] share multiple directories and files with different users

### 27 June

- [X] read about different file transfer protocols
- [X] read about different HTTP servers
- [X] Customized HTTP server using python

### 28 June

- [X] Install file transfer protocol using Globus
- [X] Test file sharing from multiple computers --> didn't work bec of the firewall
- [X] Install Apache2 server
- [X] Coustmize Apache2 server
- [X] Share directories and files using Apache2

### 29 June
- [X] Met with Dr. Kihei and his associates (Mfon and Luanne)
  - [X] Discussed Vehicle to Vehicle capabilities of 5G with Mfon
  - [X] Ran some tests with their Python [5G Tool Kit](https://github.com/Intelligent-Mobile-Device-Lab-at-KSU/5gtoolkit)
    - [X] We were achieving typical speeds with UE to UE communication (~40-50ms delays)
    - [X] Jitter test had very low delays because we are alone on our network (~5ms)
  - [X] Tried running their [Latency Tools](https://github.com/Intelligent-Mobile-Device-Lab-at-KSU/wireless_latency_tools) but the read outs were not making sense
- [X] Installed and started configuring the Blade Edge Server


## Week 2


### 20 June

- [X] Talked with Joaquin and Zoe about next steps for server
- [X] install ssh server
- [X] test ssh protocol with different users

### 21 June

- [X] install HTTP server
- [X] share multiple directories and files with different users

### 22 June

- [X] read about different file transfer protocols
- [X] read about different HTTP servers
- [X] Customized HTTP server using python

### 23 June

- [X] Install file transfer protocol using Globus
- [X] Test file sharing from multiple computers --> didn't work bec of the firewall
- [X] Install Apache2 server
- [X] Coustmize Apache2 server
- [X] Share directories and files using Apache2

### 24 June
- trying to run Waggle stack
- Testing connectivity of modem
  - we are shut out of WiFi connectivity
  - something is wrong and our Linux computers can no longer connect to our cellular. Could have something to do with Docker?



## Week 1


### 13 June

- [X] Attend orientation sesstion

- [X] TMS training

### 14 June
- [X] Finished TMS training

- [X] Toured building 446 and 485 to see the project base and the lab

- [X] Met with Raj, Jaoquin and Randy to discuss project plan

- [X] Setup Telit board and connected to the server

### 15 June
- [X] Set up GitHub and my drive folder

- [X] Started the 5G course on Linkedin Learning

### 16 June
- [X] Finished 5G practice course 

- [X] Learned about Linux Network Sharing, Routing and DNS commands
