# Previous footage requests
- [ ] Timestamps are formatted differently from documentation instead of YYYYMMDDTHHMMSS they are formatted as YYYYMMDDHHSS
- [ ] Unlike documentation requests include username & password
- [ ] Unlike documentation requests must have a starting timestamp
- [ ] SD cards are constantly overwriting themselves because of limited storage, this means there is a limit to how long footage is stored
- [ ] In the case that a timestamp too early is requested the earliest footage is sent
- [ ] Most media players have additional unkown tags that must be set in order to play received video, ffplay doesn't
- [ ] Video can be requested using timestamps that refer to a time zone or local time, YYYYMMDDHHMMSS->local YYYYMMDDHHMMSSZ->universal
- [ ] Video can be requested with just a starting time, in which case it appears to send footage up to 5 mins+ after that start time, video can also be requested by passing a start time and an end time
<br>
just start time->ffplay rtsp://username:password@10.31.81.10/recording/20220728083000/play.smp
<br>
two timestamps->ffplay rtsp://admin:why1not+@10.31.81.10/recording/20220728083000Z-20220728083500Z/play.smp
<br>
In the case of trying to get footage from previous 5 mins,ffplay rtsp://username:password@10.31.81.10/recording/time_5_mins_agoYYYYMMDDMMSS/play.smp
