#!/usr/bin/python3

import os

t = os.popen("cat /etc/passwd").read()
t = t.split("\n")

tt = ""
for i in t:
	if i != '':
		tt += "\t" + i.split(':')[0]
print("USER GROUPS:\n")
print(tt)
