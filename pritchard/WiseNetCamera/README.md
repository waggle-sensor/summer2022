# The Purpose #
The purpose of the project is to create a method for ML systems using the current camera used by Waggle nodes to originally scan lower resolution footage for something interesting then request higher quality footage for said interesting event. Thus hopefully lowering buffer time and other processing constraints.
# The Identity #
In this project I was tasked with figuring out how to access portions of saved video from a Hanwha security camera saved on an internal SD card. I eventually found that I could accomplish this through use of ffplay so long as I referenced at least one timestamp (YYYYMMDDHHMMSS->local, YYYYMMDDHHMMSSZ->universal) which would be received as a starting timestamp for the requested recording. I also learned that I could use two timestamps to request a set period of time. 
# Command #
ffplay rtsp://username:password@10.31.81.10/recording/20220728083000/play.smp
# Note #
This command works on firmware version 2.10.02_20220401_R615 on a Model XNV-8080R Hanhwa security camera.
