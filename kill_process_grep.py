#!/usr/bin/python3

import os, re, sys

grep = ""

if len(sys.argv) == 1:
	grep = input("process name: ")
else:
	grep = sys.argv[1]

cmd = "ps aux | grep " + grep

out = os.popen(cmd).read().split('\n')

for i in out:
	if i != '':
		pid = re.findall("\d+", i)[0]
		if not re.search("grep", i):
			cmd = "kill -9 " + pid
			out = os.popen(cmd).read()

