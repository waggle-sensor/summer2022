### docker_OT2

1.Set up ssh key to connect to the robot (not finished yet)

https://support.opentrons.com/s/article/Setting-up-SSH-access-to-your-OT-2

2. pip3 install rosdep&& rosdep init

rosdep update && rosdep install -i --from-path src --rosdistro foxy -y

```
arm_controller: Cannot locate rosdep definition for [arm_driver_pkg] (error message)

```

3. pip3 install mysql-connector, also add sys directory to protocp_handling_client.py

Several steps to protocol_handling_client.py
1.given protocol ID, pull the protocol file from database 

```
File "/home/shirleyzzr/ot2_workcell/ot2_driver/database/connect.py", line 8, in <module>
    import config_SDl_DB as config
```

2.using scp to send the protocol file to the robot: have not tried on the real robot yet

3.create zeroMQ socket to send execute command to the rasperry pi: test on local machine with ip address, 127.0.0.1 success
