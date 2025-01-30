#!/usr/bin/python3
import os, sys

#os.popen("notify-send working").read()
path = "/home/nuvhandra/Documents/dev/python/scripts/"

if len(sys.argv) == 2:
	f = open(path + "rshift_v","r+")
	if sys.argv[1] == "kill":
		print("kill")
		os.popen("redshift -x").read()
		f.seek(0)
		f.truncate()
		f.write(str(6000))
		sys.exit()
	rshift = f.read().split('\n')[0]
	print(rshift)
	rshift_v = 0
	delta = 500
	limits = [1000, 25000]
	if sys.argv[1] != "up":
		delta = -delta
	try:
		rshift_v = int(rshift)
	except:
		rshift_v = 6000
	rshift_v += delta
	if rshift_v >= limits[0] and rshift_v <= limits[1]:
		os.popen("redshift -x").read()
		v = "redshift -O " + str(rshift_v)
		#os.popen("notify-send -i /home/nuvhandra/Pictures/xek.png 'redshift @ " + str(rshift_v) + "'").read()
		#print(v)
		os.popen(v).read()
		f.seek(0)
		f.truncate()
		f.write(str(rshift_v))
		f.close()
	else:
		f.close()
