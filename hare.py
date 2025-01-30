#!/usr/bin/python3

import sys, os

file1 = ""
file2 = ""

if len(sys.argv) < 3:
	file1 = input("file 1: ")
	file2 = input("file 2: ")
else:
	file1 = sys.argv[1]
	file2 = sys.argv[2]

#os.popen("convert {0} -resize 10% {1}".format(file1, "_" + file1)).read()
#file1 = "_" + file1

f = open(file1, "rb")
t = f.read()
f.close()

f = open(file2, "rb")
tt = f.read()
f.close()

nfile = file1.split('.')
nfile = "krishna." + nfile[-1] if len(nfile) >= 1 else "krishna"
f = open(str(len(t)) + "_" + nfile, "wb")
f.write(t + tt)
f.close()
