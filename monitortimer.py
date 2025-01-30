#!/usr/bin/python3
import psutil
import time
from datetime import date
import subprocess
import os

#remove suspicious processes list
susl = [
	"sd-pam"
]

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = ':0.0'

soundpath = "/home/nuvhandra/Music/tibet/bowl.wav"

def playsound():
	sproc = subprocess.Popen(['cvlc','--play-and-exit', soundpath], close_fds=True)
	time.sleep(20)
	sproc.kill()

# Set the time limit
today = date.today()
if today.weekday() >= 0 and today.weekday() < 5:
	time_limit = 6 * 60 * 60
else:
	time_limit = 4 * 60 * 60

print(f"Monitor Timer started, time limit: {(time_limit/60)/60}")

# Main loop to check system usage
while True:
	#remove sus
	for i in susl:
		subprocess.Popen(["killall",i])

	# Get the total system uptime in seconds
	uptime = psutil.boot_time()
	current_time = time.time()
	system_usage = current_time - uptime

	# Check if the system usage exceeds the time limit
	if system_usage > time_limit:
		print("Sending notification to user")
		# Send a notification
		subprocess.Popen(['notify-send', 'Usage Limit Exceeded', 'You have reached the 8-hour usage limit','--expire-time=10000'])
		playsound()
		time.sleep(60)
		print("Poweroff")
		subprocess.Popen(['poweroff'])
		#break

	# Check system usage every 10 minutes
	time.sleep(600)
