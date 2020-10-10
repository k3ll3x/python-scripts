#!/usr/bin/python3

import subprocess, re
from datetime import datetime

f = open("habits")
txt = f.read().split('\n')
f.close()

habits = {}

for i in txt:
	if i != '':
		h = re.findall("[\w ]+", i)
		habits[h[0]+h[1]] = h

cmd = 'notify-send "'

while True:
	now = datetime.now()
	for i in habits:
		if now.hour >= int(habits[i][0]):
			if now.minute >= int(habits[i][1]):
				subprocess.call(cmd + habits[i][-1] + '"', shell=True)
				del habits[i]
				break
