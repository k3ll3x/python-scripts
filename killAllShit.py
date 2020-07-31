#!/usr/bin/python3
import os

file = open("tasklist","r")
str = file.readlines()
file.close()

for i in str:
	cmd = i.split('\n')[0]
	print("Killing\t"+cmd+"...")
	cmd = "killw " + cmd
	os.system(cmd)
