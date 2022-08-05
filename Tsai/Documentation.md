# Waggle: LoRaWAN

## Introduction
This project utilitizes the LoRaWAN technology to create a network system spanning from end nodes -> gateways -> network servers -> application servers -> forwarding LoRa frames to pywaggle's data pipeline via its plug-in:
![](https://i.imgur.com/G7Nl5s3.png)


## Chirpstack and RAKpi Setup
In this particular setup, the Gateway, Gateway Bridge, Network Server, and Application Server are all installed in the RAKpi (Raspberry Pi 4 with the RAK2287 mounted on it). The RAKpi log in credentials are:
- username: pi
- password: raspberry

I did everything in root, so when you log in the RAKpi, make sure to `sudo -s`. First, you need to connect to wifi to install the dependencies.
1. In the RAKpi terminal, use the gateway GUI by typing `gateway-config`, select `Configure WIFI`
2. Select `Enable Client Mode/Disable AP Mode`
3. Back in terminal, type `raspi-config`, select `System Options`
4. Select `S1 Wireless LAN`, then enter the SSID and passphrase accordingly
5. Type `ifconfig` in terminal to check the connections:![](https://i.imgur.com/b0hc66G.png)
    - The wlan0 should have an inet address
6. Install the dependencies:
    - `sudo apt install mosquitto`
    - `sudo apt install postgresql`
    - `sudo apt install redis-server`
7. Setting up the Gateway Bridge: https://www.chirpstack.io/gateway-bridge/install/debian/
8. Setting up the Network Server: https://www.chirpstack.io/network-server/install/debian/
    - In the `/etc/chirpstack-application-server/chirpstack-application-server.toml` file, edit it to the following:![](https://i.imgur.com/QOdkatM.png)
8. Setting up the Application Server: https://www.chirpstack.io/application-server/install/debian/
    - In the `/etc/chirpstack-network-server/chirpstack-network-server.toml` file, make sure the dsn is: ![](https://i.imgur.com/s4oqZup.png)
9. In the RAKpi terminal, use the gateway GUI by typing `gateway-config`, select the `Setup RAK Gateway Channel Plan`: ![](https://i.imgur.com/b5Wo08l.png)
10. Select `Server is Chirpstack`: 
![](https://i.imgur.com/mEkliNH.png)
6. Select `Chirpstack Channel-plan configuration`: ![](https://i.imgur.com/pHCQYGr.png)
7. Select `US_902_928`:
![](https://i.imgur.com/bt8YxHp.png)
8. Set the Server IP to 127.0.0.1 (localhost):
![](https://i.imgur.com/nBtTQzp.png)


## Chirpstack Application
With the setup completed, you should be able to access the chirpstack application on the RAKpi's IP address port 8080. In my case, since the RAKpi IP is 10.31.81.21, I can access the application on `10.31.81.21:8080` in the web browser on my computer (computer has to be connected to the same wifi with same netmask as the RAKpi). ![](https://i.imgur.com/262bR3C.png)
Once you can get into the application, you'll need to setup device profiles.

### Setup Device Profiles
There will initially be two default profiles already in the device profile tab: ![](https://i.imgur.com/eVA7ey6.png)
1. Create a new profile and fill in the blanks accordingly:![](https://i.imgur.com/F8UXcV4.png)
2. Check the "Device supports type B" in the Class-B tab and choose "every 2 seconds for ping slot periodicity":![](https://i.imgur.com/6J6ejC2.png)
3. Check the "Device supports type C" in the Class-C tab, then click update device profile
4. Create another new profile and fill in the blanks accordingly: ![](https://i.imgur.com/iuIMr37.png)
5. Click "Device supports type A" in the JOIN (OTAA/ABP) tab, then cluck update device profile


## End Nodes
The end nodes can be any device that supports LoRaWAN connectivity. In my working example, I used Arduino's MKRWAN 1310 and Seeed's LoRa E5 mini as end nodes. 

There are two methods of authentication for end nodes to join the network server via a gateway:
1. Over the Air Activation (OTAA)
2. Activation by Personalization (ABP)

|                 |         OTAA           |           ABP           |
| :-------------: | :--------------------: | :----------------------:|
| **Description** | Uses Device Address (DevAddr), Network Session Key (NWK SKEY), and Application Session Key (APP SKEY) to join the server | Uses Application Key (APP KEY) for request joining the server. Once joined, The NWK SKEY, APP SKEY, and DevAddr will be generated.
| **Pros**        | Can rejoin network after device reset | The session keys don't have to be hardcoded; only the application key has to match |
| **Cons**        | The DevAddr, NWKSKEY, APPSKEY have to be hardcoded in the device | Can't rejoin network after device reset |

The MKRWAN 1310 supports both OTAA and ABP while the E5 was only successful in using OTAA to connect.

### Setting up the MKRWAN
1. Download the arduino IDE at https://www.arduino.cc/en/software
2. After opening the IDE, go to Tools -> Manage Libraries. In the Library Manager that you just opened up, search up MKRWAN and download "MKRWAN" version 1.1.0
![](https://i.imgur.com/FMEgPxP.png)
3. Download the MKRWAN_SetUp.ino and MKRWAN_RepeatMsg.ino
4. Upload MKRWAN_SetUp.ino to MKRWAN1310 and open the serial monitor once it finishes uploading. You will be able to see the device EUI in the serial monitor: ![](https://i.imgur.com/Qe0KL7C.png)
5. On the Chirpstack Application page, click into "app" in the Application tab and create a new device:![](https://i.imgur.com/fqzwFtw.png)
6. After you click create device, click back into the device, then go to Activation tab and generate the DevAddr, nwkSKEY, appSKEY and note those hex strings down. Press Reactivate device
7. Back on the serial monitor, choose ABP by entering 2, then enter the DevAddr, NWK SKEY, APP SKEY in that order (these keys and addresses have to match with the device keys and address on Chirpstack)
8. There should be a Up loraframe shown on the Chirpstack application (this could take up to five minutes)
9. Once you see the Up loraframe show up on the Chirpstack application, open MKRWAN_RepeatMsg.ino, and change the DeviceAddr, NWK SKEY, APP SKEY and then upload the code:
![](https://i.imgur.com/5EVVHrx.png)
10. If the chirpstack server is able to receive the repeated messages, you're set to move the arduino anywhere with a power source

### Setting up the E5 Mini
1. Connect the E5 Mini to a machine to send AT commands to it
2. The following are the AT commands:
    - `AT+ID` lists the devEUI, devAddr, and appEUI
    - `AT+ID=DevEui,"98f1f997cfe558b5"` sets the devEUI (match the devEUI with the Chirpstack device EUI)
    - `AT+KEY=APPKEY,"66a8d4bcfcaf292f10907eef6d8d4545"` sets the APPKEY (match the APPKEY with Chirpstack)
    - `AT+DR=US915` changes frequency place to US frequency
    - `AT+MODE="LWOTAA"` changes mode to OTAA
    - `AT+JOIN` joins the OTAA network with corresponding APPKEY
    - `AT+MSG="Waggle!"` sends a message
    - `AT+CMSG="Waggle!"` sends a message and expects an ACK reply


## MQTT and Pywaggle Plugin
### Installing Dependencies and Code
1. Upgrade the apt: `apt update`
2. Check if the python is above version 3.6: `python3 --version`
3. Install the pip3: `sudo apt install python3-pip`
4. Install paho mqtt: `pip3 install paho-mqtt`
5. Install the Pywaggle plugin: `pip3 install -U pywaggle[all]`
6. Create a directory called `code`, and create a python file called mqtt_plugin.py:![](https://i.imgur.com/8yEOyCI.png)
7. Copy paste the code in the mqtt_plugin.py: https://github.com/waggle-sensor/summer2022/blob/main/Tsai/plugin/mqtt_plugin.py
### Creating a Service
1. `sudo touch /etc/systemd/system/mqtt_plugin.service`
2. `sudo nano /etc/systemd/system/mqtt_plugin.service`
3. Copy this into the mqtt_plugin.service file:
```python
[Unit]
Description=My long running script
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=pi
Restart=always
RestartSec=1
ExecStart=python3 /home/pi/mqtt_plugin.py

[Install]
WantedBy=multi-user.target
```
4. `sudo systemctl start mqtt_plugin && sudo systemctl enable mqtt_plugin`
5. Check the status of the service: `sudo systemctl status mqtt_plugin`
6. The logs of the lorawan frames will be updated live in the test-run-logs/data.ndjson file

