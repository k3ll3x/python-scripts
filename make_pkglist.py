#!/usr/bin/python3
# Get installed pkg list for using script 'installPackages.py'
import os, sys
t = os.popen("apt list").read().split('\n')
tt = []
for i in t:
	tt.append(i.split('/')[0])
if len(sys.argv) == 2:
	f = open(sys.argv[1], "w");
else:
	f = open(input("filename to save pkglist: "), "w");
f.write('\n'.join(tt))
f.close()
