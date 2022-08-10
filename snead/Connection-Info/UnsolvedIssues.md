# Current Issues and Ideas to Fix

## Can connect to 4G, but not 5G using Telit modems

This is the biggest problem that could prevent us from intergrating the Waggle Nodes onto ANL's 5G network. Solving this issue is of highest priority. The following measures were taken to try to isolate the problem. 

We first made sure the tested SIM card was 5G capable by taking it from a verified 5G phone. When the SIm card was in the phone, it could connect to 5G both on and off ANL campus, and using the [Network Cell Info Lite & Wifi](https://play.google.com/store/apps/details?id=com.wilysis.cellinfolite) app, we were able to use the phone to find the strongest connection off campus. The phone being able to connect meant that the problem was not with the SIM card or a lack of 5G infrastructure in our area. 

We then put the SIM card into the Telit modem and connected it to the computer. Following the standard procedure listed in the [How To Connect](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md) page, we were able to connect to a network using the APN provided by the SIM card's provider. However, the ModemManager information was telling us that we were only connected to an LTE signal. Sending the following command

`qmicli --device=/dev/cdc-wdm0 -p --device-open-proxy  --dms-get-band-capabilities`

returned the following output:
```
[/dev/cdc-wdm0] Device band capabilities retrieved:
	Bands: 'wcdma-2100, wcdma-pcs-1900, wcdma-dcs-1800, wcdma-1700-us, wcdma-850-us, wcdma-800, wcdma-900, wcdma-1700-japan, wcdma-850-japan'
	LTE bands: '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43'
	LTE bands (extended): '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43, 46, 48, 66, 71'
```

Notice how no 5G bands are listed. The next thought was what band are we on and is it an overlap band?? fjdksafhjksd;a

## Jetson Nano and NX compatability



## 5G phones could not connect to the Nokia network


## `mmcli` Connection

A quick current problem is the establishment of a connection between the modem and ModemManager. We are currently unsure why it sometimes requires disconnecting and reconnnecting the USB cable to the modem for it to show up for `mmcli -L`, when `dmesg` shows it properly connected. This is a problem because the modems may need to be reset in the future during their installation, and ideally we would be able to do that remotely for a Waggle Node in the field, but this issue means someone would have to physically service the node to troubleshoot something. That being said, `mmcli` is not entirely necessary to connect to the network, as far as I'm aware. 

What's interesting about this is the assigned modem number will increase with each disconnect, even if the ModemManager did not recognize the modem, e.g. if I have to disconnect twice before the modem shows up the first time, the modem number will still be 2, instead of 0. It could be a problem with patience? 

There are no current ideas as to a solution for this; it's more of a hassle than an issue...

## 5G phones could not connect to the Nokia network

Nokia has been contacted. 


At the beginning of this research program, ANL's base station unit (BBU) was only serving a 4G network connected to Nokia Bell Labs' core. It was decently simple to achieve the first sub-goal with respect to 4G  by connecting the modems to a Linux laptop and accessing the network in the manner described in \textit{How to Connect to a Network} (\ref{sect:howtoconnect}). Two computers connected this way were able to ping each other and ping the BBU. The BBU was able to create an HTTP server that the computers could access. The network was unable to provide access to the internet due to restrictions placed by Argonne, so that is a permission problem, not a hardware or network problem. An issue was found where one Linux system could not connect to multiple modems at different times. At the time, this issue was assumed to be a SIM card problem because a 5G capable phone was also unable to connect, and Nokia was contacted. With current knowledge looking back, it could also have been that the modem's initial bearer APN was not set because ModemManager was able to communicate with the modem, but the computer could not get on the network, but this does not explain the problem with the phone. 

It was after this initial success that the ANL BBU and its radios started undergoing construction, which shut down the network. The process then shifted towards using a 5G capable AT\&T SIM card instead of the Nokia SIM to try achieve the sub-goals on a different network, the idea being that troubleshooting connectivity on a commercial network will make connecting to the ANL network faster when it starts working again. This shift meant starting over with the sub-goals.

At first, the modem showed itself to be getting a signal, but the computer was unable to connect to the network. The initial thought as to what the problem could be was an issue with the network to which it was trying to connect. {\tt qmicli}\footnote{All {\tt qmicli} commands are sourced from the QMICLI man page \cite{qmibib}} provides more network based control of modems and was used to gather more information. {\tt sudo qmicli -d /dev/cdc-wdm1 --device-open-proxy}, where {\tt cdc-wdm1} is the primary port listed from the ModemManager information output, is the base command that allowed the function to use to modem to get information and perform network surveys. For example, adding {\tt --nas-network-survey} to that base command showed a list of available networks,\footnote{If this command doesn't work, add {\tt --nas-force-network-search} to the base command instead, then retry}\footnote{Sample output in Appendix \ref{AppA}.} and {\tt --nas-set- preferred-networks= MCCMNC,access\_tech} allowed the modem to toggle between networks, but the computer still could not connect to any of the networks. Finally, by adding {\tt --nas-get-home-network}, it was seen that the home network was not one listed by the network search, and the SIM card later turned out to have been deactivated. 

\subsubsection{Modem connected to 4G but not 5G}
This is an ongoing problem that does not yet have a clear answer, but there are a couple things to try to help diagnose the problem. In the information supplied by ModemManager about the modem, check the section on Modes and make sure there is a mode that allows 5G, even better if one prefers 5G\footnote{If 5G not allowed, this is a problem with the ModemManager version. Check that it is 1.14.0 or higher.}. Check the ModemManager Documentation \cite{mmbib} on how to switch modes. An example of a command that could work is as follows:

{\tt mmcli -m 4 --set-allowed-modes="3g|4g|5g" --set-preferred-mode="5g"}
