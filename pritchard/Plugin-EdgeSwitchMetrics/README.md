This file contains the necessary files to take various metrics from a locally connected edgeswitch8 via its local api. 
These metrics currently include basic measurements of the POE wattage consumed per each port, as well as wether the port was disconnected or connected to a power consuming device over the period of testing.
It is intended to be run with python3.
After running main.py will write the obtained metrics to edgeswitch.csv.
Eventually these metrics will be able to be passed to a database from said file using a pywaggle library.
