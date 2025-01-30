#!/usr/bin/python3

import os

f = open("piplist","r")
t = f.read()
f.close()

t = t.split('\n')

for i in t:
	if i != '':
		print(os.popen("pip3 install " + i).read())

