#!/usr/bin/python3

import sys, subprocess

if len(sys.argv) == 1:
	ch = range(256)
elif len(sys.argv) == 2:
	ch = range(int(sys.argv[1]))
else:
	ch = range(int(sys.argv[1]),int(sys.argv[2]))

table = ""
for i in ch:
	table += str(i)+"\t:\t"+chr(i)+'\n'

try:
	if sys.argv[3]:
		subprocess.call('nohup xmessage "' + table + '" &',shell=True)
except:
	print(table)
