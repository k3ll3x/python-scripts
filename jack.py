#!/usr/bin/python3

import os, sys

if len(sys.argv) == 1:
	ch = input("start or stop jack: ")
else:
	ch = sys.argv[1]

cmd = []

if ch == "start":
	cmd.append("pulseaudio --kill")
	cmd.append("systemctl --user stop pulseaudio.socket")
	cmd.append("systemctl --user stop pulseaudio.service")
	cmd.append("jack_control  start")
elif ch == "stop":
	cmd.append("jack_control exit")
	cmd.append("pulseaudio --start")
else:
	print(ch + " is not an option!")

out = ""

for i in cmd:
	out += os.popen(i).read()

print(out)

if ch == "start":
	if (input("start qjackctl? (y/N)") or 'n') == 'y':
		out = os.popen("qjackctl &")
		print(out)

