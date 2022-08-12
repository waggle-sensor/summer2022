# Current Issues and Ideas to Fix

## Can connect to 4G, but not 5G, using Telit modems

This is the biggest problem that could prevent us from intergrating the Waggle Nodes onto ANL's 5G network. Solving this issue is of highest priority. The following measures were taken to try to isolate the problem. 

We first made sure the tested SIM card was 5G capable by taking it from a verified 5G phone. When the SIM card was in the phone, it could connect to 5G both on and off ANL campus, and using the [Network Cell Info Lite & Wifi](https://play.google.com/store/apps/details?id=com.wilysis.cellinfolite) app, we were able to use the phone to find the strongest connection off campus. The phone being able to connect meant that the problem was not with the SIM card or a lack of 5G infrastructure in our area. 

We then put the SIM card into the Telit modem and connected it to the computer. Following the standard procedure listed in the [How To Connect](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md) page, we were able to connect to a network using the APN provided by the SIM card's provider. However, the ModemManager information was telling us that we were only connected to an LTE signal. Sending the following command

`qmicli --device=/dev/cdc-wdm0 -p --device-open-proxy  --dms-get-band-capabilities`

returned the following output:
```
[/dev/cdc-wdm0] Device band capabilities retrieved:
	Bands: 'wcdma-2100, wcdma-pcs-1900, wcdma-dcs-1800, wcdma-1700-us, wcdma-850-us, wcdma-800, wcdma-900, wcdma-1700-japan, wcdma-850-japan'
	LTE bands: '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43'
	LTE bands (extended): '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43, 46, 48, 66, 71'
```

Notice how no 5G bands are listed. Since the 5G networks in the area are NSA, the next thought was could we be on a band that overlaps with 5G (i.e. the entended LTE bands) so the modem is just saying LTE when it could also mean 5G NSA. We used `socat` to send AT commands to the modem, and sent the follow two commands:

```
AT#5GLINKSTAT?
AT#LTEDS?
```

The first command told us that we were only connected to LTE, not 5G, and the second told us we were on band 30, which is not an extended band. 

We double checked the available modes listed for the modem by `mmcli -m 0` and made sure that it preferred 5G with the following command:

`mmcli -m 0 --set-allowed-modes='3g|4g|5g' --set-preferred-mode='5g'`

And even tried restricting the modem to only allow 5G, upon which the modem disconnected from the network completely. 

What's strange is we could get information about the 5G signal, as in the following, (though sometimes the 5G signal information would show up as N/A). 

```
# qmicli --device=/dev/cdc-wdm0 -p --device-open-proxy --nas-get-signal-info

[/dev/cdc-wdm0] Successfully got signal info
LTE:
	RSSI: '-70 dBm'
	RSRQ: '-12 dB'
	RSRP: '-97 dBm'
	SNR: '9.6 dB'
5G:
	RSRP: '-74 dBm'
	SNR: '16.5 dB'
	RSRQ: '-11 dB'
```

And using the next command, we can see that 5G NSA is available, so maybe the modem does not recognize a distinction between 4G and 5G NSA when connecting or setting preferences?

```
# qmicli --device=/dev/cdc-wdm0 -p --device-open-proxy --nas-get-system-info  

[/dev/cdc-wdm0] Successfully got system info:
	CDMA 1x service:
		Status: 'none'
		Preferred data path: 'no'
	CDMA 1xEV-DO (HDR) service:
		Status: 'none'
		Preferred data path: 'no'
	GSM service:
		Status: 'none'
		True Status: 'none'
		Preferred data path: 'no'
	WCDMA service:
		Status: 'none'
		True Status: 'none'
		Preferred data path: 'no'
	LTE service:
		Status: 'available'
		True Status: 'available'
		Preferred data path: 'no'
		Domain: 'cs-ps'
		Service capability: 'cs-ps'
		Roaming status: 'off'
		Forbidden: 'no'
		Cell ID: '54263189'
		MCC: '310'
		MNC: '410'
		Tracking Area Code: '16676'
		Voice support: 'no'
		IMS voice support: 'yes'
		eMBMS coverage info support: 'no'
		eMBMS coverage info trace ID: '65535'
		Cell access: 'all-calls'
		Registration restriction: 'unrestricted'
		Registration domain: 'not-applicable'
		5G NSA Available: 'yes'
		DCNR Restriction: 'no'
	TD-SCDMA service:
		Status: 'none'
		True Status: 'none'
		Preferred data path: 'no'
	5G SA service:
		Status: 'none'
		True Status: 'none'
		Preferred data path: 'no'
	SIM reject info: 'available'
```

We also tried the following, which confirms that the modem would prefer a 5G network:

```
# qmicli --device=/dev/cdc-wdm0 -p --device-open-proxy --nas-get-system-selection-preference

[/dev/cdc-wdm0] Successfully got system selection preference
	Emergency mode: 'no'
	Mode preference: 'lte, 5gnr'
	Disabled modes: 'none'
	Band preference: 'wcdma-2100, wcdma-pcs-1900, wcdma-dcs-1800, wcdma-1700-us, wcdma-850-us, wcdma-800, wcdma-900, wcdma-1700-japan, wcdma-850-japan'
	LTE band preference: '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43'
	LTE band preference (extended): '1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 29, 30, 32, 34, 38, 39, 40, 41, 42, 43, 46, 48, 66, 71'
	TD-SCDMA band preference: 'a, b, c, d, e, f'
	CDMA PRL preference: 'any'
	Roaming preference: 'any'
	Network selection preference: 'automatic'
	Service domain preference: 'cs-ps'
	GSM/WCDMA acquisition order preference: 'wcdma'
	Usage preference: 'data-centric'
	Voice domain preference: 'ps-preferred'
	Registration restriction: 'unrestricted'
	Acquisition order preference: '5gnr, lte, umts'
```

We have not yet been able to verifiy a connection to any 5G network. The current idea as to what could be happening is that there could be something wrong or out-of-date on the firmware of the Telit modems. Since the 5G phone could connect but the modem could not, that isolates the issue to a problem with the modem. A thought is to update the firmware and see if anything changes. I at least think it would be best to escalate this problem to Telit and ask if there is a misunderstanding or an issue.

## Jetson Nano and NX compatability

Currently, both the Jetson Nano and NX run on Ubuntu 18.04, which means there are limits on the ModemManager drivers that can control the modems; without any changes, the ModemManager version on Ubunutu 18.04 is 1.10.0, which is too old to properly control the Telit modem. On the Nano, I was able to make a custom build that ran ModemManager 1.14.0, but that was not recent enough to provide the proper drivers to enable `qmicli`. Additionally, when I was finally able to connect to the modem, the achievable network speeds were over 100 times slower than when the same modem-SIM set up was plugged into my laptop running Ubuntu 22.04. 

As for the Jetson NX, after mfollowing the same procedure to make a custom build of ModemManager, I was then unable to get to system to assign the modem the ttyUSB ports. This could be a problem with USB port splitter I was using, because it kept returning an error that the buffer was overflowing when it was trying to communicate to the ports. This could also be a problem with the general USB drivers in the system. 

Regardless, with both computers my recommendation would be to try to get a later version of Ubuntu running. [Jetpack 5.0](https://developer.nvidia.com/embedded/jetpack) would maybe allow that, but it is unclear from the developer previews. 

## 5G phones could not connect to the Nokia network

We noticed this problem right before construction on the server started, and do not yet have 5G capable phones to try again with. It's a little worrying, but possibly not applicable to connecting the Waggle Nodes. Nokia has been contacted about this issue.

## `mmcli` Connection

A quick current problem is the establishment of a connection between the modem and ModemManager. We are currently unsure why it sometimes requires disconnecting and reconnnecting the USB cable to the modem for it to show up for `mmcli -L`, when `dmesg` shows it properly connected. This is a problem because the modems may need to be reset in the future during their installation, and ideally we would be able to do that remotely for a Waggle Node in the field, but this issue means someone would have to physically service the node to troubleshoot something. That being said, `mmcli` is not entirely necessary to connect to the network, as far as I'm aware. 

What's interesting about this is the assigned modem number will increase with each disconnect, even if the ModemManager did not recognize the modem, e.g. if I have to disconnect twice before the modem shows up the first time, the modem number will still be 2, instead of 0. It could be a problem with patience? 

There are no current ideas as to a solution for this; it's more of a hassle than an issue...

## Unable to access the internet from ANL's network

This is a redtape issue with ANL. We believe we can get clearance to access the internet if we pull some strings. 

## Linux and Telit modems

Back in June, we had trouble getting Linux systems to connect to the networks. It was an issue where we could talk to the modems but not set up the network connection. The same modem allowed a Windows system to properly connect. This was after multiple successful connections on the same computer, but with a different modem. Upon retrying with the original modem it worked. At the time, we contacted Nokia about this issue, but looking back, it could have also been an issue with the initial bearer APN on that particular modem.  
