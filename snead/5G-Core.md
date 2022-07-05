# 5G Core Information
This is where I'm compiling my research about different open source 5G Core organizations. 
### Helpful 5GC Resources
- [UERANSIM](https://github.com/aligungr/UERANSIM) is a simulator that acts as a 5G mobile phone and base station to test 5G Cores 
- Explanation of [5G Core Architecture](https://www.digi.com/blog/post/5g-network-architecture)
- Quick dicussion of [PNF and VNF](https://www.linkedin.com/pulse/technology-analogy-physical-virtual-network-functions-milind-kulkarni/)

# ONAP
> "Open Network Automation Platform (ONAP) is an open source project hosted by the Linux Foundation. ONAP provides a comprehensive platform for real-time, policy-driven service orchestration and automation. ONAP enables service providers and developers to rapidly automate the instantiation and configuration of physical and virtual network functions and to support complete life cycle management activities." \- [ONAP](https://docs.onap.org/en/honolulu/index.html)

[ONAP Home Page](https://www.onap.org/)

[ONAP Documentation](https://docs.onap.org/en/honolulu/index.html#)

[Software and Hardware Requirements](https://docs.onap.org/projects/onap-oom/en/honolulu/oom_cloud_setup_guide.html#cloud-setup-guide-label)
## Architecture Notes
![ONAP-Notes](https://user-images.githubusercontent.com/107580325/176268551-013da326-381a-4dad-b308-e67f7bfd19b1.png "ONAP Architecture")

All pictures and information compiled from [ONAP's Architecture page](https://docs.onap.org/en/honolulu/guides/onap-developer/architecture/index.html)

## Integrating COTS Radios
So far it looks like mmWave Radios and our equipment can be controlled using an ONAP's SDN controller for ‘Radio’ (SDN-R), an additional service you can integrate into the run-time model. It's a part of their ONAP component, SDN-Controller. Once set up, the user could open the SDN-R portal and see which devices are connected (and manually mount radios, if needed). 

![image](https://user-images.githubusercontent.com/107580325/176289800-2dbdf6bd-9397-4a30-9d91-4cc5e908bf1d.png)

Image from [ONAP SDN-R Documentation](https://docs.onap.org/projects/onap-ccsdk-features/en/honolulu/guides/onap-user/home.html)

### Attributes
- Automated closed-loop management
  - takes a little more set up at the beginning to design and manage
- Portal function makes interacting with ONAP system more accessible
  - Also has CLI function
- Robust with community and ONAP created plugins and services
- A wealth of direct how-to guides (mostly focuses on initial set up) and documentation
- Use of Kubernetes and Docker containers already present in Waggle community
- Can't find much evidence of user support, ie being able to contact a developer to get help
- One-time-pay [eLearning course](https://training.linuxfoundation.org/training/onap-fundamentals/) on specifics of how to use and interact with ONAP 
- Being very robust means a lot of RAM and processing power required

# free5GC
An opensource 5G Core that can be used commercially without any licensing. To gain access to training, seminars, and tech support you must pay for [membership](https://www.free5gc.org/membership/)

[free5GC Home Page](https://www.free5gc.org/)

[free5GC Stage 3 GitHub](https://github.com/free5gc/free5gc-stage-3)
## Versions
free5GC was developed in different stages, and offers each stage as an independent download. Information compiled from free5GC's [roadmap](https://www.free5gc.org/roadmap/)
#### Stage 1: Non-Standalone 5G
Based on 4G EPC architecture, with migrated 5G interfaces. This stage was developed when 5G UE and gNB hardware was not yet on the market, so it goes through and communicates with 4G UE and eNB. 

[Hardware and Software Requirements and Installation](https://www.free5gc.org/installations/stage-1-all-in-one/)

Architecture below:

<img src="https://user-images.githubusercontent.com/107580325/176721996-1af7fae7-facc-4371-9903-41fc0cd4c8fb.png" width="625" height="250">

#### Stage 2: Standalone 5G
In the standalone architecture, they added more network functions and made them all 5G based. Partial implementation of network slicing and orchestration. No application services at this stage. 

[Hardware and Software Requirements and Installation](https://www.free5gc.org/installations/stage-2-standalone-5g/)

Architecture below:

<img src="https://user-images.githubusercontent.com/107580325/176761914-b822154a-e396-4305-81e2-7be512abf4a0.png" width="625" height="300">

#### Stage 3: Full Operational 5G Core
5G orchestrator and Operation, Administration and Management (OAM) implemented as a features, supports IPTV application.
Add features: non-mobile access network (N3IWF) and UP Uplink Classifier (ULCL)

[Hardware and Software Requirements](https://github.com/free5gc/free5gc/wiki/Environment)

[Installation](https://github.com/free5gc/free5gc/wiki/Installation)

## Integrating COTS Radios
free5GC has a [WebConsole](https://github.com/free5gc/webconsole) that allows you to manage registered radios. Here's a link to how they recommend [testing connections](https://www.free5gc.org/installations/stage-3-sim-install/) using [UERANSIM](https://github.com/aligungr/UERANSIM) as a radio.

[Radio Connection Demo](https://www.youtube.com/watch?v=2rgZgYyqugM&ab_channel=free5GC) <-- got access to the internet!

Other videos they have show demos of how to [configure and run UE, RAN with free5GC](https://www.youtube.com/watch?v=WDy0TL4fPKI&ab_channel=free5GC)

## Attributes
- Access to different versions in varying stages of 5G integration could be useful as Waggle begins migration to 5G
- After initial configuration, it seems ready to go "off the shelf," so to speak
- [Forum](https://forum.free5gc.org/) for asking questions!
- Pay wall (annual membership fee) for training and seminar access, but that's not too unique 
- run and managed entirely through Linux CLI

# Aether (ONF)
> "Aether is the first open source 5G Connected Edge platform for enabling enterprise digital transformation. It provides mobile connectivity and edge cloud services for distributed enterprise networks as a cloud managed offering. Aether is an open source platform optimized for multi-cloud deployments, and simultaneous support for wireless connectivity over **licensed, unlicensed and lightly-licensed (CBRS) spectrum."** \- Aether website

[Aether Home Page](https://opennetworking.org/aether/)

[Aether Dev Wiki](https://wiki.opennetworking.org/display/COM/Aether)

## Architecture
![Aether Architecture](https://user-images.githubusercontent.com/107580325/176931696-64211a88-295d-403c-9f32-87f96d4017d6.png)

(Image from Aether website)

## SD-Core
> "The SD-Core project is a 5G/4G disaggregated mobile core implementation optimized for deployment in the public cloud. SD-Core exposes standard 3GPP interfaces for those wishing to use the project as a conventional mobile core, but it is also pre-integrated with an adapter available as part of the Aether ROC subsystem for those wishing to deploy mobile-core-as-a-service as a SaaS solution.
>
> SD-Core leverages control plane components of the **Free5GC project** and the ONF OMEC project, building on both of these upstream open source projects by adding cloud native capabilities for scaling, resiliency and multi-cloud agility." - SD-C Wiki


[SD-Core Wiki](https://wiki.opennetworking.org/display/COM/SD-Core)

[SD-C Documentation](https://docs.sd-core.opennetworking.org/master/overview/introduction.html)

[Hardware requirements](https://docs.sd-core.opennetworking.org/master/deployment/deployment5G.html) <-- seems very costly, and requires Kubernetes and Helm environments

- Standard 3GPP interfaces allow SD-Core to be run as a standalone mobile core, can also be integrated into Aether
- SD-C has runtime APIs that enable closed loop control and other services, including ensuring that only authorized users are connecting to the network
- SD-C manages Network Slicing
- Three User Plane Functions (UPF) that are designed to be customized at the edge for different use cases
- Aether acts as a Runtime Operational Control (ROC) portal, and it seems you can use the ROC to control SD-Core without... needing everything? Might need to look into third party ROC. REST Interface (Simapp?) or Helm Charts?

### SD-C Architecture
<img src="https://user-images.githubusercontent.com/107580325/176935832-4d35d1b6-1e12-4366-9548-885ae904bfa5.png" width="625" height="350">

(Image from SD-C Wiki)

> "SD-Core provides the 4G/5G connectivity and the SD-Core control plane at the central site controls multiple user plane components running at each Aether Edge site." \- from SD-C documentation
>
## SD-Fabric
> "SD-Fabric is an open source, full stack, deeply programmable network fabric optimized for edge cloud, 5G, and Industry 4.0 applications." - SD-Fabric Documentation

> "A network fabric describes the network topology in which components pass data to each other through interconnecting switches." - [IBM Documnetation](https://www.ibm.com/docs/en/flashsystem-9x00/8.2.x?topic=overview-network-fabrics)

[SD-Fabric Home Page](https://opennetworking.org/sd-fabric/)

[SD-Fabric Wiki](https://wiki.opennetworking.org/display/COM/SD-Fabric)

[SD-Fabric Documentation](https://docs.sd-fabric.org/master/index.html)]

- Uses bare metal switches, enables network verification and closed loop control, spine-leaf structure
- Scalable with varying topologies
- Plans to build a **Docker-based environment** so we could run Fabric without hardware. Otherwise we would have to buy the switches. Does this mean Aether can't run without the hardware in its current state?
- Programmable, API driven

### SD-Fabric Architecture
<img src="https://user-images.githubusercontent.com/107580325/177362988-a4e58943-9c81-46f0-af26-89a6d5866474.png" width="500" height="350"> <img src="https://user-images.githubusercontent.com/107580325/177368695-30a3f39c-e606-4a5c-8f00-fdf14313382b.png" width="200" height="350">

(Left image from SD-F Documentation, right image from SD-F Homepage)

## Attributes
- Has both a 5G and 4G core: Aether (and SD-C) build off of free5GC to create a "dual-mode solution" that supports both
  - also allows for standalone and non-standalone 5G connectivity
  - has two containerized User Plane Function so the core can process LTE and 5G signals simultaneously
- **SD-Core can be run as a separate entity from Aether for a simple mobile core**
- Deployment flexibility: network can be deployed completely centrally or distributed at the edge
- SD-Fabric is a vital component that Aether and SD-Core run on. **At the moment it looks like we would need to invest in hardware until they get a virtual environment**
- [Aether-in-a-Box](https://docs.sd-core.opennetworking.org/master/developer/aiab.html#aiab-guide) can be deployed on a simple computer then scaled up
- [gNB Simulator](https://docs.sd-core.opennetworking.org/master/developer/gnbsim.html) for testing the core?

