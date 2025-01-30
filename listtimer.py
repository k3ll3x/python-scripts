#!/usr/bin/python3

# args are the sequence of seconds timers

# Args: timer_name X timer2_name X ...
#where X is a number

import time
import threading
import subprocess
import sys

soundpath = "/home/nuvhandra/Music/tibet/bowl.wav"

def playsound():
	sproc = subprocess.Popen(['cvlc','--play-and-exit', soundpath], close_fds=True)
	time.sleep(20)
	sproc.kill()

def timer(tlist):
	print("Sequencer Timer")

	d = {int(tlist[i+1]): tlist[i] for i in range(0, len(tlist), 2)}

	for i in d:
		sleep = i
		print(f"{d[i]} : {sleep} seconds")
		subprocess.Popen(['notify-send',f"{d[i]} : {sleep} seconds",'--expire-time=10000'])
		time.sleep(sleep)
		background_thread = threading.Thread(target=playsound)
		background_thread.start()

if __name__ == "__main__":
	l = sys.argv[1:]
	timer(l)
