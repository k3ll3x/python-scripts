#!/usr/bin/python3

#run this as sudo

import time, mouse, random, os

min = 0
max = 255
deltaTime = 9*60

#os.system("sleep " + str(deltaTime2) + "m; poweroff")
if input("sleep? (y/n):") == "y":
	deltaTime2 = input("minutes: ")
	os.spawnl(os.P_NOWAIT, "/usr/bin/sleepoff", "sleepoff", str(deltaTime2))

print("sleep scope passed")

while True:
	mouse.move(
		random.randint(min,max),
		random.randint(min,max)
	)
	time.sleep(deltaTime)
