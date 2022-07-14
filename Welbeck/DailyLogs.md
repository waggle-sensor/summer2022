# Daily Progress and ToDo Log

## Week 1: 06/20 - 06/24

### Thursday 06/23

- [ ] Worked through WaggleSensor Summer 2022 Onboarding
    - [x] Part 1: What is Sage? github, website, docs
    - [x] Parts 4, 5: Accounts and SSH Setup
    - [ ] Part 2: Agile Scrum Development Process
    - [ ] Part 3: Docker

### Friday 06/24

- [ ] Continue WaggleSensor Onboarding
    - [x] Part 3: Docker
    - [ ] Part 2: Agile Scrum Development Process
- [x] Investigate/Demonstrate Docker + ROS Integration
- [ ] Introductory Tutorial with Sage Edge Computing kit (Jeston Nano)
- [x] Internship Introduction slide to GDrive

#### Later

- [ ] Intro to ROS2

## Week 2: 06/27 - 07/02

### Tuesday 06/27

- [ ] Configured and Tested ROS with Docker on the Jetson Nano

### Thursday 06/30

 - [X] Augmented Dockerfile beyond waggle/ros-base per official ROS installation instructions
   - bootstrap tools
   - custom workspace
   - net-tools and iputils-ping for diagnostics
   - [updated Dockerfile](./Docker)
     - Docker container still requires ROS_MASTER_URI to be specified; could automate later

 - [x] Demonstate Bi-directional communications across containers on Nano [Shirley]
 - [x] Protocols Examples meeting @ 2pm
 - [x] Robot Team Meeting @ 4pm

## Week 3: 07/05 -07/08

### Tuesday 07/05

- [x] Successfully Flashed Jetpack 4.5 as test run
  - could not find Jetpack 4.4.1 OS Installation
  
- [x] Direction Meeting with YongHo (to be continued)

### Wednesday 07/06

- [x] Direction Meeting with YongHo Continued
  - Next Steps: Implement a multi-Nano, multi-container(docker for now) ROS(or other)-based network interfacing with a scheduler node to simulate multi-robot coordination
  - Think large-scale (!!)

- [x]Flash Nana-eMMC with JetPack 4.4.1 [Did not finish]

### Thursday 07/07

- [x] Flash Nano-eMMC with JetPack 4.4.1 with SDK Components
  - [Instructions to flash Jetson OS and Jetson SDK Components via docker container](./Getting%20Jetpack%204.4.1%20on%20Jetson%20Nano(emmc)/)
  - Next steps:
    - Multi-flash: script provided in docker. [Instructions](./Getting%20Jetpack%204.4.1%20on%20Jetson%20Nano(emmc)/README_Massflash.txt)
    - Can we create a ready image to flash directly instead of repeatedly following instructions?

- [x] Robot Team Meeting @ 4pm
  - Discussion:
    - Registered Peer-to-peer communication (as opposed to pub/sub comms) between ROS machines is inconsistent with waggle network architecture
    - Would require opening up ports between all sibling WES nodes
    - Could channel communication through upstream scheduler
    - Also ROS2 breaks away from the roscore registeration of ROS1; eliminates failure mode.
  - Next Steps: Execute [06/30 Protocols Examples Meeting] script on Nano

### Friday 07/08

- [x] ROS2 Setup and Beginner tutorials (to be continued)


## Week 4: 07/11 - 07/15

Goals

- Execute [06/30 Protocols Examples Meeting] script on Nano
- Implement a multi-Nano, multi-container(docker for now) ROS(or other)-based network interfacing with a scheduler node to simulate multi-robot coordination
- ROS2

### Monday 07/11
