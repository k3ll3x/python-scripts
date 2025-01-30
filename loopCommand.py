#!/usr/bin/python3
import os, sys

ch = ""
if len(sys.argv) == 3:
	ch = sys.argv[1]
	n = sys.argv[2]
	if n == "True":
		n = True
	else:
		n = int(n)
if len(sys.argv) == 2:
	ch = sys.argv[1]
	n = True
else:
	ch = input("input: ")
	n = int(input("times: "))

if n == True:
	while True:
		print(os.popen(ch).read())
else:
	for i in range(n):
		print(os.popen(ch).read())
