# Welcome to my README! 
My hope is to make this a useful resource (mostly for me to reference) of the things I've learned so far! My focus is on the client side of the network, so verifying that the Waggle Nodes can connect and transmit data over the network, so my information is mostly relevant to that. A loootta Telit manual stuff so far :)
## Telit FN980m Information
This is the module we are using to eventually connect our Waggle Nodes to the 5G network. They kind of act like cell phones -they can send and recieve calls and SMS- and we will mainly use them like a phone putting up a hotspot. It's a pretty versatile little machine!
### Helpful AT Commands
This section will not tell you the full functionality of the commands, but instead serves as a culled down list of relevant commands. Use this in conjunction with the Telit AT Command manual (not sure if it's kosher to link that here)
- **AT#BND** selects band for 3G, 4G, and 5G [(command help)](https://techship.com/faq/how-to-use-atbnd-to-select-active-bands-on-telit-modules/)
- **AT+WS46** selects cellular network 
- **AT#5GCTL** enable NSA FR1/FR2 and SA FR1/FR2 
- **AT+CIND?** returns some status updates, like battery charge, signal quality, and RSSI 
- **AT+CESQ** returns RSRQ, RSRP, and SNR for 5G signals, will give parameters for 3G and 4G if those are enabled 
  - **AT#CAINFO** returns like, every possible parameter possible and is a little hard to read, but could be useful
- **AT#TEMPSENS** gives current temperature and **AT#TMLVL?** gives temperature mitigation level 
- **AT#CSURV** performs network survey, but possibly only finds 3G and 4G networks 
- **AT#TESTMODE** and **AT#MIMOSTS** are also possibly useful 
 ### Some EVB interests of mine
  - Use Arduino to remotely control the EVB
    - Looks like standard 20-pin connection
  - GNSS information can give us date, time, location, and ground speed information
  - Found some GPIO pin commands if we want to connect a Raspberry Pi, I2C, or possibly have analog data flow
  - Audio input, looks like mainly so you can "call" other devices, but who knows!
## Other helpful links
- [Linux learning help](https://linuxjourney.com/)
- Quick [CBRS Resource](https://www.fiercewireless.com/private-wireless/what-cbrs)
- [Docker basics explanation](https://yannmjl.medium.com/what-is-docker-in-simple-english-a24e8136b90b#:~:text=Docker%20is%20a%20tool%20designed,all%20out%20as%20one%20package.)
- Raspberry Pi [GPIO](https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html)
- Python window automater [pywinauto](https://pywinauto.readthedocs.io/en/latest/getting_started.html)
