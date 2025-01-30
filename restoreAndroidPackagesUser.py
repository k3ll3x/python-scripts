#!/usr/bin/python3

import os

f = open("apkglst")
t = f.read()
t = t.split('\n')

#cmd = "adb shell cmd package install-existing "
cmd = "adb shell cmd install-existing "

for i in t:
	if i != '':
		pkgnm = i.split(':')[-1]
		print("Restoring " + pkgnm + "...")
		o = os.popen(cmd + pkgnm)
		t = o.read()
		print(t)

