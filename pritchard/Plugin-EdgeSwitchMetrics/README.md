# What is this file?
This file contains the necessary files to take various metrics from a locally connected edgeswitch8 via its local api. 
These metrics currently include basic measurements of the POE wattage consumed per each port, as well as wether the port was disconnected or connected to a power consuming device over the period of testing.
# Example of running the file
It is intended to be run with python3.
example:
<br />
![image](https://user-images.githubusercontent.com/106760508/177652188-d9b7ca2e-2042-4724-879b-64c3bdc0a2e6.png)
<br />
here are some example final outputs: 
<br />
![image](https://user-images.githubusercontent.com/106760508/177652120-ea8f27b4-1b91-4035-aa40-31a8f1212674.png)
<br />
In order they include:  the average POE wattage used over testing interval by port1, the maximum wattage pulled over that period by said port, the minimum wattage pulled, and a number indicating whether port one either remained plugged in or un plugged= 0,  was originally unplugged in but was plugged in at some point in the testing period= 1, or was originally plugged in but was unplugged at some point in the testing period= 2,   
After running main.py will append the obtained metrics to edgeswitch.csv. In addition to the earlier referenced variables isonoriginal is also included, it indicates whether a particular port was originaly consuming wattage at the beggining of testing 
<br />
![image](https://user-images.githubusercontent.com/106760508/177653691-be3a7f9d-b02a-409b-b3e0-f0b62adec717.png)
<br />
# Future progress to be made
Eventually these metrics will be able to be passed to a database from said file using a pywaggle library.
