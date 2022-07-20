6.24

- Learn about the structure of Waggle and Sage
- Go through Docker tutorial, waggle-docker

6.30
- Configure ROS on docker

- Implement publisher and subscriber nodes for ROS to communicate between two docker environment on two host machine connected to same local network 

  --net=host

  ROS_MASTER_URI=http://hostip:11311/  Are we able to specific the port needed

7.6

- go over introduction to distributed systems: performance, fault tolerance, consistancy
- try ROS publisher/subscriber on multiple machines/dockers: ROS1 successful

7.11

- Using dockerd to manager dockers,spin up docker on remote machine: refer to docker_related.md successful
https://github.com/ct2034/dockeros maybe useful for a scehduler?

- Go through OT2 basic tutorial
https://support.opentrons.com/s/ Ethernet supported, scp protocols to OT2 robot

7.12

- Go though OT2-driver and OT2-workcell github repo
  https://github.com/AD-SDL/ot2_workcell 

  ot2-workcell_manager's relationship to scheduler; ROS2 layer

  https://github.com/AD-SDL/ot2_driver 

7.13 

- find examples for multi-robot middleware like open-RMF

  https://github.com/open-rmf/rmf

- Learn about ROS2 

  no more roscore, setting up ros_domain_id can make nodes talk to each other

7.14

- test ROS2 publisher/subscriber within Docker: successful

  All devices will be within the same waggle Node, K3s cluster
  

 7.15
 - rewrite the Dockerfile for ros2 based on waggle plugin
 - test ROS2 publisher/subscriber across docker in different machines withint same local network: successful
 - no more host network! configure fast DDS to use specified ports for ros2 to communicate across containers on machines within same local network
 https://github.com/eProsima/Fast-DDS/issues/1698

 7.18
 - test ros2 docker file in both wireless and Ethernet

7.19

- meeting with Doga, go over the connection for OT2, super helpful
- test zeroMQ socket connection on local machine, successful
