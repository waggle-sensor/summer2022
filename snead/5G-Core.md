# 5G Core Information
This is where I'm compiling my research about different open source 5G Core organizations. These include:
- [ONAP](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#onap)
- [free5GC](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#free5gc)
- [Aether](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#aether-onf) and [SD-Core](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#sd-core)
- [Magma](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#magma)
- [Open Air Interface 5G CN](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#open-air-interface-mosaic5g--5g-core-network)

Please also see my working [glossary](https://github.com/waggle-sensor/summer2022/blob/main/snead/5G-Core.md#glossary) at the end of this page
### Helpful 5GC Resources
- [UERANSIM](https://github.com/aligungr/UERANSIM) is a simulator that acts as a 5G mobile phone and base station to test 5G Cores 
- Explanation of [5G Core Architecture](https://www.digi.com/blog/post/5g-network-architecture)
- Quick dicussion of [PNF and VNF](https://www.linkedin.com/pulse/technology-analogy-physical-virtual-network-functions-milind-kulkarni/)

# ONAP

> "Open Network Automation Platform (ONAP) is an open source project hosted by the Linux Foundation. ONAP provides a comprehensive platform for real-time, policy-driven service orchestration and automation. ONAP enables service providers and developers to rapidly automate the instantiation and configuration of physical and virtual network functions and to support complete life cycle management activities." \- [ONAP](https://docs.onap.org/en/honolulu/index.html)

[ONAP Home Page](https://www.onap.org/)

[ONAP Documentation](https://docs.onap.org/en/honolulu/index.html#)

[Software and Hardware Requirements](https://docs.onap.org/projects/onap-oom/en/honolulu/oom_cloud_setup_guide.html#cloud-setup-guide-label)

### Sponsors / Contributors

ONAP is a Linux Foundation project with [contributing organizations](https://wiki.onap.org/display/DW/Membership) including Amdocs, AT&T, Bell Canada, Edgegap, Samsung, Nokia, Ericsson, Fujitsu, Orange, Huawei, Intel, IBM, NEC/Netcracker, Swisscom, TIM, Turk Telecom, Verizon, ZTE

## Architecture Notes

![ONAP-Notes](https://user-images.githubusercontent.com/107580325/176268551-013da326-381a-4dad-b308-e67f7bfd19b1.png "ONAP Architecture")

All pictures and information compiled from [ONAP's Architecture page](https://docs.onap.org/en/honolulu/guides/onap-developer/architecture/index.html)

## Integrating COTS Radios

So far it looks like mmWave Radios and our equipment can be controlled using an ONAP's SDN controller for ‘Radio’ (SDN-R), an additional service you can integrate into the run-time model. It's a part of their ONAP component, SDN-Controller. Once set up, the user could open the SDN-R portal and see which devices are connected (and manually mount radios, if needed). 
[SDNC Documentation](https://docs.onap.org/projects/onap-sdnc-oam/en/latest/index.html#master-index) is currently missing, so unsure?

![image](https://user-images.githubusercontent.com/107580325/176289800-2dbdf6bd-9397-4a30-9d91-4cc5e908bf1d.png)

Image from [ONAP SDN-R Documentation](https://docs.onap.org/projects/onap-ccsdk-features/en/honolulu/guides/onap-user/home.html)

[PNF Plug and Play Use Case](https://wiki.onap.org/display/DW/R8+PNF+Plug+and+Play+Use+Case) shows there is a method to register and operate Physical NF

[RAN-Sim Setup guide](https://wiki.onap.org/display/DW/RAN-Sim+setup) could be relevant to configuration. I think as long as you have the SDN-R config information you can connect RAN?
[Old 5G RAN Use Case](https://wiki.onap.org/display/DW/Use+case+proposal%3A+5G-+RAN+deployment%2C+Slicing%2C+SON)

## Edge Computing Capabilities

[Edge Automation use case](https://wiki.onap.org/display/DW/Edge+Automation+through+ONAP#EdgeAutomationthroughONAP-KeyPresentations:) is a case aimed at integrating existing edge architectures into ONAP. 

ONAP running [edge resources on K8S](https://wiki.onap.org/pages/viewpage.action?pageId=60889650) 

This use case outlines [goals for implementing cloud driven edge computing](https://wiki.onap.org/display/DW/Edge+Cloud+Infrastructure+Enablement+in+ONAP) and it was written in 2018, so maybe some of these goals are implemented?

## Attributes
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

## Reviews
This '[UBiqube article](https://ubiqube.com/onap-is-no-automation-panacea-quite-the-opposite-by-design/) thinks ONAP is overly complex, requires training to understand (I agree), with a high learning curve.

This was the only review I could find

# free5GC
An opensource 5G Core that can be used commercially without any licensing. To gain access to training, seminars, and tech support you must pay for [membership](https://www.free5gc.org/membership/)

[free5GC Home Page](https://www.free5gc.org/)

[free5GC Stage 3 GitHub](https://github.com/free5gc/free5gc-stage-3)

### Sponsors / Members

Members: Chungwa Telecom, Fujitsu, Open Networking Foundation (ONF), Edge-core Networks, Wistron NeWeb Corp. (WNC), EstiNet

Hardware Sponsors: Alpha Networks, Intel, Transnet, Advantech Moxa, Accton

Project Host and Main Contributor: Communication Service/software Lab at National Yang Ming Chiao Tung University

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

They have set up instructions for [connecting external RAN](https://github.com/free5gc/free5gc/wiki/Configuration#sample-configuration) and for connecting to [non-3GPP RAN](https://www.free5gc.org/installations/stage-3-free5gc/#b-run-the-n3iwf-individually)

## Edge Computing Capabilities

None that I can see? No mention of network slicing or edge computing abilities in UPF documentation. 

## Attributes
- Access to different versions in varying stages of 5G integration could be useful as Waggle begins migration to 5G
- After initial configuration, it seems ready to go "off the shelf," so to speak
- [Forum](https://forum.free5gc.org/) for asking questions!
- Pay wall (annual membership fee) for training and seminar access, but that's not too unique 
- run and managed entirely through Linux CLI
- Online videos and documentation for install and use

# Aether (ONF)
> "Aether is the first open source 5G Connected Edge platform for enabling enterprise digital transformation. It provides mobile connectivity and edge cloud services for distributed enterprise networks as a cloud managed offering. Aether is an open source platform optimized for multi-cloud deployments, and simultaneous support for wireless connectivity over **licensed, unlicensed and lightly-licensed (CBRS) spectrum."** \- Aether website

[Aether Home Page](https://opennetworking.org/aether/)

[Aether Dev Wiki](https://wiki.opennetworking.org/display/COM/Aether)

### Members / Contributors

[Members](https://opennetworking.org/member-listing/): AMD, ARM, AT&T, China Telecom, Cisco, Dell Technologies, Deutsche Telekom, GenXComm, Google, Intel, Microsoft, National Chiao Tung University, Nokia, Rutgers, Verizon, ADTRAN, Aerospace, Airhop Communications, Albot Technologies, Alibaba Group, Amdocs, Amirkabir University of Technology, APS Networks, Arista Networks, Asterfusion, Avesha, Bii, BISDN, Broadcom, Budapest University of Technology, C-DOT, Canopus Networks, China Mobile, China Unicom, Ciena, CNIT, CN Labs, Cohere Technologies, Comtrend, CPQD, Cumucore, Edge-Core, EURECOM, Excelacom, Far EasTone, FEI, FiberHome, FIT, Foxcomasia, Ganpat University, Genew Technologies, GS Lab, GTENT, Hawe Telekom, Infosys, Instituto de Telecomunicacoes, Iowa State, ITA, Kajeet, Kaloom, LabLabee, Lillyneir, Marvell, Merkator, NUS, NEC, Netsia, Neutroon, NGN Apps, NoviFlow, Northeastern University, NTT Group, Nvidia, Open Valley, Parallel Wireless, PalC Networks, Pathfinder Wireless, Pavonis, POSTECH, Purdue University, Qucomm, racksnet, Radisys, Reply, Rimedo Labs, Ruijie, Salient Global Technologies, Selta, Sercomm, Technische Universitat Ilmenau, SUTD, Smoptics, Sorbonne Universite, Sterlite Tech, Sunder Networks, T1 Nexus, Tech Mahindra, Tetrate, TIM, Turk Telecom, Turkcell, Universidade de Aveiro, Universita Deglia Studi Dell’Aguila, Universitat Politecnica de Valencia, University of Bristol, UC San Diego, University of Colorado Boulder, University of Ottawa, U. of Surrey, University of Utah, University of Waterloo, Vector Data, Venko Networks, Virginia Tech, Vodafone, Wiwynn, YADRO, ZTE, Zyxel Communications

<img src="https://user-images.githubusercontent.com/107580325/179571256-cf34baed-4e1f-44b9-8cd1-aa9ece3a6fe8.png" height="300" width="600">

[Full Collaborator list here](https://opennetworking.org/collaborators/). 

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

### SD-C Connection to COTS Radios and RAN
[Test cases for RAN Emulator](https://docs.sd-core.opennetworking.org/master/testing/sdcore_testing.html)

SD-Core is [compliant](https://docs.sd-core.opennetworking.org/master/overview/3gpp-compliance-5g.html?highlight=ran) with UE registration and de-registration, NRF NF registration. Otherwise, it is vague how you would connect

[Config with SimApp](https://docs.sd-core.opennetworking.org/master/configuration/config_simapp.html) has a section about gNB names?

[WebConsole](https://github.com/omec-project/webconsole) facilitates communication to NFs and manages configuration. I think this is where we would find out

[gNB Simulator](https://github.com/omec-project/gnbsim#readme)

### Edge Computing Capability

Advertised: "Hardware-based P4 and software (containeried) UPFS can be intermixed for different application/use cases running in edge clouds" \- from [SD-Core Home page](https://opennetworking.org/sd-core/)

Has multiple [UPF variations](https://docs.sd-core.opennetworking.org/master/overview/architecture.html#multiple-distributed-user-planes) that are assigned to users upon registration with the AMF. ONF's ROC allows for management of APIs that manage [network slices](https://docs.sd-core.opennetworking.org/master/overview/architecture.html#network-slicing). "The behavior of each slice is configurable and can be dynamically changed during run time... Network slice selection is achieved through 3GPP-specified network functions like Network Slice Selection Function (NSSF) and Network Repository Function (NRF)."

"It is possible to deploy all components of SD-Core collocated in an edge cloud or a central cloud for private consumption. It is also possible to distribute the components of SD-Core across multiple clouds, edge and central, to deliver a cloud-managed multi-tenant connectivity service... SD-Core’s hybrid cloud deployment is an important enabler for a managed 4G/5G connectivity service where each customer site may be deployed to serve a different set of use cases and may have different types of underlying cloud environments."

<img src="https://user-images.githubusercontent.com/107580325/180821928-17f53b01-56ae-4aac-afdc-e43f7d64f11a.png" height="250" width="450">

## SD-Fabric
> "SD-Fabric is an open source, full stack, deeply programmable network fabric optimized for edge cloud, 5G, and Industry 4.0 applications." - SD-Fabric Documentation

> "A network fabric describes the network topology in which components pass data to each other through interconnecting switches." - [IBM Documnetation](https://www.ibm.com/docs/en/flashsystem-9x00/8.2.x?topic=overview-network-fabrics)

[SD-Fabric Home Page](https://opennetworking.org/sd-fabric/)

[SD-Fabric Wiki](https://wiki.opennetworking.org/display/COM/SD-Fabric)

[SD-Fabric Documentation](https://docs.sd-fabric.org/master/index.html)

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

# Magma

[Magma Home Page](https://magmacore.org/)

[Magma Documentation](https://docs.magmacore.org/docs/basics/introduction.html)

[Software Requirements](https://docs.magmacore.org/docs/basics/prerequisites#prerequisites) and [Hardware Requirements](https://docs.magmacore.org/docs/basics/prerequisites#production-hardware) including needs for Access Gatewas and RAN 

### Sponsors / Contributors

[Members](https://magmacore.org/members/): ARM, Meta, Qualcomm, Red Hat, 0Chain, Aarna Networks, Advanced Micro Devices (AMD), Althea, AQSACOM, Canonical Group Limited, Connect 5G, Inc., Ecrio, FreedomFi, Helium Systems, Inc., Highway9 Networks, Platform9 Systems, Inc., RADTONICS, Sempre.ai, Teal Communications, Inc., Telaverge Communications, Wavelabs Technologies Private Limited, Whitestack LLC, ZEDEDA, Inc., OpenStack, OpenAirInterface Software ALliance, free5GC, University of Delhi

<img src="https://user-images.githubusercontent.com/107580325/179582095-4b234350-5b9f-44be-a2bf-6d35fbdced5c.png" height="100" width="550">

## Architecture

![magma Architecture](https://user-images.githubusercontent.com/107580325/177576609-2ef4e7ff-cf21-493e-9e12-898dfa895f73.png) 
(Image and following decription from Magma documentation)

- **Access Gateway (AGW):** provides network services and policy enforcement. In an LTE network, the AGW implements an evolved packet core (EPC), and a combination of an AAA and a PGW. It works with existing, unmodified commercial radio hardware.
  - <img src="https://user-images.githubusercontent.com/107580325/177583060-e7e32f2e-e912-4d1f-845f-a690a783e27a.png" width="300" height="350">
  - _enodebd_ manages eNBs (supports TR-069 management interface), _mobilityd_ manages subscriber mobility, _control_proxy_ proxies control-plane traffic between AGW and Orch., _magmad_ parent service that orchestrates all others, for more info on all services see the [AGW docs](https://docs.magmacore.org/docs/lte/architecture_overview#architecture-overview)
- **Orchestrator (Orch8r):** configures and monitors the network, and can be hosted publicly or privately. [Magma web UI (NMS)](https://docs.magmacore.org/docs/nms/nms_arch_overview#overview) allows access to analytics and other info. Composed of two components
  - A standardized, vendor-agnostic northbound REST API which exposes configuration and metrics for network devices
  - A southbound interface which applies device configuration and reports device status
  - <img src="https://user-images.githubusercontent.com/107580325/177586755-e423cddc-0f93-40f9-95e6-c9c4ea59048e.png" width="350" height="300">
  - Network entity configuration (networks, gateway, subscribers, policies, etc.), metrics querying via Prometheus and Grafana, event and log aggregation via Fluentd and Elasticsearch Kibana, config streaming for gateways, subscribers, policies, etc., device state reporting (metrics and status), request relaying between access gateways and federated gateways
  - Supports some [extensions](https://docs.magmacore.org/docs/orc8r/architecture_modularity#overview) to functionality that can either push data out to or recieve data from core services
  - For more detailed info, see [Orch8r docs](https://docs.magmacore.org/docs/orc8r/architecture_overview#architecture-overview)
- **Federation Gateway (FeG):** integrates the Mobile Network Provider (MNO) core network with Magma by using standard 3GPP interfaces to existing MNO components. It acts as a proxy between the Magma AGW and the operator's network and facilitates core functions, such as authentication, data plans, policy enforcement, and charging to stay uniform between an existing MNO network and the expanded network with Magma.
- **Domain Proxy (DP):** Vendor neutral Domain Proxy serves as a single point of contact for eNB-SAS communication for private networks using Magma as the Operator Core. Without a Domain Proxy an eNB has to request for SAS Spectrums/Grants on its own, which is not typical. 
	- <img src="https://user-images.githubusercontent.com/107580325/177859453-3041edb2-4bb6-4f76-946a-b3088dec0414.png" width="600" height="300">

## Deploying for 5G

Must partner with [Wavelabs](https://magmacore.org/wavelabs/) or [Radtonics](https://www.radtonics.com/) to deploy Magma for 5G. 

<img src="https://user-images.githubusercontent.com/107580325/178586161-9423e068-ef77-44e9-b0a0-c6c1e9d6c880.png" height="200" width="450">

(Image from Magma Wavelab Page) 

Current Wavelab Magma 5G Capabilities (as of Jan 2022):
- Registration, 5G specific authentication, PDU session estab., idle mode paging, service request, UE init. session release and de-registration, dynamic policy support & 5G QOS, usage reporting & charging
  - pulled from this [video](https://youtu.be/KkNp3vJZc24?t=1837) that you can watch for more info (here's the [GitHub link](https://github.com/magma/magma/tree/80493f7c96a5500063f1f57e2962ea9f7da624b8/lte/gateway/c/core/oai/tasks) he talks about at [45:00](https://youtu.be/KkNp3vJZc24?t=2699))
- as of Feb 2022 (?): stateless network function, basic IPv6 support, network initiated session modification
- [Future Dev](https://youtu.be/ynsORXa_OI8)
  - not yet implemented network slicing (talking to ONAP community to learn more, unsure when it will be available
  - some implemented [private network use cases](https://youtu.be/ynsORXa_OI8?t=2058)
- Wavelab has a Slack you can join with a dedicated 5G support channel

### Connecting to COTS Radios and such

[5G NSA support](https://docs.magmacore.org/docs/howtos/5g_nsa_support#5g-nsa-support) documented here, interfaces are compliant with 3GPP so should be good to set up COTS radios.

enodebd service in AGW manages eNBs (compatible with TR-069 management interface) but unsure about connection to 5G RAN equipment. They have tested with the following [eNBs](https://docs.magmacore.org/docs/basics/prerequisites#ran-equipment):
- Baicells Nova 233 TDD Outdoor
- Baicells Nova 243 TDD Outdoor
- Assorted Baicells indoor units (for lab deployments)

[UE Sim to test gateways](https://docs.magmacore.org/docs/next/lte/s1ap_tests)

In Domain Proxy [docs](https://docs.magmacore.org/docs/dp/architecture_overview), it looks like most of the radio interface is 4G based, so will have to see at the Wavelabs 5G webinar.

### Edge Computing Capabilities

None listed that I can see. They are looking into network slicing in the next 18 months, but that doesn't necessarily mean ability to perform edge computing.

## Attributes

- Part of the Linux Foundation
- [Training!](https://training.linuxfoundation.org/training/introduction-to-magma-cloud-native-wireless-networking-lfs166x/)
- Does not run on windows. macOS preferred, also runs on Ubuntu
- "Add capacity and reach by using Wi-Fi and CBRS even when constrained with licensed spectrum." - Magma Home Page
  - yet to find anything to this end
- Built for service providers: what does that mean?
  - AGW is built to interface with a preexisting LTE Gateway (is this required?)
- Looks like it is originally built to interface with LTE systems as a means to create a 5G-like system that controls 4G so transitioning to 5G would be easier 
  - it says with it just takes some adjustment to use RAN 
- Orchestrator usually runs on AWS but can be deployed on a provate cloud on existing Kubernetes cluster

# Open Air Interface Mosaic5G & 5G Core Network

### Members

Open Air Interface is founded by Eurecom. The National Science Foundation (NSF) has also [announced the creation of OpenAirX-Labs (OAX)](https://www.prnewswire.com/news-releases/national-science-foundation-funded-platforms-for-advanced-wireless-research-project-office-announces-launch-of-openairx-labs-oax-to-accelerate-development-and-testing-of-an-open-source-5g-standalone-software-stack-301304723.html) to help testing of OAI's 5G research. 

[Members](https://openairinterface.org/osa-members/): Orange, Platforms for Advanced Wireless Research, XILINX, NI, Qualcomm, Meta, Sequans, Nokia Bell Labs, fujitsu, Interdigital, Firecell, Kyocera, Ulak Haberlesme A.S., Developing Solutions, HTP, B-yond, Zengyi TEchnology, allbesmart, Red Hat, Inmarsat, Dolcera, Benetel, Innogence Technology, ID Tolu, Wilab, BINJ Laboratories, ZaiNar, iDAQS, CPQD, Hytec Inter Co., Ltd., FibroLAN, and universities in the UK, China, USA, Spain, Germany, Poland, Czech Republic, and India 

## Mosaic5G (M5G)

> "The newly created MOSAIC5G (M5G) PROJECT GROUP aims to transform radio access (RAN) and core networks (CN) into agile and open network-service delivery platforms. Such a platform allows for exploring new use-cases of interest to different vertical industries. Mosaic5G introduces the world’s first ecosystem of 5G R&D open source platforms ranging from the centralized network control to the mobile edge network deployment." - from M5G Home

[Mosaic Home](https://openairinterface.org/mosaic5g/)

[Mosaic Gitlab](https://gitlab.eurecom.fr/mosaic5g) (in the gitlab for each component there are docs for installation, not much else, information-wise)

### M5G Architecture

<img src="https://user-images.githubusercontent.com/107580325/178587171-b8313a9a-0e63-46d3-9348-dc07897e1909.png" height="250" width="475"> <img src="https://user-images.githubusercontent.com/107580325/178587526-9dd3ffe2-6348-4b8c-840d-b213712168f1.png" height="250" width="450">

(Images from Mosaic Home)

As it looks right now, only FlexCN and FlexRIC are ready to try, though not fully implemented. In May of 2021, Mosaic5G was adopted as a project group by OAI and is being integrated to control OAI's existing core and RAN infrastructure, so it might take a while before it's operational

### FlexRIC

> "FlexRIC is short for “Flexible RAN Intelligent Controller”. It interfaces with the OAI radio stack over the O-RAN-defined E2-interface to monitor and control the RAN in real-time." - from Mosaic home page

[Demo of FlexRIC](https://youtu.be/k2JDPBKCcNM) that shows some slicing and control of OAI RAN

### Slicing and Edge Computing

FlexRIC can "perform slicing control at a NSA 5G network" in this [demo](https://youtu.be/k2JDPBKCcNM). It looks like FlexRIC can be used to control what radio resources go to what UE, but not slicing as a means to create different use cases and enable edge computing. 

## 5G CN

> "The scope of 5G CN project developments is to deliver a 3GPP compliant 5G Core Network under the OAI Public License V1.1. OpenAirInterface CN 5G project is one of the main projects under OSA’s umbrella. The main objective is to develop a fully 3GPP compatible 5G CN stack as an open-source software for the OAI community. In the scope of this project, we focus only on Standalone Mode." - OAI 5G Page 

[OAI 5G CN Home](https://openairinterface.org/oai-5g-core-network-project/)

[OAI 5G Gitlab](https://gitlab.eurecom.fr/oai/cn5g)

### Architecture

![OAI 5G Architecture](https://user-images.githubusercontent.com/107580325/177624977-d32e45e8-57c2-435f-9e31-a7c1c21c2dca.png)  
(Image from OAI 5G Home Page)

![Future Development Roadmap](https://user-images.githubusercontent.com/107580325/177625214-77bd317f-5bcc-43a9-9b1c-dd4b465c6018.png) 
(Future Development Roadmap, Image from OAI 5G Home Page)

## Attributes

- runs on Ubuntu
- has most 5G functionalities tested, missing some as can be seen from the 5G CN architecture picture
	- Overall, I think this is missing components that would make it understandable or usable at the current moment, but if we are willing to wait another year or so, the stack looks well thought out so far... where's the shrug emoji when you need it...
- Little documentation on installation of each piece, not much on how to run this (I'm unsure it can be run at all?)
- As far as I can tell, built to work with their preexisting [RAN](https://openairinterface.org/oai-5g-ran-project/) which looks pretty robust upon first inspection (?)
	- but if it is 3GPP compliant we should be able to interface with COTS radios... unclear

# Glossary

**AMF:** Access and Mobility Management Function, receives all session and connection related info from the UE. Forwards session info to SMF <br>
**AUSF:** Authentication Server Function, receives authentication requests from AMF, works with UDM to mkae sure a User can gain access <br>
**MNO:** Mobile Network Operator, the companies, usually <br>
**N3IWF:** Non-3GPP Interworking Function <br>
**NRF:** Network function Repository Function, provides record of all NFs available <br>
**NSSF:** Network Slice Selection Function  <br>
**PCF:** Policy Control Function  <br>
**PNF:** Physical Network Function, most radios and physical equipment  <br>
**RAN:** Radio Access Network, series of cllular connection nodes <br>
**SAS:** Spectrum Access System <br>
**SMF:** Session Management Function  <br>
**UDM:** Unified Data Management  <br>
**UDR:** Unified Data Repository  <br>
**UE:** User Equipment, e.g. phones, modem, cars
**UPF:** User Plane Function  <br>
**URLLC:** Ultra-Reliable Low Latency Connection <br>
**VNF:** Virutal Network Function, cloud based or otherwise virtual version of NFs <br>  
