# Daily Progress Report
----------------------------------------------
### Week 1: 5/31 to 6/3 ###
#### Tuesday May 31th ####
- [x] Attended the first orientation
- [x] Created workflow and documentation on Github
- [x] Filled out HR forms such as I-9 and workday
- [x] Registered and took mandatory TMS courses

Things to do:
- [ ] In order to get permission Argonne file box, the authorization issue needs to be solved out  
- [ ] Meeting for the project shedule with Pete and Raj  
- [ ] Building up the agile planning for the summer plan

#### Wednesday June 1th ####
- [x] Took mandatory TMS courses  

Things to do:  
- [ ] In order to complete the section 1 and section 2 of I-9 process, communicating with Argonne HR by sending an email is required by tomorrow  

#### Thursday June 2th ####
- [x] Made an appointment and obtained an Argonne badge
- [x] Had a lunch meeting with Joe and Sean to discuss about the internship plan  

Things to do: 
- [ ] Before ask Yongho to figure out the ROS configuration, implementing and deploying docker files on my laptop.

#### Friday June 3th ####
- [x] Attended the PAISE Workshop: www.paise.org
- [x] Read the file *RPL software/network brainstorm* and *WORKFLOWs for Modular SAL Demo* shared by Joe  

----------------------------------------------
### Week 2: 6/6 to 6/10 ###
#### Monday June 6th ####
- [x] Had a meeting with Pete and Raj to discuss about the overall summer plan (Yongho and Rory virtually)
- [x] Met Doga, Casey and Rafael in the robot room and talked about the schedule.  

Things to do:  
- [ ] Reading up the documents shared by Doga by this Friday  
- [ ] Preparing tomorrow meeting with Joe & Francisco to catch up the WAGGLE OS process

#### Tuesday June 7th ####
- [x] Completed the mandatory TMS courses: DEI101 Diversity Equity and Inclusion at Argonne Introduction (ESH561 Bicycle Safety course as an elective class)
- [x] Finished up the ROS course week 1, and took an exam for the certificate
- [x] Emailed HR to figure out Alien Determination Form (ANL67)

Things to do:
- [ ] Conducting research into the ROS system and how to apply it  

#### Wednesday June 8th ####
- [x] Attended the SAGE software team meeting (brief demo of accomplishments over the past sprint)
- [x] Set up RPI finally
- [x] Updated my payment check on Argonne Workday
- [x] Obtained the Argonne prox card. 

Things to do:  
- [ ] Reading up following documents: https://docs.waggle-edge.ai/docs/about/overview and https://github.com/waggle-sensor/  
- [ ] Preparing tomorrow meeting with Joe & Neal - Interface for new nano-student nodes to register with beekeeper to get credentials to a “student” beehive

#### Thursday June 9th ####
- [x] Had a meeting with Joe and Francisco to discuss about the WAGGLE OS/WES
- [x] Set up Jetson Nano and install/test ros docker file on Nano, ref: https://developer.nvidia.com/embedded/learn/tutorials/jetson-container  

Things to do:  
- [ ] Reading up the Lightweight Kubernetes, ref: https://k3s.io

#### Friday June 10th ####
- [x] Had a discussion with Yomi; Self-Supervised Learning Tree Detection
- [x] Tested ros/ros2 files on Nano  

Things to do:  
- [ ] I need to implement the nano image to deploy, run codes from ECR, and get the ros example from Yongho working to control something in the robot space. Furthermore, as the previous ros file built by Yongho might need a different ROS version (LIDAR), it needs to be modified  

----------------------------------------------
### Week 3: 6/13 to 6/17 ###
#### Monday June 13th ####
- [x] Attended the Argonne Fifth Quantum Computing Tutorial Day 1: Qiskit (Hands-On)
- [x] Had a meeting with Yomi to discuss about the ECR and docker for the Sage project.
- [x] Finally completed read up https://github.com/waggle-sensor/ and https://docs.waggle-edge.ai/docs/about/overview 

Things to do:  
- [ ] Preparing Thursday meeting with Joe & Francisco to discuss about the details of what needs to be in nano OS and the detailed services needed to run WES
- [ ] Reading up and implemented Docker tutorial: https://www.katacoda.com/courses/container-runtimes

#### Tuesday June 14th ####
- [x] Attended the Argonne Fifth Quantum Computing Tutorial Day2: VQE (Hands-On)
- [x] Had a meeting with Joe, Francisco, and Sammi. Francisco and I figured out the outline for setting up Nano on Ansible. The steps are following:  

***Note. Assuming your Jetson developer kit has been flashed with and is running L4T 32.3.1 or higher.***  
1. ```sudo apt update```
2. ```sudo apt install nvidia-jetpack```  
3. ```sudo apt install nvidia-cuda-toolkit```  
4. ```sudo apt show nvidia-jetpack```  
5. ```cat /usr/local/cuda/version.txt```  

Current Jetson NAno version: JetPack 4.6 that includes 10.2 CUDA, ref: https://docs.nvidia.com/jetson/jetpack/install-jetpack/index.html 
 
Things to do:
- [ ] July 1: Get the document to figure out the list of minimal WES
- [ ] July 15: Get the Ansible script done
- [ ] Reading up Ansible documents

#### Wednesday June 15th ####
- [x] Attended the Argonne Fifth Quantum Computing Tutorial Day3: QAOA (Hands-On)
- [x] Debugging, Solved synchronization issue in Nano: https://github.com/justsoft/jetson-nano-date-sync

#### Thursday June 16th ####
- [x] Attended the Argonne Fifth Quantum Computing Tutorial Day4: Quantum Machine Learning (Hands-On)
- [x] Conducting research into ROS (edc courses) 

#### Friday June 17th ####
- [x] Attended the Argonne Fifth Quantum Computing Tutorial Day5: Quantum Noise (Hands-On)
- [x] Had a meeting with Joe & Francisco: https://github.com/waggle-sensor/node-platforms/tree/main/nvidia-nano (IT WAS VERY USEFUL, AWESOME!!!!!)
- [x] Attend the Demo meeting; Joe, Neal, Sergey, ismael and Sammi to understand the overall plan (e.g., discussion of testing the VSN beepkeeper change in a VM style space)

Things to do:
- [ ] It seems like ROS depends on other modules such as python version, and need to conduct more research into the singularity dependency & docker to run ROS - I will ask the question when Sean comes back to Argonne from his vacation.
- [ ] Checking Jetson Nano software updater; the package system is broken because of using third party repositories.
- [ ] Reading the Ansible documents to implement our node system.

----------------------------------------------
### Week 4: 6/20 to 6/24 ###
#### Monday June 20th ####
- [x] Report to Raj and Pete: The current Jetson Nano version is JetPack 4.6 which includes 10.2 CUDA. While installing several packages such as Jetpack 4.6 for Nano on Ubuntu 18.04 LTS, it shows the unmet dependencies issue, including to the python-rosdep-moduels do not match. Setting up for ROS in a Singularity container as singularity can be an option to solve it out and Docker container can be used to run a container inside the container, however, it also shows the mismatch of the dependencies; Plus, it shows the another mismatch issue such as minikube_1.16.0-0_amd64.deb: package architecture (arm64) does not match system (amd64) as those architectures are not same. The next step in order to get over these issues, the list of dependencies for ROS is required.

Things to do:  
- [ ] Debugged the dependency and listed up the required for Nano

#### Tuesday June 21th ####
- [x] Had a meeting with Joe and Francisco: https://github.com/waggle-sensor/node-platforms/tree/main/nvidia-nano

#### Wednesday June 22th ####
- [x] Setup and cleaned up robotic lab workspace
- [x] Had a meeting with Joe and Francisco: https://catalog.ngc.nvidia.com/containers 

Things to do:  
- [ ] Research into configuring keyboard-configuration as this command```DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration``` does not work.
- [ ] Install ROS GUI

#### Thursday June 23th ####
- [x] Had a meeting with Pete, Raj, Joe to discuss about Jetson Nano Kit plan
- [x] Got ssh access for Nano 
- [x] Had a meeting with Sean and Yomi; discussion docker container & architecture

#### Friday June 24th ####
- [x] Read up ROS documents
- [x] Debugging ROS dockerfile 

Things to do:  
- [ ] Research into Ansible 
- [ ] Jetson Nano Kit github edition
- [ ] Zhuoru & Kojo meeting next Monday

----------------------------------------------
### Week 5: 6/27 to 7/1 ###
#### Monday June 27th ####
- [x] Debugged all day: last deployed the gpu-stress-test ```kubectl run gpu-test --image=waggle/gpu-stress-test:1.0.1 --attach=true```
- [x] Had a meeting with Yongho to discuss about the summer internship plan (IT WAS GREAT!!!!!!) 

Things to do (by tomorrow):  
- [ ] disconnect everything from the Nano in 4302 and start from scratch
- [ ] install the 32.4.4 L4T
- [ ] for the external media use the 512GB Samsung USB stick (in-place of the SD-card dongle)
- [ ] follow the instructions in the README to get the node back to the point of it is now, but with a L4T 32.4.4 base
- [ ] ensure docker and k3s GPU access work using the gpu-stress-test

#### Tuesday June 28th ####
- [x] Figured out the Nano GPU running on the K3S finally (THANKS FRANCISCO AND JOE!!!!!)

Things to do (by this Friday):  
- [ ] Cleaning up the documents such as README file

#### Wednesday June 29th ####
- [x] Career Day YAY !!!!!! (showing off my Kayaking skill :sunglasses:)

#### Thursday June 30th (Important as it is Minji's birthday :confetti_ball:)
- [x] Attended AI group meeting
- [x] Had a meeting with Robot team for the demo
- [x] Had a Sage Edu Kit meeting
- [x] Meeting with another robot team meeting (thanks Yongho)

Things to do:  
- [ ] Getting the boot strapping for the Nano done and Ansible (https://www.ansible.com/overview/how-ansible-works?hsLang=en-us) scripts created to finish the boot strapping

#### Friday July 1th ####
- [x] Installed Ansible files on Jetson Nano
- [x] Explored the ansible playbook with tutorials: https://www.youtube.com/watch?v=bU6OEtbdiOI

Things to do:  
- [ ] Finishing the Ansible script by July 15th

----------------------------------------------
### Week 6: 7/4 to 7/8 ###
#### Monday July 4th (Happy July 4th!)

#### Tuesday July 5th ####
- [x] Installed pip Ansible on Nano. First of all, it requires to switch the python version to install pip as there are two python versions on linux. If the command line ```curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 (e.g.)``` runs, it will show the moduleNotFoundError: No module named 'distutils.cmd' for example.  
```sudo apt update```  
```alias python='/usr/bin/python3.6```  
```sudo update-alternatives --config python3```  
```python -m pip install --upgrade pip```  
```python -m pip install --user ansible```  
```python3 -m pip show ansible```  

Things to do:  
- [ ] Finishing up reading the Ansible tutorials

#### Wednesday July 6th ####
- [x] Conducting research into Ansible running on Nano VS Ansible running on Docker: which one is suitable for WaggleOS?

#### Thursday July 7th ####
- [x] Had a meeting weekly EDU; summary: (1) Need to figure out hw to add the sensor on our OS (like building a tutorial for the educational points), (2) Add another type sensor such as soil moisture sensor  
- [x] Had a meeting with Francisco and Sean: how to configure the microphone setup: Completed! (update device manager (labeling) PulseAudio)
- [x] Had a weekly Robot (ROS) meeting
 
Things to do:  
Linux(Waggle) should know about the itemized list such as different types of sensors 
 
#### Friday July 8th ####
- [x] Had a meeting with Joe to talk about Ansible script
- Configuration on MAC

- From user side

(1) Ensuring ```pip``` is available on your computer and install ansible  
```pip --version```  //pip 21.3.1 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

```pip3 install --upgrade pip``` //if you do not have

```pip3 install ansible``` // For linux, it is avilable here: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

(2) Test on your own machine with hello-world file. Create your own directoy first (e.g., ansible): https://github.com/waggle-sensor/node-platforms/blob/main/nvidia-nano/01_ansible_nvidia-nano_base.yaml 

```cd ansible```

```cd node-platforms/```

```cd nvidia-nano```

```ansible-playbook -i ansible_inventory 01_ansible_nvidia-nano_base.yaml //error will occur if it is your own host```

```ansible-playbook -i ansible_inventory --user root 01_ansible_nvidia-nano_base.yaml //should work as "--user" included```

Ref
https://formulae.brew.sh/formula/ansible 
https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#:~:text=Group%20variables%20are%20a%20convenient,from%20all%20of%20those%20groups.

----------------------------------------------
### Week 7: 7/11 to 7/15 ###
#### Monday July 11th
- [x] Configured out how to set up sensors on Nano (Microphone and BME680 Sensor)

#### Tuesday July 12th
- [x] Half done with building Ansible script
- [x] Had a meeting with Raj, Joe, Francisco and Sammi to discuss about the WES and Ansible

Things to do:  
- [ ] Finishing up creating the Ansible script by this Friday (or ASAP)

#### Wednesday July 13th
- [x] Attended Yomi presentation regarding his current work on application profiling
- [x] SSH setup and tested the Ansible script on the New Nano 

#### Thursday July 14th
- [x] Done with Ansible script
- [x] Had a meeting with EDU team and Robotic team

#### Friday July 15th
- [x] Ansible script final test

----------------------------------------------
### Week 8: 7/18 to 7/22 ###
#### Monday July 18th
- [x] Had a meeting

----------------------------------------------
### Week 9: 7/25 to 7/29 ###
#### Monday July 25th
- [x] ddd

----------------------------------------------
### Week 10: 8/1 to 8/5 ###
#### Monday August 1th
- [x] ddd
