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
* [ ] Sort out transportation to Argonne Laboratory
* [ ] Once transportation is sort out, register for badge appointment with Argonne Lab
* [x] Look into ways to create a private local network between NVIDIA system, RAK2287, and the individual sensors using LoRaWAN
    - Looked into LoRaWAN networks and how it can be setup as a local network using the MAC addresses
    - Found useful read https://www.cardinalpeak.com/blog/setting-up-a-lora-gateway-to-view-iot-device-data : uses Rak7243, which also has antennas for LoRa and GPS system
        - Flash SD card (check out above link for more details on this), attach antennas, test WiFi connectivity
        - ![](https://i.imgur.com/uVBMwVY.png)
        - **instead of connecting to The Things Network (TTN, a LoRaWAN server), we can connect to the NVIDIA system**

`NEXT STEPS: find out how to connect RAK2287 to an individually owned server instead of TTN, possibly need authentication abilities to prevent random modules connecting. Need to know more about the NVIDIA system.`
