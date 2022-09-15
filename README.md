
  <div align="center">
  
  #  Inky-losaurus 
   || Custom Dashboards for e-ink displays ||
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
<p align="center">
  <a href="https://www.livecoinwatch.com/tools/api#try"><style="height:100px">get API key</a>
  <br>

## Table of contents
* [Requirements](#requirements)
* [Setup](#setup)
* [Config](#config)


## Hardware required

- Raspberry Pi (running on Zero W and 4B)
- [Pimoroni InkyPHAT display](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707)
- **Optional:** 3D printed case with [micro USB sockets](https://www.aliexpress.com/item/4000484202812.html)
- **Optional:** [Waveshare 2.13" e-paper display V2](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) (**Note:** the case designs will need modification to fit this display. Set the `WAVESHARE` environment variable to `1` to enable support)

## Setup & Installation

Running this project is as simple as deploying it to a balenaCloud application. You can do it in just one click by using the button below:

You can also deploy in the traditional manner using the balena CLI and `balena push` command. For more information [check out the docs](https://www.balena.io/docs/learn/deploy/deployment/).

## Customization

![inky-losaurus](https://user-images.githubusercontent.com/69374354/190515235-84974961-f46f-4417-b627-bd83541c6267.png)


## Requirements
- Raspberry Pi
- Inky pHAT e-ink display

## Setup
- SSH onto Pi
- Install the Inky pHAT libary on the command line
```
curl https://get.pimoroni.com/inky | bash
```
- Reboot the Pi
- Download the bitcoin_ticker code to any your home directory
```
git clone https://github.com/naviavia/bitcoin_ticker.git
```
- Edit cron jobs
```
crontab -e
```
- Add the below entry (5 represents the frequency of the task e.g. updating to 1 will run every minute)
```
*/5 * * * * python3 /home/pi/bitcoin_ticker/bitcoin.py
```
Make sure the above path is pointing to the folder you've downloaded the code to

## Config
- To flip the display add the below argument;

```
--flip true
```

- To use an alternative Coin/Currency enter the pair & currency below e.g. ADA - GBP. This is based on available pairs on Kraken.

```
--pair adagbp
```
