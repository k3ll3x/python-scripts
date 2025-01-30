#!/usr/bin/python3

import os,sys

args = []

if len(sys.args) == 1:
	args.append(input("port: "))
	args.append(input("tcp or udp (tcp): ") or "tcp")
else:
	args.append(sys.args[1])
	try:
		args.append(sys.args[2])
	except:
		print("Missing protocol (tcp/udp)")
		exit()

out = os.popen("fuser -k {port}/{protocol}".format(port=args[0], protocol=args[1]))
print(out.read())
