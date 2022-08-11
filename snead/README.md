# Welcome to my README! 

My hope is to make this a useful resource of the things I've learned so no one has to wade through the murky waters of Telit modem troubleshooting and opensource 5G documentation again! My focus is on the client side of the network, so verifying that the Waggle Nodes can connect and transmit data over the network, and the core side of a network. 

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

# Connecting Waggle Nodes to 5G Network

Most of the work done to gather information about this task was using a commercial network while the ANL Nokia network was down due to construction. My goal, therefore, is to provide all relevant information I encountered while working to create a roadmap and debugging guide for the next person who is trying to connect to the ANL network. May the 5G gods be on their side.

[How to Connect to a Network](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md)

[Common Problems and Solution Ideas](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/Debugging.md)

[Current Issues and Ideas to Fix](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/UnsolvedIssues.md)

# Telit FN980m Information

This is the module we are using to eventually connect our Waggle Nodes to the 5G network. They kind of act like cell phones -they can send and recieve calls and SMS- and we will mainly use them like a phone putting up a hotspot. It's a pretty versatile little machine! Kinda clunky though...

## Helpful AT Commands

This section will not tell you the full functionality of the commands, but instead serves as a culled down list of relevant commands. Use this in conjunction with the Telit AT Command manual (search online to easily find it).
- `AT+CGDCONT?` will let you define the PDP (Packet Data Protocol) context; basically, you can set the initial bearer APN, which is essential to getting the modem to connect
    - `AT+CGDCONT= 1,"IP","[insert APN here]"` will change the APN
-  `AT#BND` selects band for 3G, 4G, and 5G [(command help)](https://techship.com/faq/how-to-use-atbnd-to-select-active-bands-on-telit-modules/)
    - I've actually found there isn't much flexibility for choosing a band for our Telit module. Instead can be used to see what bands are allowed
- `AT#LTEDS` second returned argument gives current LTE band number
- `AT#5GLINKSTAT?` will show if connected to 5G (3rd returned argument is 2 if connected, 1 if only LTE)
- `AT+WS46` selects cellular network 
- `AT#5GCTL` enable NSA FR1/FR2 and SA FR1/FR2 
- `AT+CIND?` returns some status updates, like battery charge, signal quality, and RSSI 
- `AT+CESQ` returns RSRQ, RSRP, and SNR for 5G signals, will give parameters for 3G and 4G if those are enabled 
  - `AT#CAINFO` returns every parameter possible and is a little hard to read, but could be useful
- `AT#TEMPSENS` gives current temperature and **AT#TMLVL?** gives temperature mitigation level 
- `AT#CSURV` performs network survey, but possibly only finds 3G and 4G networks 
- `AT#TESTMODE` and `AT#MIMOSTS` are also possibly useful 

## Linux and Telit

As of 6/24 we've been having trouble connected the modems to Linux running computers, so here's some information about how that interface works and ideas I have on how to debug that problem!

### Information
- Our Telit modules support the following USB compositions for Linux. The default is 0x1050. The modems are of the reduced Abstract Control Model (ACM)
    - <img src="https://user-images.githubusercontent.com/107580325/178064067-58db0cbd-9ec0-43e1-aa05-32ae9b29442d.png" height="100" width="400"> <img src="https://user-images.githubusercontent.com/107580325/178064285-a0481560-6d87-4eb5-99be-c710da8ebd95.png" height="100" width="400">
    - `mmcli` allows you to see these ports
    - <img src="https://user-images.githubusercontent.com/107580325/178070156-96091343-7972-4d82-bea0-3d2dc66a956f.png" height="100" width="600">
- The kernel module `option` is our control interface for USB
    - this means the device created when the Telit is connected is `/dev/ttyUSBx` where 'x' is the port number (usually 2 or 3)
    - > "These are Linux character devices and support most of the features implemented by the tty layer: for example a terminal emulator like minicom can be used to send AT commands.When writing code for using these devices, please refer to the programming language API related to character devices. As an example, C applications can use the exported functions in the system header files fcntl.h and unistd.h." - from Telit Linux User Guide

### Debug Ideas

- use [this ACM doc page](https://docs.kernel.org/usb/authorization.html) to check if new Telit modems are authorized for communication
- Check kernel version is up-to-date to run [`option`](https://superuser.com/questions/691271/what-does-modprobe-option-do)
    - <img src="https://user-images.githubusercontent.com/107580325/178068703-6fe4c3bf-ab7a-4596-aa64-03fcd02bfa58.png" height="200" width="400">
    - might need to [rebuild kernel](https://www.olimex.com/forum/index.php?topic=558.0) if option isn't there?
- We might be able to use [libqmi project](https://gitlab.freedesktop.org/mobile-broadband/libqmi) to talk to the modem, but I'm doubtful
- Is there a way to force the network manager wizard to open?
    - `nmcli c` shows what is currently connected, `nmcli d` shows current devices 
    - maybe use [`nmcli`](https://developer-old.gnome.org/NetworkManager/stable/nmcli-examples.html#:~:text=nmcli%20is%20a%20command%2Dline,and%20usage%20scenarios%20of%20nmcli.) to do this
- Maybe look into [rmnet](https://www.kernel.org/doc/html/v5.8/networking/device_drivers/qualcomm/rmnet.html)?


## Some EVB interests of mine

  - Use Arduino to remotely control the EVB
    - Looks like standard 20-pin connection
    - Arduino would be able to remotely turn off and on the modem, and manage battery life
  - GNSS information can give us date, time, location, and ground speed information
  - Found some GPIO pin commands if we want to connect a Raspberry Pi, I2C, or possibly have analog data flow
  - Audio input, looks like mainly so you can "call" other devices, but who knows!

# 5G Core Information
As part of my goals for the summer listed above, I am researching different organizations that provide open source 5G Core systems. This information is mostly compiled from the public websites and documentation of the organizations. So far I have researched ONAP, free5GC, Aether/SD-Core (ONF), Magma, and Open Air Interface Mosaic5G & 5G CN. Most of these packages seem to be able to be installed and implemented without charge or restriction, but training or tech support is behind a paywall. Go to my [5G Core notes](https://docs.google.com/document/d/12ElTunqGXwKTZYK72Wg4wYXHZw6AQMQFqlVDyauiI1I/edit?usp=sharing) to read more specifics!

Here is the current [decision matrix](https://github.com/waggle-sensor/summer2022/blob/main/snead/5GCoreDecisionMatrix_8-11-2022.pdf) of these 5G core options!

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
- [Linux USB Composition Help](https://lwn.net/Articles/395712/)
