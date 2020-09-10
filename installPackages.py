#!/usr/bin/python3

#run as root

import os, time, re

f = open("pkglst","r")
t = f.read()
f.close()

cmd = "apt -y install "

log = ""

for i in t.split('\n'):
	if i != '':
		print("Collecting " + i)
		out = os.popen(cmd + i).read()
		if re.match("error", out, re.IGNORECASE):
			print("Error found while trying to install " + i)
			print("Check log to see the error\n\n")
		else:
			print("Done\n\n")
		log += "Collecting " + i + "\n\n" + out + "\n\n"

ch = input("\n\nPrint log? (Y/n):") or 'y'
if ch == 'y':
	print(log)

ch = input("\n\nSave log? (y/N):") or 'n'
if ch == 'y':
	t = time.localtime()
	f = open("log_{y}-{m}-{d}".format(y=t.tm_yeah,m=t.tm_mon,d=t.tm_mday) ,"w")
	f.write(log)
	f.close()
