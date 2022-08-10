# Debugging: Common Problems and Solution Ideas

This document details problems I encountered for which I was able to find solutions. If you cannot find your problem here, it might be in the file on [current problems](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/UnsolvedIssues.md) that might not have clear solutions. All `mmcli` and `qmicli` commands come from the [ModemManager man page](https://www.freedesktop.org/software/ModemManager/man/1.0.0/mmcli.8.html) and [QMICLI man page](https://www.freedesktop.org/software/libqmi/man/latest/qmicli.1.html), respectively.

### Modem cannot be found by ModemManager

Try disconnecting and reconnecting the USB cable to the modem, or power cycling the modem. Be patient as it sometimes takes a while to register properly with ModemManager. `watch mmcli -L` will resend the list command every 2 seconds so the modem will pop up as soon as it's ready. This could also mean the SIM card is not being properly read by the modem, so make sure it is properly inserted.

### Modem getting signal, but computer can't connect to network

This could be a number of problems. Using `mmcli -m #`, where `#` is the assigned number of the modem, check that the initial bearer APN is the APN of your network. If not, enter `sudo socat - /dev/ttyUSB2,crnl` into the terminal and send the AT command `AT+CGDCONT=1,"IP","[insert APN]"` to the modem to switch the APN. In your Mobile Network Settings, clear out any previous connections and retry setting up this connection. 

If that does not help, at worst, this could be a problem with the SIM card itself. Send these three commands, where `cdc-wdm1` should be the primary port listed in the `mmcli -m #` output (could also be something ending in `wwan0`) (if not, [ModemManager is likely out of date](https://github.com/waggle-sensor/summer2022/blob/main/snead/Connection-Info/Debugging.md#modem-ports-not-assigned-to-ttyusb) and `qmicli` will not work):

```
sudo qmicli -d /dev/cdc-wdm1 --device-open-proxy --nas-force-network-search
sudo qmicli -d /dev/cdc-wdm1 --device-open-proxy --nas-network-scan
sudo qmicli -d /dev/cdc-wdm1 --device-open-proxy --nas-get-home-network
```

If the output of `--nas-get-home-network` contains a network MCCMNC that is _not_ listed in the output of `--nas-network-scan`, the SIM card is most likely not cleared to roam, or is not activated on current available networks. Double check that the SIM card in use is activated and cleared to connect to the desired network. When I faced this problem, I used the following command to force the modem onto a particular network and then toggle between them, but it didn't work. You are welcome to try. Replace `310410,lte` with the MCCMNC and access technology of the found networks.

`sudo qmicli -d /dev/cdc-wdm1 --device-open-proxy --nas-set-preferred-networks=310410, lte`

### Trouble pinging other UEs on the network

Check the firewall settings on the computer and make sure it can be discovered on this network.

### Running earlier version of Ubuntu

The only things this issue affects are `mmcli` and `qmicli`, which will be running out-of-date versions. If using Ubuntu 18.04, use the following link to download a more up to date version: [https://launchpad.net/~aleksander-m/+archive/ubuntu/modemmanager-bionic](https://launchpad.net/~aleksander-m/+archive/ubuntu/modemmanager-bionic). Otherwise, try a custom build to get a version of ModemManager that is 1.14.0 or later. A version of `mmcli` earlier than 1.18.0 will not have the correct drivers to allow the use of `qmicli`, but that function is not extremely necessary.

### Modem ports not assigned to ttyUSB

This is most likely a problem with the driver for the modem, which is a part of ModemManager. Check that ModemManager is version 14.0 or higher with `mmcli --version`. 
