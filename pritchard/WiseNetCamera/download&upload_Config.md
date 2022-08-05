# Purpose
By downoading the config of a camera that has had its settings manually adjusted to what ever is desired, that config can be uploaded to any number of other cameras, both in order to originally set other camera upon deployment as well as recover thier settings remotely in the event of a factory reset.
# Downloding Config
the config can be downloaded using this command
```
curl -v --digest -u "admin":"password" "http://10.31.81.10/stw-cgi/system.cgi?msubmenu=configbackup&action=control" > config.bin
```
the downloaded config can be converted into a usable format using this command
```
openssl base64 -in config.bin -out configrestore.bin
```
# Uploading Config
the config can be uploaded using this command
```
curl -v  --digest -u "admin":"password"  -H "Expect:" --data-urlencode @configrestore.bin "http://10.31.81.10/stw-cgi/system.cgi?msubmenu=configrestore&action=control&ExcludeSettings=Network"
```
