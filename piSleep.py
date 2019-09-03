#!/usr/bin/env python
import struct
import os
import time
import threading
import sys

stopDelay = float(sys.argv[1])
actionPath = "/home/pi/dev/piSleepMode/pAction/"

def js_checker():
	global sleepFlag
	global start_time
	js_path = "/dev/input/event0"
	if os.path.exists("/dev/input/event1") == True:
		js_path = "/dev/input/event1"
	else:
		js_path = "/dev/input/event0"

	EVENT_SIZE = struct.calcsize("L");
	file = open(js_path, "rb")
	event = file.read(EVENT_SIZE)
	while event:
		if sleepFlag == True:
			os.system(actionPath + "pStart.sh &")
			sleepFlag = False
			print("continue game")
		#print(struct.unpack("L", event))
		start_time = time.time()
		event = file.read(EVENT_SIZE)

print("pi_sleepMode Start")
start_time = time.time()
sleepFlag = False
th = threading.Thread(target=js_checker, name="[js_checker]", args=())
th.setDaemon(True)
th.start()
try:
	while True:
		duringTime = (time.time() - start_time )/60
		print("--- runtime : %0.2f Minutes "%duringTime  )
		if sleepFlag == False:
			if duringTime > stopDelay:
				os.system(actionPath  + "pStop.sh &")
				print("game pause")
				sleepFlag = True
		time.sleep(1)

except KeyboardInterrupt:
	print("pi_sleepMode End")
