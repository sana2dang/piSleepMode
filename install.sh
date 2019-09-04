#!/usr/bin/env bash

sudo rm -rf /opt/retropie/configs/all/piSleepMode
mkdir /opt/retropie/configs/all/piSleepMode
cp -Rf ./ /opt/retropie/configs/all/piSleepMode

sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onstart.sh
sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onend.sh

echo "sudo python /opt/retropie/configs/all/piSleepMode/piSleep.py 1 & > /dev/null 2>&1" >> /opt/retropie/configs/all/runcommand-onstart.sh
echo "ps -ef | grep piSleep.py | grep -v grep | awk '{print $2}' | xargs sudo kill -9" >> /opt/retropie/configs/all/runcommand-onend.sh
