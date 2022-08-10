# How to Connect to a Network

**Note:** All `mmcli` commands are from the [ModemManager man page](https://www.freedesktop.org/software/ModemManager/man/1.0.0/mmcli.8.html)

ANL is using Telit's FN980m 5G capable modems. The primary OS used on the computers connected to the modems is Ubuntu 20.04 and above ([using ealier version?](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/Debugging.md#running-earlier-version-of-ubuntu)). The Telit modems connect to computers using a USB-C port on the front of the upper board of the modem (we have been using a USB-C to USB cable). Once connected, open a terminal and enter `sudo dmesg`, which should show that the modem is connected and the ports are attached to ttyUSBs ([sample output](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md#input-sudo-dmesg)).

Next, enter the ModemManager command `mmcli -L` to search for the modem. If no modems show up after a while, try disconnecting and reconnecting the USB cable. Sample output:

`     /org/freedesktop/ModemManager1/Modem/0 [Telit] FN980m`

The final number in the file path is how the modem will be specified when using ModemManager controller. In this case, sending `mmcli -m 0` should return information about the hardware, capabilities, and connection status of the modem ([sample output](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md#input-mmcli--m-0)). 

Towards the bottom of the output information, it should list the initial bearer APN, which needs to match the APN of the desired network. To set this configuration, check the listed ports in the ModemManager output. The first listed port followed by `(at)` is the port through which AT commands can be sent to the modem (usually, this port is ttyUSB2). Enter `sudo socat - /dev/ttyUSB2,crnl` and send the modem the command `AT+CGDCONT=1,"IP","[insert APN]"` with the desired APN inserted where specified. Exit the `socat` command and resend `mmcli -m 0`; it should now show the desired APN in the initial bearer section. If not, power cycle the modem and reconnect.

The modem should now be ready to set up a new mobile broadband connection through the network settings on the computer. You will need to enter the same APN that you set for the modem in the connection setup wizard. To test your connection, try pinging the server IP address to check that you're on the network. Try pinging a website to check that the computer can access the internet. Disconnect from WiFi and send the command `speedtest` to check download and upload speeds. The following command will return more signal info (`cdc-wdm1` is the primary port of the modem) ([sample output](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/HowToConnect.md#input-sudo-qmicli--d-devcdc-wdm0--p---device-open-proxy---nas-get-signal-info)). 

`sudo qmicli -d /dev/cdc-wdm0 -p --device-open-proxy --nas-get-signal-info`

If there are any other problems, see the [debugging section](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/Debugging.md).

## Sample Outputs

### Input: `sudo dmesg`

```
[20650.685345] usb 2-1: new high-speed USB device number 13 using xhci_hcd
[20650.834874] usb 2-1: New USB device found, idVendor=1bc7, idProduct=1050, bcdDevice=4.14
[20650.834881] usb 2-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[20650.834884] usb 2-1: Product: FN980m
[20650.834886] usb 2-1: Manufacturer: Telit Wireless Solutions
[20650.834887] usb 2-1: SerialNumber: 378d1438
[20650.843981] option 2-1:1.0: GSM modem (1-port) converter detected
[20650.844125] usb 2-1: GSM modem (1-port) converter now attached to ttyUSB0
[20650.845297] qmi_wwan 2-1:1.2: cdc-wdm1: USB WDM device
[20650.845958] qmi_wwan 2-1:1.2 wwan0: register 'qmi_wwan' at usb-0000:00:14.0-1, WWAN/QMI device, ea:fc:5e:67:16:08
[20650.846166] option 2-1:1.3: GSM modem (1-port) converter detected
[20650.846305] usb 2-1: GSM modem (1-port) converter now attached to ttyUSB1
[20650.846725] option 2-1:1.4: GSM modem (1-port) converter detected
[20650.847322] usb 2-1: GSM modem (1-port) converter now attached to ttyUSB2
[20650.847512] option 2-1:1.5: GSM modem (1-port) converter detected
[20650.847648] usb 2-1: GSM modem (1-port) converter now attached to ttyUSB3
[20650.847811] option 2-1:1.6: GSM modem (1-port) converter detected
[20650.847914] usb 2-1: GSM modem (1-port) converter now attached to ttyUSB4
```

### Input: `mmcli -m 0`

```
  ----------------------------------
  General  |                   path: /org/freedesktop/ModemManager1/Modem/0
           |              device id: a407fbb1a3c8f20c8b6f875dd9eff91843019a27
  ----------------------------------
  Hardware |           manufacturer: Telit
           |                  model: FN980m
           |      firmware revision: M0H.020001
           |         carrier config: default
           |           h/w revision: 0.00
           |              supported: gsm-umts, lte, 5gnr
           |                         cdma-evdo, lte, 5gnr
           |                         lte, 5gnr
           |                         cdma-evdo, gsm-umts, lte, 5gnr
           |                current: lte, 5gnr
           |           equipment id: 350313452018685
  ----------------------------------
  System   |                 device: /sys/devices/pci0000:00/0000:00:14.0/usb2/2-1
           |                drivers: qmi_wwan, option
           |                 plugin: telit
           |           primary port: cdc-wdm1
           |                  ports: cdc-wdm1 (qmi), ttyUSB0 (ignored), ttyUSB1 (ignored)
           |                         ttyUSB2 (at), ttyUSB3 (at), ttyUSB4 (ignored), wwan0 (net)
  ----------------------------------
  Numbers  |                    own: 12253281183
  ----------------------------------
  Status   |                   lock: sim-pin2
           |         unlock retries: sim-pin (3), sim-puk (10), sim-pin2 (3), sim-puk2 (10)
           |                  state: registered
           |            power state: on
           |            access tech: lte
           |         signal quality: 83% (recent)
  ----------------------------------
  Modes    |              supported: allowed: 4g; preferred: none
           |                         allowed: 5g; preferred: none
           |                         allowed: 4g, 5g; preferred: 5g
           |                         allowed: 4g, 5g; preferred: 4g
           |                current: allowed: 4g, 5g; preferred: 5g
  ----------------------------------
 Bands     |              supported: utran-1, utran-3, utran-4, utran-6, utran-5, utran-8, 
           |                         utran-9, utran-2, eutran-1, eutran-2, eutran-3, eutran-4, eutran-5,
           |                         eutran-7, eutran-8, eutran-12, eutran-13, eutran-14, eutran-17,
           |                         eutran-18, eutran-19, eutran-20, eutran-25, eutran-26, eutran-28,
           |                         eutran-29, eutran-30, eutran-32, eutran-34, eutran-38, eutran-39, 
           |                         eutran-40, eutran-41, eutran-42, eutran-43, eutran-46, eutran-48, 
           |                         eutran-66, eutran-71, utran-19
           |                current: utran-1, utran-3, utran-4, utran-6, utran-5, utran-8,
           |                         utran-9, utran-2, eutran-1, eutran-2, eutran-3, eutran-4, eutran-5, 
           |                         eutran-7, eutran-8, eutran-12, eutran-13, eutran-14, eutran-17, 
           |                         eutran-18, eutran-19, eutran-20, eutran-25, eutran-26, eutran-28, 
           |                         eutran-29, eutran-30, eutran-32, eutran-34, eutran-38, eutran-39, 
           |                         eutran-40, eutran-41, eutran-42, eutran-43, eutran-46, eutran-48, 
           |                         eutran-66, eutran-71, utran-19
  ----------------------------------
  IP       |              supported: ipv4, ipv6, ipv4v6
  ----------------------------------
  3GPP     |                   imei: 350313452018685
           |          enabled locks: fixed-dialing
           |            operator id: 310410
           |          operator name: AT&T
           |           registration: home
  ----------------------------------
  3GPP EPS |   ue mode of operation: csps-2
           |    initial bearer path: /org/freedesktop/ModemManager1/Bearer/4
           |     initial bearer apn: broadband
           | initial bearer ip type: ipv4
  ----------------------------------
  SIM      |       primary sim path: /org/freedesktop/ModemManager1/SIM/3
           |         sim slot paths: slot 1: /org/freedesktop/ModemManager1/SIM/3 (active)
           |                         slot 2: none
```

## Input: `sudo qmicli -d /dev/cdc-wdm0 -p --device-open-proxy --nas-get-signal-info`

```
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
