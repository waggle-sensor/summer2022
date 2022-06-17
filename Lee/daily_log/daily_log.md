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
- [x] Had a meeting with Joe & Francisco: https://github.com/waggle-sensor/node-platforms/tree/main/nvidia-nano (IT WAS VERY USEFUL, AWESOME!!!!!)
- [x] Attend the Demo meeting; Joe, Neal, Sergey, ismael and Sammi to understand the overall plan (e.g., goal of testing the VSN beepkeeper change in a VM style space)

Things to do:
- [ ] It seems like ROS depends on other modules such as python version, and need to conduct more research into the singularity dependency & docker
- [ ] Checking Jetson Nano software updater; the package system is broken because of using third party repositories.
