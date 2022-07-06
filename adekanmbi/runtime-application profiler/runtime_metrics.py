import json
import socket
import sys
from collections import deque
import time
import threading
import logging
import subprocess
import os
import pickle
from tau_parser import parser
from collections import OrderedDict
from pathlib import Path
from datetime import datetime,timedelta
from waggle.plugin import Plugin
from jtop import jtop


def get_container_memory() -> int:
    """ Returns the memory usage of the container that this script is running in. """
    return int(open("/sys/fs/cgroup/memory/memory.usage_in_bytes").readline()[:-1])

class profiler:
    def __init__(self, filename, socket_path="/var/run/docker.sock"):

        """
        Init server with a dictionary of
            {metric_name: METRIC_TYPE}
        and host at the default socket path (unless otherwise specified as a str)
        """
        self.indir = os.getcwd()
        self.metric = {}
        self.filename = filename
        self.socket_path = socket_path
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.connect_to_metrics_socket()

        #self.server_thread = threading.Thread(target=self.runSystemProfile)
        #self.server_thread.start()

    def connect_to_metrics_socket(self):
        """
        Block until the server connects to the metrics socket. NOTE: this file must be shared with the Docker container
        that this script runs inside.
        """
        self.socket.connect(self.socket_path)

    def runTau(self):
        """ Provided Tau is installed in docker container this function will run Tau on the file to profile"""

        if Path(self.filename).is_file():
            cmd = "tau_python"
            temp = subprocess.Popen(
                "tau_python -ebs -T serial,python firstprime.py", shell=True, stdout=subprocess.PIPE
            )
            print(str(temp.communicate()))
        else:
            print("Cannot run Tau because ", self.filename, " not in directory")

    def send_data(self):
        with Plugin() as plugin:
            if os.path.exists('profile.0.0.0'):
                # self.parse()
                logging.info('Tau Profiling Completed')
                logging.info('Sending Data to Beehive')
                plugin.upload_file('profile.0.0.0', timestamp=str(datetime.now()))
                plugin.publish('test.bytes',self.parse())

            else:
                logging.info("Sending System Data to Beehive")
                plugin.publish('test.bytes',self.metric)


    def runSystemProfile(self):
        """ This function looks for the Tau subprocess
            and records system utilization.
        """
        self.metric["container_ram_usage"] = get_container_memory()
        # Records the tegrastarts of the host NVIDIA Nx device
        with jtop() as jetson:
            if jetson.ok():
                self.metric['tegrastats'] = jetson.stats
        # print(self.metric)
        self.send_data()

       


    def parse(self):

        """ Parses the data from Tau and System Utilization
            sends to beehive via pywaggle
        """
        tau = parser()
        data = OrderedDict()
        index = 1
        print ("Processing:", self.indir)
        # p.parse_directory(self.indir, index, data)


        application = OrderedDict()
        #application["source directory"] = indir

        # add the application to the master dictionary
        # tmp = "Application " + str(index)
        #data[tmp] = application
        data[self.indir] = application
        
        # get the list of profile files
        profiles = [f for f in os.listdir(self.indir) if os.path.isfile(os.path.join (self.indir, f))]
        #application["num profiles"] = len(profiles)

        application["metadata"] = OrderedDict()
        function_map = {}
        counter_map = {}
        for p in profiles:
            if p == 'profile.0.0.0':
                tau.parse_profile(p, application, function_map, counter_map)        
        
        return json.dumps(data, indent=2, sort_keys=False)
