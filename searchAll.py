#!/usr/bin/python3
import os

file = open("tasklist","r")
str = file.readlines()
file.close()

stream = []
for i in str:
	cmd = i.split('\n')[0]
	print("Finding\t"+cmd+"...")
	cmd = os.popen('find "/mnt/c" -name ' + cmd).read()
	stream.append(cmd)

file = open("pathListSearch","w")

for i in stream:
	file.write(i + '\n')

file.close()
