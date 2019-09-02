#!/usr/bin/env python
import struct
import os
import time
import threading


def js_checker():
	global sleepFlag
	global start_time
	js_path = "/dev/input/js0"
	EVENT_SIZE = struct.calcsize("LhBB");
	file = open(js_path, "rb")
	event = file.read(EVENT_SIZE)
	while event:
		if sleepFlag == True:
			os.system("ps -ef | grep emulators | grep -v grep | awk '{print $2}' | xargs kill -SIGCONT &")
			sleepFlag = False
			start_time = time.time()
			print("continue game")
		#print(struct.unpack("LhBB", event))
		event = file.read(EVENT_SIZE)

start_time = time.time()
sleepFlag = False
th = threading.Thread(target=js_checker, name="[js_checker]", args=())
th.start()

while True:
	duringTime = (time.time() - start_time )/60
	print("--- runtime : %0.2f Minutes "%duringTime  )
	if sleepFlag == False:
		if duringTime > 0.10:
			os.system("ps -ef | grep emulators | grep -v grep | awk '{print $2}' | xargs kill -SIGSTOP &")
			print("game pause")
			sleepFlag = True
	time.sleep(1)
