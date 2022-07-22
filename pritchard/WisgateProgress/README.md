# The intent of this project
In this project I worked to design a framework we could use to have a large web of small sensors communicate over Lora with a LoRaWAN gateway which would then pipe the results to a NVIDIA Nano, which would then communicate the collected data to Beehive. The Main focus of the assignment was to identify whether we should use a RAK equiped rasberry pi or a WisGate gateway as the gateway used in the final implemenation by trying to get a waggle plugin running successfully on both. Originally I worked on both the RAK Pi and WisGate, but after Andre joined the project he took over the RAK Pi portion and I concentrated on the WisGate. Between the two devices, we found out early on that the RAK pi was more controllable and the WisGate was more of a user friendly, out of the box ready device. In essence, when working with the WisGate I had access to a nice and expansive UI, but was quite restricted from touching what was outside the bounds of that UI.



# Where I got in this project
I eventually decided on using the built in LoRaWAN network server within the WisGate to communicate with a built in MQTT broker which would then communicate with a MQTT client on the nano. There were some troubles getting the client to enroll correctly as it would not accept the large scale topics used by the WisGate which were denoted by "+". I eventually realized that I could subscibe to any topic that would logically be within those larger topic assignments. I ended up getting moved off of this project when next developement steps required experimental devices to be connected up to the WisGate as I could not give it false data to send to the nano. By that point I had figured out how to enroll a client hosted on the nano to the MQtt broker hosted on the Wisgate and could see basic existence communication between the two. I had also picked out the devices/sensors to hook up to the wisGate, they ended up ariving twoish days after I was reassigned.
<br>
sample output of testingpaho.py:
```
creating new instance
connecting to broker
Subscribing to topic John
Publishing message to topic John
message received  1
message topic= application/2/device/238/rx
message qos= 0
message retain flag= 0

```
