Welcome to my README!
----------------------


<b>Overall Objective:</b> To demonstrate a real scientific workflow using a Waggle node connected via 5G CBRS to a Multi-access Edge Computing (MEC) resource.

<b>Tasks:</b>

<ol>
 <li>Integrate Waggle Blade with Argonne’s private 5G network as an MEC resource (Waggle Edge-Blade)</li>
 <li>Complete installation of Argonne’s 5G testbe MEC server:
 <ol style="list-style-type: lower-alpha; padding-bottom: 0;">
  <li style="margin-left:2em">Test connectivity, verify remote access, install tools such as Kubernete, etc.</li>
  <li style="margin-left:2em; padding-bottom: 0;">Optionally, port the software of Waggle Blade</li>
 </ol>
 </li>
 <li>Integrate Waggle nodes on Argonne’s 5G network with MEC resources and show demo.</li>
 <li>Investigate how to integrate Open RAN into an existing 5G core.</li>
</ol>


<b>Other tasks:</b>
<ol>
<li>Complete integration of 5G core with router and MEC server</li>

<li>Configure and evaluate Nokia OSS MediatorCollector API https://use.dac.nokia.com/nokia-dac-oss/nokia-dac-oss-mediator-collector-configuration</li>
</ol>



<h1><b>Summary: </b></h1>

<h3><b>Open Source RAN</b></h3>

In an Open RAN environment, the RAN is disaggregated into three main building blocks:
<ul>
  <li>the Radio Unit (RU)
</li>
  <li>the Distributed Unit (DU)
</li>
  <li>the Centralised Unit (CU)
</li>
</ul>

The RU is where the radio frequency signals are transmitted, received, amplified, and digitized. The RU is located near or integrated into, the antenna. The DU and CU are the computation parts of the base station, sending the digitalized radio signal into the network. The DU is physically located at or near the RU whereas the CU can be located nearer the Core.

The key concept of Open RAN is “opening” the protocols and interfaces between these various building blocks (radios, hardware, and software) in the RAN. 

<hr>

<b>Airspan</b>

OpenRANGE vCU key benefits:

<ul>
  <li>Enables interworking with MEC applications through Radio Network Information Service (RNIS) API
</li>
  <li>Segregated user plane/control plane support (over E1AP) maximizes cost efficiency (resource pooling)
</li>
  <li>High-availability support
</li>
</ul>


OpenRANGE vDU key benefits:

<ul>
  <li>SDN based L2 transport capabilities enables support for transport network slicing

</li>
  <li>Sliceable L2 architecture enables support for RAN network slicing

</li>
  <li>L1/L2 aggregation enabling inter RU carrier aggregation and multipoint transmission schemes

</li>
</ul>


<hr>

<b>Casa Systems</b>

key benefits:
<ul>
  <li>Deliver true gigabit per second speeds across both mid-band and millimeter wave frequencies.
</li>
  <li>Deploy on premise or in the cloud for lower latency
</li>
  <li>Support deployments as small as 10K square feet and up to 1M square feet
</li>
  <il>Enable network components to work together seamlessly
</li>
  <li>Avoid vendor lock-in and support the ideal mix of hardware and software solutions
</li>
  <li>Support multi-vendor deployments for a more competitive, vibrant ecosystem
</li>
  
 <hr>
</ul>

<b>Radisys</b>

key benefits:

<ul>
  <li>The software is based on 3GPP Release 15 with upcoming support for Release 16 and Release 17.
</li>
  <li>offer a high-performance and feature-rich complete software package that is fully interoperable for multi-vendor Open RAN deployments in public and private network deployments.
</li>
  <li>Radisys O-RAN Protocol software solution provides complete control/user plane separation, integration through open interfaces with RAN Intelligent controllers (RICs) and application of AI/ML through various xApps per O-RAN architecture.
</li>

</ul>
 <hr>
 
Access the full open source RAN research: <a href="https://docs.google.com/document/d/1aRn2xVmkS2u5RtlqUbxxVOrsKDpVYHVFu83ZWkVf1sU/edit?usp=sharing">click here</a>

Access the open source decision matrix: <a href="https://github.com/waggle-sensor/summer2022/blob/main/Ziad/5g_o-ran_decision_matrix.pdf">click here</a>



<h3><b>MEC resources:</b></h3>
<ul>
  <li>HTTP server</li>
  <li>apache server</li>
  <li>file transfer server</li>
  <li>SSH server</li>
  <li>docker</li>
  <li>Kubectl</li>
  <li>k3d</li>
</ul>

Access the set up instructions: <a href="https://github.com/waggle-sensor/summer2022/blob/main/Ziad/MEC_server_resources.md">click here</a>
