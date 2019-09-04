#!/usr/bin/env bash

sudo chmod 755 ./pAction/pStart.sh
sudo chmod 755 ./pAction/pStop.sh

sudo rm -rf /opt/retropie/configs/all/piSleepMode

echo "mkdir /opt/retropie/configs/all/piSleepMode"
mkdir /opt/retropie/configs/all/piSleepMode

echo "cp -Rf ./ /opt/retropie/configs/all/piSleepMode"
cp -Rf ./ /opt/retropie/configs/all/piSleepMode

echo "runcommand-onstart.sh / runcommand-onend.sh line add"
sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onstart.sh
sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onend.sh

echo "python /opt/retropie/configs/all/piSleepMode/piSleep.py 1.0 & > /dev/null 2>&1" >> /opt/retropie/configs/all/runcommand-onstart.sh
echo "ps -ef | grep piSleep.py | grep -v grep | awk '{print \$2}' | xargs kill -9" >> /opt/retropie/configs/all/runcommand-onend.sh


echo "install complete!"