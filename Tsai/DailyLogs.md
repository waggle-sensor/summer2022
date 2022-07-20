## Andre's Daily Logs ##

**June 13th**
* [x] Attend 9:00AM virtual orientation for Argonne
* [x] Look into Waggle and the network of Sage nodes, edge computing, cloud uploading, cloud computing, and cloud extracting
* [x] Finish paperwork for onboarding
* [x] Request access to waggle-sensor GitHub
* [x] Join slack for waggle-sensor team
* [x] Setup Argonne accounts: email, employee account, etc


**June 14th**
* [x] Zoom call with Dr. Raj, who filled me up with the projects our team is working
* [x] Accept invitation for waggle-sensor GitHub
* [x] Look into ways to create a private local network between NVIDIA system, RAK2287, and the individual sensors using LoRaWAN
    - Looked into LoRaWAN networks and how it can be setup as a local network using the MAC addresses
    - Found useful read https://www.cardinalpeak.com/blog/setting-up-a-lora-gateway-to-view-iot-device-data : uses Rak7243, which also has antennas for LoRa and GPS system
        - Flash SD card (check out above link for more details on this), attach antennas, test WiFi connectivity
        - ![](https://i.imgur.com/uVBMwVY.png)
        - **instead of connecting to The Things Network (TTN, a LoRaWAN server), we can connect to the NVIDIA system**

**June 15th**
* [x] Sort out transportation to Argonne Laboratory
* [x] Once transportation is sort out, register for badge appointment with Argonne Lab
* [ ] TMS
* [x] Lined up with Pritchard on our current tasks
* [x] Look into network authentication and certificates
* [x] Look into Arduino LoRaWAN
* [x] Figure out RAK2287 and Wisgate network logistics, useful for tomorrow:
    - RAK commercial LoRaWAN (need to have a built in server): https://www.youtube.com/watch?v=6YES3DD-N60&ab_channel=RAKwireless
    - RAK2287 manual setup:
http://tosscore.com/download/RAK2287%20Quick%20Start%20Guide.pdf
* [x] Refamiliarize with new GitHub instructions

**June 16th**
* [x] Acquire gatepass and badge
* [x] Work env set up
* [x] Familiarize with linux terminal
* [x] Update NVIDIA nano system
* [x] Test out connections:
    - RAK pi to personal computer
    - RAK pi to NVIDIA nano
    - NVIDIA nano to Argonne-auth
* [x] Further studies on establishing LoRaWAN with RAK pi and the sensor nodes

**June 16th**
* [x] Connect RAKpi to WiFi while connecting to NVIDIA nano through ethernet (eth0), met multiple issues:
    - Argonne-auth WiFi needs WPA2 authentication
        - attempted to follow this: https://iceburn.medium.com/raspberry-pi-connected-to-wifi-of-wpa2-enterprise-ddd5a40c0b07 , but did not work
    - `nmtui` edit connections only show LAN (with eth0) and not wireless network
        - thought that was weird so I turned off AP mode and turned on client mode, then entered `iwlist wlan0 scan` in terminal -- I actually found that it scans the Argonne-auth network properly
        - ![](https://i.imgur.com/q833fFO.png)
        - followed https://raspberrytips.com/raspberry-pi-wifi-setup/ : go into `raspi-config` in terminal
        - ![](https://i.imgur.com/dbSRSyL.jpg)
        - go into System Options and select Wireless LAN
        - turned on hotspot on my laptop so the raspi can connect to a WPA authentication WiFi network
        - entered SSID and password of my laptop's hotspot manually on raspi and connected successfully
        - ![](https://i.imgur.com/iJiLZGU.png)
    - After successfully connecting to WiFi, I found the connection is unstable if the ethernet port is also plugged in -- probably because the RAK pi is confused if it should use WiFi or ethernet as connection to ping (I tested this by pinging 8.8.8.8, or google DNS server). If the ethernet port is unplugged however, the WiFi is stable other than high ping due to the additional intermediate network node (my laptop)
* [x] Keep the AP mode on but use an external wireless adapter to connect to WiFi

**June 20th**
- ChirpStack is a fullstack that includes connecting the sensor nodes to gateway to server.
- https://www.chirpstack.io/network-server/install/debian/
- Creates a database using the Postgres
- https://www.chirpstack.io/gateway-os/guides/getting-started/

ChirpStack Gateway Bridge:
- Converts LoRa packet fowarder protocol into a ChirpStack Network Server common data format (JSON and Protobuf) -- part of the ChirpStack open source LoRaWAN Network Server Stack
- https://www.chirpstack.io/gateway-bridge/gateway/raspberrypi/


**June 21st**
* [x] Complete TMS
* [x] Explore the capabilities of raspberry pi as the gateway
    - raspberry pi can function as a small database itself using Postgres management system
    - has a Application Server and Network Server for its chirpstack for LoRaWAN
    - `sudo journalctl -f -n 100 -u chirpstack-application-server` will allow us to see the log output for the raspberry pi's application server activity
    - forgot to take a picture of the log output when I tried it
* [x] Look into the Postgres commands and how we can edit and excess the database using this management system


**June 22nd**
We figured out that RAK2287 raspi can't be used as a sensor node, nor can the wisgate, so while waiting for the arduino sensors, we can figure out the gateway-server side of the system
* [x] Filing through the database of the raspberry pi to see what it is used for at the moment
    - found that there is an application server and network server database
    - also an empty database called postgres which is probably defaultly there
    - chirpstack application server table list:
    - ![](https://i.imgur.com/OWpuSMc.jpg)
        - interesting information is the "device" table:
        - ![](https://i.imgur.com/6CzwlqX.png)
        - these devices might be the sensor nodes that the gateway is connected to, or the nano that I was connected to before
* [x] Built a bike rack to place in the back of Argonne building 240 and another bike rack at a greenhouse place
* [x] Cleared the 4th floor lab and made it habitable
* [x] Populated the empty postgres database with fake data to test sending database entries to nano later on

**June 23rd**
Today was mainly trying to setup the chirpstack application server (AS) as well as the chirpstack network server (NS)
Chirpstack AS:
- Initially I tried following the set up of chirpstack AS following https://www.chirpstack.io/application-server/
- Realized that we don't want to use WiFi on the gateway, there is no way of accessing the set up application server on a webserver
- Decided to set up the application server on the nano's end
-![](https://i.imgur.com/eRYX8B0.jpg)
- successfully setup the application server on localhost and accessed it on a web server
- need to to decide whether to put the network server on the RAK2287 or the nano --- have quite a few thought on that at the moment


**June 24th**
* [x] Connect the gateway to the network server which connects to the application server
    - Since setting up the AS, NS, and gateway bridge all is easier, I decided to set them all up in the nano since I'm testing it out to see if the chirpstack even works
    - ![](https://i.imgur.com/qqOKube.png)
    - After setting up the servers and bridge, I linked them together using the chirpstack application platform
    * [x] create network server profile, gateway profile
    * [x] Connect the gateway to the network server using the gateway bridge 
    - ![](https://i.imgur.com/q9SBtur.png)
    - Successfully linked up the gateway
    - *when the arduino sensors get here, we can try setting up the applications and see if it shows up on the chirpstack application*

**June 27-28th**
* [x] Understand different components of the chirpstack
    - Gateways
        - demodulates LoRa packets
        - forwards the packets to the Network Server via the internet or LAN
    - Network Server
        - handles authentication
        - communicates with the Application Server
        - deduplicates number of uplinks
        - schedules downlink messages
        - handles join request and join accept messages between device and Join Server
    - Application Server
        - application layer, user interface
        - receives frame from Network Server and decrypt the data
        - encrypts the data and send downlinks to the end nodes
        - data events can be integrated with third party platform or storage like AWS, MQTT broker, HTTP, etc
    - Join Server
        - used for Over the Air Activation
        - generates security keys for encrypting and signing the messages
        - responsible for join request and join accept messages
        - from shared application key inside the device:
            - a dynamic device address
            - network session key
            - a appllication session key is generated to enable secure transmission of LoRaWAN messages

**June 30th**
- the live LoRaWAN frames given by the gateway has an issue because the WebSocket API is not connected
* [x] Fix the WebSocket API issue
    - with the new chirpstack update, the redis server needs to be version 5+. I was able to fix the websocket API not connected issue
- After the websocket issue is fixed, the Live LoRaWAN frames just continuously loads -> doesn't show any frames
* [ ] Fix the frame not showing issue
    - I checked the mqtt log files and it seems like the network server is receiving packets from the gateway, but it is not showing up on the application
    - ![](https://i.imgur.com/6NksVSa.jpg)
    - `gateway/mqtt: gateway stats packet received` are logged
* [x] look into the pywaggle plugin and see how the Application server can be integrated with it

**July 1st**
- MKRWAN 1310 and the antennas are here, so today's agenda is to get them to connect with the LoRa gateway and display packets on the Application Server
* [x] Look through the Arduino LoRamodem library
* [x] Code up a straightfoward message sending arduino code to send to the gateway
    - successfully sent messages to the gateway and have it show on the application
    - ![](https://i.imgur.com/nx8cLdw.jpg)
* [x] Edit code so the MKRWAN 1310 can connect to gateway with network and application session keys by itself without Serial write
* [x] Test the distance of connection
    - put the MKRWAN 1310 different floors of the buildingr
    - setup the MKRWAN 1310 on the 7th floor and it was able to send messages to the gateway on 3rd floor

**July 5th, 6th**
* [x] Set up router to connect both the gateway and the chirpstack network server -> so gateway can have communication with the server
* [x] Replicate work on Friday from home's environment
* [x] Create a new device with unique NWSKEY and APPKEY and DEV id
* [ ] Connect a second device simultaneously
    - unable to receive frames from the second device
* [x] Familiarize with the seeed modules that came in

**July 7th, 8th**
* [x] Connect a second device to the same gateway
    - successfully connected two device that sends data together at the same time
    - the application is able to see both devices' messages entering
    - ![](https://i.imgur.com/KzGeYt7.jpg)
    - ![](https://i.imgur.com/V2BFF2c.jpg)
    - The `TQ==` is a Base64 message that is translated into 'M', which was what I was sending to the gateway repeatedly
    - I also tried sending different messages like "Hello" and "Andre Tsai" >> all sends successfully
* [x] Send 10 messages of 'M' and see the packet loss
    - I was able to receive five out of the ten packets
    - Lots of theories:
        - could be that the gateway is unable to receive from a certain port when it is in use by another
        - could be that the message just simply did not send properly, etc
    - I also noticed that when there are no particular message being sent by the arduino devices, the gateway still receives a "AA==", which translates to ? when converting from base64

**July 11th, 12th**
* [x] Fixed packet loss issue
    - tried multiple different ways
    - in the end, delaying the sending of each packet solves the issue
        - this is consistent with the theory that the arduino was still in the process of communicating the previous message when another is sent. That will cause an error
    - I also tried resending each time we meet an error, and that also allows us to send all 10 packets
* [x] Look into Seeed lora E5 mini

**July 14,15th**
* [x] Connected LoRaE5 mini to the gateway and communicate with Chirpstack via lora connection
    - Use AT commands to personalize the LoRaE5 mini
    - Able to customize message after activating the OTAA connection
    - One issue that the message are often dropped
* [x] Switch to OTAA connect instead of ABP
    - OTAA allows the NWSKEY and other sessions keys to be rotatable and therefore increasing security of the connections

**July 18th**
- Carpool was cancelled so I was unable to go into office
* [x] Work with the E5 mini and see what is causing the message dropping issues
    - I looked into multiple write ups on OTAA connection issues and most are dealing with joining session which we don't have an issue with. I believe packet losses are inevitable and is what's causing the unsent messages
    - A pretty clear idea of the process of joining OTAA session as well as the comparison to ABP: https://www.techplayon.com/lora-device-activation-call-flow-join-procedure-using-otaa-and-abp/
