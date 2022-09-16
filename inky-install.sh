#!/bin/bash

#setup of inky-losaurus
curl https://get.pimoroni.com/inky | bash &&
git clone https://github.com/su77ungr/inky-losaurus.git
cd inky-losaurus 
sudo pip install -r requirements.txt 
sudo apt-get install jq -y 

# init first setup to generate config.json
python3 main.py &&
cat config.json | jq .directory_path > path.yml
v=$(cat path.yml)
v2=${v::-12}
myString="${v2:1}"
echo $myString

# put script into cron / script runs every minute automatically
crontab -l > mycron
echo "* * * * * python3 $myString/main.py" >> mycron
crontab mycron

# remove installation files
rm mycron
rm path.yml

echo "Setup complete -> edit config.json to change parameters to your liking!"
echo cat config.json | jq .version 