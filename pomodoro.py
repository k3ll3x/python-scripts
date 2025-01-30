#!/usr/bin/python3
import time
import argparse
import subprocess

soundpath = "/home/nuvhandra/Music/tibet/bowl.wav"

def playsound():
	sproc = subprocess.Popen(['cvlc','--play-and-exit', soundpath], close_fds=True)
	time.sleep(20)
	sproc.kill()

def pomodoro_timer(work_time, short_break, long_break):
	work_time *= 60
	short_break *= 60
	long_break *= 60	
	
	pomodoro_count = 0

	print("Pomodoro Timer")

	while True:
		print(f"Work for {work_time/60} minutes")
		subprocess.Popen(['notify-send',f"Work for {work_time/60} minutes",'--expire-time=10000'])
		playsound()

		for _ in range(work_time-20):
			time.sleep(1)

		pomodoro_count += 1

		if pomodoro_count % 4 == 0:
			print(f"Take a {long_break/60}-minute break")
			subprocess.Popen(['notify-send',f"Take a {long_break/60}-minute break",'--expire-time=10000'])
			playsound()
			for _ in range(long_break-20):
				time.sleep(1)
		else:
			print(f"Take a {short_break/60}-minute break")
			subprocess.Popen(['notify-send',f"Take a {short_break/60}-minute break",'--expire-time=10000'])
			playsound()
			for _ in range(short_break-20):
				time.sleep(1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Pomodoro Timer')
	parser.add_argument('--work_time', type=int, default=25, help='Work time in minutes')
	parser.add_argument('--short_break', type=int, default=5, help='Short break time in minutes')
	parser.add_argument('--long_break', type=int, default=15, help='Long break time in minutes')
	args = parser.parse_args()

	pomodoro_timer(args.work_time, args.short_break, args.long_break)
