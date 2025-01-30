#!/usr/bin/python3

import os, sys

if len(sys.argv) < 2:
	pch = input("process name: ")
else:
	pch = sys.argv[1]

tout = os.popen("ps aux | grep " + pch).read()
t = tout.split('\n')
#count of process excluding empty line and grep process
num = len(t)-5
if num < 1:
	#re-run process
	print("re-run process " + pch)
	print(os.popen("export DISPLAY=:0; nohup " + pch).read())
else:
	print("Process " + pch + " still running...")
