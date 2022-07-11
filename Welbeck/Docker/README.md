## Updated Docker File for ROS1 

Created on 06/30/2022

Beyond waggle/base-ros
 - installs rosdep, build-essentials, 
 - writes bash sourcing to .bashrc
 - sources .bashrc
 - creates and sources custom workspace for later downloading of packages from their respective sources
 - Copies in and builds beginner-tutorials package for bi-directional demonstration.


## Runtime Instructions

From within the Dockerfile locations, build with 
 - `docker build --tag <tag-name> .`

Then run  docker image/container with 
 - `docker run -it --net=host  <tag-name>`

Note: --net=host options expose all host ports to container

From the command-line within container,

 - ` echo "export ROS_MASTER_URI=http://<ip-of-master>:11311/" >> ~/.bashrc` 
 
 - ` echo "export ROS_IP=<ip-of-host>" >> ~/.bashrc` 
