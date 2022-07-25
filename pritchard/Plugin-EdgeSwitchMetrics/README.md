# What is the Edge Switch Plugin?
This plugin works with the Edge Switch 8 to provide various statistics on both  the internal metrics of the edgeswitch itself as well as statistics on the current connection to other devices via its ports. This data is gained via connection to its local api. This plugin uses a three thread system of reading from the switch, routine writing to beehive and an interjection thread to allow for user controlled adjustment of the frequencies these three threads trigger. In the proccess of sending this data to beehive the third thread checks if selected variables are within the boundaries set in config, if they are not the thread sends a message to beehive denoting which variables located at which ports or areas of the switch are behaving strangely, as well as whether the detected value is too high or too low. This third thread also keeps a circular buffer of adjustable size that can be used if there is a desire to use the included max, min and average functions on the buffer data.
All librarys currently used are common, with exception of waggle.plugin which requires installation using:
```
pip install -U pywaggle[all]
```
libraries:
```
#from sqlite3 import TimestampFromTicks
from threading import Thread
import myconfig
from queue import Queue, Empty
from collections import deque
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import time
import requests
#import csv
from waggle.plugin import Plugin
```
# Example of running the Plugin
It is intended to be run with python3. Due to difficulties accessing Beehive, my pluggin curently uses the publish function to send the data to a local directory. As such my plugin is currently run using:
```
export PYWAGGLE_LOG_DIR=runlog <-----this sends data to local directory runlog
python3 main.py
```
data sent:
```
{"name":"test.bytes","ts":1658503730152837614,"meta":{},"val":"[{\"timestamp\": 1658503730092, \"device\": {\"cpu\": [{\"identifier\": \"ARMv7 Processor rev 1 (v7l)\", \"usage\": 64}],
ect... full json converted to string

{"name":"test.bytes","ts":1658503730158803000,"meta":{},"val":"8,rate,High"}
{"name":"test.bytes","ts":1658503730158803000,"meta":{},"val":"[0.0, 'on']"}

```
# Note
this pluggin requires the pywaggle library, local connection to an EdgeSwitch 8, as well as an additional file containing the password of your switch 
  <br>  
![image](https://user-images.githubusercontent.com/106760508/180482614-45add548-1df6-497a-aeb6-5ad1adbb94a8.png)
# Credits
This pluggin makes use of the unifi_switch_client, that file is the creation of Joseph Swantek and gemblerz, you can find it [here](https://github.com/waggle-sensor/unifi_switch_client)
