#!/usr/bin/python3

import os

ch = input("grep: ")

cmd = "adb shell pm list packages | grep " + ch
o = os.popen(cmd)
t = o.read()

t = t.split('\n')

if t[0] == '':
		exit()

nt = []

for i in range(len(t)):
	if t[i] != '':
		tmp = t[i].split(':')[-1]
		print(str(i+1) + ": " + tmp)
		nt.append(tmp)

ch = input("Select a package name (separated by space) 0 to cancel: ")
ch = ch.split(' ')

if ch[0] == '0':
	exit()

cmd = "adb shell pm uninstall -k --user 0 "

for i in ch:
	if i != '':
		pkgnm = nt[int(i)-1]
		print("Removing " + pkgnm + "...")
		o = os.popen(cmd + pkgnm)
		print(o.read())
