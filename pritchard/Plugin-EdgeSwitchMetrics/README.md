# What is this file?
This file contains the necessary files to take various metrics from a locally connected edgeswitch8 via its local api. 
These metrics currently include basic measurements of the POE wattage consumed per each port, as well as wether the port was disconnected or connected to a power consuming device over the period of testing.
<br />
All librarys currently used are common:
<br />
![image](https://user-images.githubusercontent.com/106760508/177654319-2e67b8ae-99bf-4d99-a3b0-6765ebd82d01.png)
<br />
```
import json
import time
import requests
import csv
```
# Example of running the file
It is intended to be run with python3. Over the test period data is pulled from the api multiple times in order to find metrics that model the data collected over the test period 
Example of running code: 
<br />
![image](https://user-images.githubusercontent.com/106760508/177652188-d9b7ca2e-2042-4724-879b-64c3bdc0a2e6.png)
<br />
```
python3 main.py
2.58
port 1
0.0
port 2
0.0
port 3
iterations= 1
2.62
port 1
0.0
port 2
0.0
port 3
iterations= 2
2.62
port 1
0.0
port 2
0.0
port 3
iterations= 3

```
here are some example final outputs: 
<br />
![image](https://user-images.githubusercontent.com/106760508/177652120-ea8f27b4-1b91-4035-aa40-31a8f1212674.png)
<br />
```
2.596
2.62
2.58
0.0

```
In order they include:  the average POE wattage used over testing interval by port1, the maximum wattage pulled over that period by said port, the minimum wattage pulled, and a number indicating whether port one either remained plugged in or un plugged= 0,  was originally unplugged in but was plugged in at some point in the testing period= 1, or was originally plugged in but was unplugged at some point in the testing period= 2,   
After running main.py will append the obtained metrics to edgeswitch.csv. In addition to the earlier referenced variables isonoriginal is also included, it indicates whether a particular port was originaly consuming wattage at the beggining of testing 
<br />
![image](https://user-images.githubusercontent.com/106760508/177653691-be3a7f9d-b02a-409b-b3e0-f0b62adec717.png)
<br />
# Future progress to be made
Eventually these metrics will be able to be passed to a database from said file using a pywaggle library.
