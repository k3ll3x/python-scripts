#!/usr/bin/python3
import sys

filename = ""

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = input("filename: ")

f = open(filename)
txt = sorted(f.read().split('\n'))
f.close()
txt = '\n'.join(txt)
f = open(filename, "w")
f.write(txt)
f.close()
