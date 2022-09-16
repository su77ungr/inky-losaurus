
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

> NICE TO KNOW: QR code redirects to your pi-hole admin page ヾ(＠⌒ー⌒＠)ノ
  
 
## Requirements

  
- Raspberry Pi (running on Zero W and 4B)
- [Pimoroni InkyPHAT display](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707)
- Pi-hole installation running on default ports
- **Optional:** Cryptocurrency Ticker <a href="https://www.livecoinwatch.com/tools/api#try">get API key</a>


## Setup
- Install the Inky pHAT libary on the command line
```
curl https://get.pimoroni.com/inky | bash
```
- Reboot the Pi
- Clone repo to your home directory
```
git clone https://github.com/su77ungr/inky-losaurus.git \
cd inky-losaurus \
sudo pip install -r requirements.txt

```

- Edit cron jobs
```
crontab -e
```
- Add the below entry to auto-run script every three minutes
```
*/3 * * * * python3 /home/pi/inky-losaurus/main.py
```
Make sure the above path is pointing to the folder you've downloaded the code to

Make sure cron.service is enabled by running  `sudo systemctl enable cron && sudo systemctl start cron`
## Config
- Inside config.json you can change parameters:

```
{
    "directory-path": "/home/pi/inky-losaurus/resources",
    "ticker-enabled": "true",
    "flipped": "true",
    "topic": "config file",
    "version": "Inky-losaurus V.0.1",
    "x-api-data": "{\"currency\":\"EUR\",\"code\":\"XCH\"}",
    "x-api-key": "52d21667-5475-4a08-9ed2-2756e79470db"
}
```
- with following options: 

> "directory-path": "/home/pi/inky-losaurus/resources", `/home/m1000/inky-losaurus/resources` <br><br>
> "ticker-enabled": "true", `false` <br><br>
> "flipped": "true", `false` <br><br>
> "x-api-data": "{\"currency\":\"EUR\",\"code\":\"XCH\"}"  `{\"currency\":\"USD\",\"code\":\"SOL\"}`  <br><br>
> "x-api-key": "52d21667-5475-4a08-9ed2-2756e79470db" `YOUR_KEY` 

## About me

<a href="https://twitter.com/chialisp"> @chialisp </a>

