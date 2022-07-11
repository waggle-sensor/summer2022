NVIDIA JETSON LINUX DRIVER PACKAGE QUICK START GUIDE

The information here is intended to help you get started quickly using the NVIDIAÂ® Jetsonâ„¢ Linux
Driver Package (L4T) in conjunction with an NVIDIA Jetson developer kit.

TYPES AND MODELS OF JETSON DEVICES

Both Jetson modules and Jetson developer kits are available from NVIDIA. A Jetson developer kit
includes a non-production specification Jetson module attached to a reference carrier board. You
can use it with JetPack SDK to develop and test software for your use case. Jetson developer kits
are not intended for production use.

Jetson modules are suitable for deployment in a production environment throughout their operating
lifetime. Each Jetson module ships with no software pre-installed; you attach it to a carrier board
designed or procured for your end product and flash it with the software image you have developed.

This release of L4T supports the following Jetson devices:

1. NVIDIA Jetson AGX Xavierâ„¢ series modules and Jetson AGX Xavier Developer Kit

2. NVIDIA Jetson Xavierâ„¢ NX module and Jetson Xavier NX Developer Kit

3. NVIDIA Jetson TX2 series modules and Jetson TX2 Developer Kit

4. NVIDIA Jetson TX1 module and Jetson TX1 Developer Kit

5. NVIDIA Jetson Nanoâ„¢ module and Jetson Nano Developer Kit


For details about these Jetson devices, see the Jetson Developer Site and the Jetson FAQ.


PREPARING A JETSON DEVELOPER KIT FOR USE

This section explains how to prepare a Jetson developer kit for use by flashing it with the
appropriate software.

Assumptions
-----------

- You have a Jetson Developer Kit.

  * For the Jetson Nano Developer Kit, you can skip this guide and simply download and use the
    supported SD Card image. Alternatively, you can follow these instructions to flash the QSPI-NOR,
    or flash the QSPI-NOR and a microSD Card inserted on the Jetson Nano module.

- Your Jetson developer kit is powered off and is connected as follows. (Note that your Jetson
  developer kit may not come with the devices and cables listed below.)

  *  A USB cable connects the correct USB port of your Jetson developer kit to your Linux host for
     flashing. (For the NVIDIA Jetson AGX Xavier Developer Kit, use the USB-C port next to the power
     button. For the other Jetson developer kits, use the micro USB port.)

  *  Any required USB peripherals such as keyboard and mouse are connected to the Jetson developer
     kit, possibly through a USB hub.

  *  A wired Ethernet connection is available for installing optional software on the Jetson developer
     kit after L4T is installed and running.

  *  Either a display device or a serial console is connected to the Jetson developer kit.

- The qemu-user-static package has been installed on the Linux host:

  sudo apt-get install qemu-user-static

  The installation process needs this package to install certain NVIDIA software components
  onto the Jetson developer kit.

Variables
---------

The directions below assume that:

   ${L4T_RELEASE_PACKAGE} contains the pathname of the L4T release package name.

   For the Jetson Nano and Jetson TX1 modules: Jetson-210_Linux_R32.4.3_aarch64.tbz2
   For Jetson Xavier NX, Jetson AGX Xavier series and Jetson TX2 series modules: Jetson_Linux_R32.4.3_aarch64.tbz2

   ${SAMPLE_FS_PACKAGE} refers to the sample filesystem package file name:
   Tegra_Linux_Sample-Root-Filesystem_R32.4.3_aarch64.tbz2

   ${BOARD} refers to the name of a supported configuration of a specific Jetson module with a
   specific carrier board.
   Examples: jetson-nano-devkit, jetson-tx2-devkit, jetson-xavier-nx-devkit, etc.


TO FLASH JETSON DEVELOPER KIT OPERATING SOFTWARE

1. Download the latest L4T release package and sample file system for your Jetson developer kit
   from: https://developer.nvidia.com/linux-tegra

2. Enter the following commands to untar the files and assemble the rootfs:

  tar xf ${L4T_RELEASE_PACKAGE}
  cd Linux_for_Tegra/rootfs/
  sudo tar xpf ../../${SAMPLE_FS_PACKAGE}
  cd ..
  sudo ./apply_binaries.sh

3. Prepare the Jetson developer kit for flashing.

  a) Ensure that your Jetson developer kit is configured and connected to your Linux host as
  described in Assumptions.

  b) Put your Jetson developer kit into â€Force Recovery Modeâ€ (FRC).

     For the Jetson Nano Developer Kit, follow these instructions:

	1. Ensure that your Jetson Nano Developer Kit is powered off, and that a 16GB or larger
           microSD card is inserted into the SD card slot.
	2. Enable â€Force Recovery modeâ€ by placing a jumper across the FRC pins of the
           Button Header on the carrier board.
	   a. For carrier board revision A02, these are pins 3 and 4 of Button Header (J40) which
              is located near the camera header.
	   b. For carrier board revision B01, these are pins 9 and 10 of Button Header (J50), which
              is located on the edge of the carrier board under the Jetson module.
	3. Place a jumper across J48 to enable use of a DC power adapter.
	4. Connect a DC power adapter to J25. The developer kit powers on automatically and
           enters â€Force Recovery mode.â€
	5. Remove the jumper from the FRC pins of the Button Header.
	6. Continue the software installation.

    For Jetson Xavier NX developer kit follow the instructions below:

	1. Ensure that your Jetson Xavier NX developer kit is powered off and a 16GB or larger size
           microSD card is inserted in the SD card slot.
	2. Enable â€Force Recovery modeâ€ by placing a jumper across pins 9 and 10 (FC REC and GND) of
           Button Header (J14), which is located on the edge of the carrier board under the Jetson module.
	3. Connect the included power adapter to J16. The developer kit powers on automatically and
           enters â€Force Recovery mode.â€
        4. Remove the jumper from pins 9 and 10 of the Button Header.
	5. Continue the software installation.

    For other Jetson developer kits that have hardware buttons:

	1. Ensure that the developer kit is powered off.
	2. Press and hold down the Force Recovery button.
	3. Press, then release the Power button.
	4. Release the Force Recovery button.
        5. Continue the software installation.

  c) You can confirm the developer kit is in Force Recovery mode by following the procedure
     shown at the end of this document.

4. Enter these commands on your Linux host to install (flash) the L4T release onto the
   Jetson developer kit:

   sudo ./flash.sh ${BOARD} mmcblk0p1

   The value of the environment variable ${BOARD} determines the configuration that the flashing
   script applies. A list of common configurations is found below.

5. The Jetson developer kit automatically reboots upon completion of the installation process.
   At this point your Jetson developer kit is operational. Follow the prompts on the display
   to set up a user account and log in.

JETSON MODULES AND CONFIGURATIONS

1. Jetson AGX Xavier series module attached to Jetson AGX Xavier Developer Kit carrier board
                jetson-agx-xavier-devkit	 Flashes eMMC for P2888-0001 (16GB) or P2888-0004 (32GB)
                jetson-agx-xavier-devkit-8gb	 Flashes eMMC for P2888-0006
 
2. Jetson Xavier NX module attached to Jetson Xavier NX Developer Kit carrier board
                jetson-xavier-nx-devkit          Flashes QSPI-NOR and microSD Card for P3668-0000
                jetson-xavier-nx-devkit-emmc     Flashes QSPI-NOR and eMMC for P3668-0001
 
3. Jetson TX2 series module attached to Jetson TX2 Developer Kit carrier board
                jetson-tx2-devkit                Flashes eMMC memory for P3310-1000
                jetson-tx2-devkit-tx2i           Flashes eMMC memory for P3489-0000
                jetson-tx2-devkit-4gb            Flashes eMMC memory for P3489-0888
 
4. Jetson TX1 module attached to Jetson TX1 Developer Kit carrier board
                jetson-tx1-devkit                Flashes eMMC memory for P2180-1000
 
5. Jetson Nano module attached to Jetson Nano Developer Kit carrier board
                jetson-nano-devkit               Flashes QSPI-NOR and microSD Card for P3448-0000
                jetson-nano-devkit-emmc          Flashes QSPI-NOR and eMMC for P3448-0002

There is a configuration file corresponding to each value of ${BOARD}. Its name is the value of
${BOARD} with the filename extension .conf, for example, jetson-nano-devkit.conf.

TO DETERMINE WHETHER THE DEVELOPER KIT IS IN FORCE RECOVERY MODE:

- Connect your Linux host computer to the correct USB port on your Jetson developer kit
  (see Assumptions.)
- Open terminal on your host and enter command â€œlsusbâ€.
  Assumptions: The Jetson module is in Force Recovery mode if you see the message:

	Bus <bbb> Device <ddd>: ID 0955: <nnnn> Nvidia Corp.
	Where:
		<bbb> is any three-digit number
		<ddd> is any three-digit number
		<nnnn> is a four-digit number that represents the type of Jetson module:
		7019 for Jetson AGX Xavier (P2888-0004 with 32GB)
		7019 for Jetson AGX Xavier (P2888-0001 with 16GB)
		7e19 for Jetson AGX Xavier 8GB (P2888-0006)
		7e19 for Jetson Xavier NX (P3668-0001)
		7e19 for Jetson Xavier NX (P3668-0000 devkit version)
		7c18 for Jetson TX2 (P3310-1000)
		7018 for Jetson TX2i (P3489-0000)
		7418 for Jetson TX2 4GB (P3489-0888)
		7721 for Jetson TX1 (P2180-1000)
		7f21 for Jetson Nano (P3448-0002)
		7f21 for Jetson Nano (P3448-0000 devkit version)