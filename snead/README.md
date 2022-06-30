# Welcome to my README! 
My hope is to make this a useful resource (mostly for me to reference) of the things I've learned so far! My focus is on the client side of the network, so verifying that the Waggle Nodes can connect and transmit data over the network, so my information is mostly relevant to that. A loootta Telit manual stuff so far :)
# Project Goals
**Overall Objective:** To demonstrate a real scientific workflow using a Waggle node connected via 5G CBRS to an Edge Computing resource.

**Specific Tasks:**

1. Verify connectivity between Argonne’s private 5G CBRS network and user equipment (UE) modems attached to Waggle nodes:
    1. Verify connectivity from Waggle node to the 5G core
    2. Verify direct connectivity between Waggle nodes over 5G
2. Integrate Waggle nodes on Argonne’s 5G network with Edge Computing resources and show demo.
3. Investigate how to deploy a 5G CBRS private network using open source 5G core and commercial off the shelf (COTS) radios.
4. Other tasks:
    1. Conduct Spectrum surveys using a 5G-capable smartphone and the [SigCap app](https://people.cs.uchicago.edu/~muhiqbalcr/sigcap/)
    2. Investigate Argonne’s UE modem capabilities for Spectrum sensing
    3. Collaborate on CBRS access channel techniques development

# Telit FN980m Information
This is the module we are using to eventually connect our Waggle Nodes to the 5G network. They kind of act like cell phones -they can send and recieve calls and SMS- and we will mainly use them like a phone putting up a hotspot. It's a pretty versatile little machine!
## Helpful AT Commands
This section will not tell you the full functionality of the commands, but instead serves as a culled down list of relevant commands. Use this in conjunction with the Telit AT Command manual (not sure if it's kosher to link that here)
- **AT#BND** selects band for 3G, 4G, and 5G [(command help)](https://techship.com/faq/how-to-use-atbnd-to-select-active-bands-on-telit-modules/)
  - I've actually found there isn't much flexibility for choosing a band for our Telit module. Instead can be used to see what bands are allowed
- **AT#LTEDS** second returned argument gives current LTE band number
- **AT#5GLINKSTAT?** will show if connected to 5G (3rd returned argument is 2 if connected)
- **AT+WS46** selects cellular network 
- **AT#5GCTL** enable NSA FR1/FR2 and SA FR1/FR2 
- **AT+CIND?** returns some status updates, like battery charge, signal quality, and RSSI 
- **AT+CESQ** returns RSRQ, RSRP, and SNR for 5G signals, will give parameters for 3G and 4G if those are enabled 
  - **AT#CAINFO** returns like, every possible parameter possible and is a little hard to read, but could be useful
- **AT#TEMPSENS** gives current temperature and **AT#TMLVL?** gives temperature mitigation level 
- **AT#CSURV** performs network survey, but possibly only finds 3G and 4G networks 
- **AT#TESTMODE** and **AT#MIMOSTS** are also possibly useful 
## Some EVB interests of mine
  - Use Arduino to remotely control the EVB
    - Looks like standard 20-pin connection
  - GNSS information can give us date, time, location, and ground speed information
  - Found some GPIO pin commands if we want to connect a Raspberry Pi, I2C, or possibly have analog data flow
  - Audio input, looks like mainly so you can "call" other devices, but who knows!

# 5G Core Information

## ONAP
"Open Network Automation Platform (ONAP) is an open source project hosted by the Linux Foundation. ONAP provides a comprehensive platform for real-time, policy-driven service orchestration and automation. ONAP enables service providers and developers to rapidly automate the instantiation and configuration of physical and virtual network functions and to support complete life cycle management activities." \- [ONAP](https://docs.onap.org/en/honolulu/index.html)

[ONAP Home Page](https://www.onap.org/)

[ONAP Documentation](https://docs.onap.org/en/honolulu/index.html#)
### Architecture Notes
![ONAP-Notes](https://user-images.githubusercontent.com/107580325/176268551-013da326-381a-4dad-b308-e67f7bfd19b1.png "ONAP Architecture")

All pictures and information compiled from [ONAP's Architecture page](https://docs.onap.org/en/honolulu/guides/onap-developer/architecture/index.html)

### Integrating COTS Radios
So far it looks like mmWave Radios and our equipment can be controlled using an ONAP's SDN controller for ‘Radio’ (SDN-R), an additional service you can integrate into the run-time model. It's a part of their ONAP component, SDN-Controller. Once set up, the user could open the SDN-R portal and see which devices are connected (and manually mount radios, if needed). 

![image](https://user-images.githubusercontent.com/107580325/176289800-2dbdf6bd-9397-4a30-9d91-4cc5e908bf1d.png)

Image from [ONAP SDN-R Documentation](https://docs.onap.org/projects/onap-ccsdk-features/en/honolulu/guides/onap-user/home.html)

### Pros/Advantages
- Portal function makes interacting with ONAP system more accessible
- Robust with community and ONAP created plugins and services
- A wealth of direct how-to guides (mostly focuses on initial set up) and documentation
- Use of Kubernetes and Docker containers already present in Waggle community
### Cons/Challenges
- Can't find much evidence of user support, ie contact a developer to get help
- One-time-pay [eLearning course](https://training.linuxfoundation.org/training/onap-fundamentals/) on specifics of how to use and interact with ONAP 

## free5GC
An opensource 5G Core that can be used commercially without any licensing. To gain access to training, seminars, and tech support you must pay for [membership](https://www.free5gc.org/membership/)

[free5GC Home Page](https://www.free5gc.org/)
### Versions
free5GC was developed in different stages, and offers each stage as an independent download. Information compiled from free5GC's [roadmap](https://www.free5gc.org/roadmap/)
#### Stage 1: Non-Standalone 5G
Based on 4G EPC architecture, with migrated 5G interfaces. This stage was developed when 5G UE and gNB hardware was not yet on the market, so it goes through and communicates with 4G UE and eNB. Architecture below:

<img src="https://user-images.githubusercontent.com/107580325/176721996-1af7fae7-facc-4371-9903-41fc0cd4c8fb.png" width="625" height="250">

#### Stage 2: Standalone 5G
In the standalone architecture, network functions became 5G based
#### Stage 3: 

### Pros/Advantages
- Access to different versions in varying stages of 5G integration could be useful as Waggle begins migration to 5G
### Cons/Challenges
- Pay wall for training, but that's not too unique

## Helpful 5GC Resources
- [UERANSIM](https://github.com/aligungr/UERANSIM) is a simulator that acts as a 5G mobile phone and base station to test 5G Cores 
- Explanation of [5G Core Architecture](https://www.digi.com/blog/post/5g-network-architecture)
- Quick dicussion of [PNF and VFN](https://www.linkedin.com/pulse/technology-analogy-physical-virtual-network-functions-milind-kulkarni/)

# Other helpful links
- [Linux learning help](https://linuxjourney.com/)
- Quick [CBRS Resource](https://www.fiercewireless.com/private-wireless/what-cbrs)
- [Docker basics explanation](https://yannmjl.medium.com/what-is-docker-in-simple-english-a24e8136b90b#:~:text=Docker%20is%20a%20tool%20designed,all%20out%20as%20one%20package.)
- Raspberry Pi [GPIO](https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html)
- Python window automater [pywinauto](https://pywinauto.readthedocs.io/en/latest/getting_started.html)
