#!/usr/bin/env bash
sudo rm -rf /opt/retropie/configs/all/piSleepMode

sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onstart.sh
sudo sed -i '/piSleep.py/d' /opt/retropie/configs/all/runcommand-onend.sh