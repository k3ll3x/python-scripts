#!/usr/bin/python3

import os

ch = input("grep: ")

cmd = "adb shell pm list packages | grep " + ch
o = os.popen(cmd)
t = o.read()
t = t.split('\n')

cmd = "adb shell pm uninstall -k --user 0 "

for i in t:
	if i != '':
		pkgnm = i.split(':')[-1]
		print("Removing " + pkgnm + "...")
		o = os.popen(cmd + pkgnm)
		t = o.read()
		print(t)

