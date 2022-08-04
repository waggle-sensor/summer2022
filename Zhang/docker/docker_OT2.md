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
1.given protocol ID, pull the protocol file from database : get rid of this process

```
File "/home/shirleyzzr/ot2_workcell/ot2_driver/database/connect.py", line 8, in <module>
    import config_SDl_DB as config
```

2.using scp to send the protocol file to the robot: have not tried on the real robot yet

3.create zeroMQ socket to send execute command to the rasperry pi: test on local machine with ip address, 127.0.0.1 success



how to ssh into the robot without giving the password

https://alvinalexander.com/linux-unix/how-use-scp-without-password-backups-copy/

1.generate a public and private key pair

```
ssh-keygen -t rsa
```

2.Copy your public key to your remote servers

```
scp id_rsa.pub al@pluto.example.com:./
```

3.Next, `ssh` into pluto, again supplying your password when prompted:

```
ssh al@pluto.example.com
```

4.Now copy the *id_rsa.pub* file to a new file named *authorized_keys* in that *.ssh* directory, like this:

```
$ cp id_rsa.pub .ssh/authorized_keys
```



add code to check the Internet connection



pip3 install zmq,paramiko, scp, rich (open port 8085)

apt-get install openssh-client (open port 22)



python3 -m protocol_handler.protocol_handling_client



when having the docker build image, COPY the ssh file

docker run -it -p 22 -p 8085 ros2:latest



find some way to add parameter for ip address instead of hardcode everything
