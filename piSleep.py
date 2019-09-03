#!/usr/bin/env python
import struct
import os
import time
import threading

actionPath = "/home/pi/dev/piSleep/pAction/"

def js_checker():
	global sleepFlag
	global start_time
	js_path = "/dev/input/js0"
	EVENT_SIZE = struct.calcsize("L");
	file = open(js_path, "rb")
	event = file.read(EVENT_SIZE)
	while event:
		if sleepFlag == True:
			os.system(actionPath + "pStart.sh &")
			sleepFlag = False
			print("continue game")
		#print(struct.unpack("LhBB", event))
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
			if duringTime > 0.10:
				os.system(actionPath  + "pStop.sh &")
				print("game pause")
				sleepFlag = True
		time.sleep(1)

except KeyboardInterrupt:
	print("pi_sleepMode End")
