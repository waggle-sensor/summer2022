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
* [ ] Keep the AP mode on but use an external wireless adapter to connect to WiFi

**June 17th**
- ChirpStack is a fullstack that includes connecting the sensor nodes to gateway to server. 
- https://www.chirpstack.io/network-server/install/debian/
- Creates a database using the Postgres
- https://www.chirpstack.io/gateway-os/guides/getting-started/

ChirpStack Gateway Bridge:
- Converts LoRa packet fowarder protocol into a ChirpStack Network Server common data format (JSON and Protobuf) -- part of the ChirpStack open source LoRaWAN Network Server Stack
- https://www.chirpstack.io/gateway-bridge/gateway/raspberrypi/
