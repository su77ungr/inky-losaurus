
  <div align="center">
  
  #  Inky-losaurus 
   Custom Dashboards for e-ink displays
  </div>
 
 <div align="center">
 
![inky-empty](https://user-images.githubusercontent.com/69374354/190515213-0754d728-cc06-440f-adb7-18ff0a2a1e2f.png)
<br><br>
<br>
![inky-losaurus](https://user-images.githubusercontent.com/69374354/190515235-84974961-f46f-4417-b627-bd83541c6267.png)
<br><br><br>
![inky-losaurus-preview](https://user-images.githubusercontent.com/69374354/190515533-cacd056c-9dad-4c64-90dc-4896bcd49cf8.png)
<br>
  </h3>

   </div>
   
<br> 

    </div>
  
 
## Requirements

  
- Raspberry Pi (running on Zero W and 4B)
- [Pimoroni InkyPHAT display](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707)
- Pi-hole installation running on default ports
- **Optional:** 3D printed case with [micro USB sockets](https://www.aliexpress.com/item/4000484202812.html)
- **Optional:** Cryptocurrency Ticker <a href="https://www.livecoinwatch.com/tools/api#try">get API key</a>


## Setup
- Install the Inky pHAT libary on the command line
```
curl https://get.pimoroni.com/inky | bash
```
- Reboot the Pi
- Clone repo to your home directory
```
git clone https://github.com/su77ungr/inky-losaurus.git
```
- Edit cron jobs to auto-run script every three minutes
```
crontab -e
```
- Add the below entry (5 represents the frequency of the task e.g. updating to 1 will run every minute)
```
*/3 * * * * python3 /home/pi/inky-losaurus/main.py
```
Make sure the above path is pointing to the folder you've downloaded the code to

Make sure cron.service is enabled by running  `sudo systemctl enable cron && sudo systemctl start cron`
## Config
- To flip the display add the below argument;

```
--flip true
```
    
```
--ticker true
```

- Select flag to select alternative Coin/Currency

```
--ticker-currency BTC-USD # ETH-EUR etc.
```


```
--pair adagbp
```
