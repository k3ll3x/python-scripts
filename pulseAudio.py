#!/usr/bin/python3

import os, sys

if len(sys.argv) == 1:
	ch = input("start or stop pulseaudio: ")
else:
	ch = sys.argv[1]

cmd = []

if ch == "start":
	cmd.append("systemctl --user start pulseaudio.socket")
	cmd.append("systemctl --user start pulseaudio.service")
elif ch == "stop":
	cmd.append("systemctl --user stop pulseaudio.socket")
	cmd.append("systemctl --user stop pulseaudio.service")
else:
	print(ch + " is not an option!")

out = ""

for i in cmd:
	out += os.popen(i).read()

print(out)
