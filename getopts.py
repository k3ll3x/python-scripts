#!/usr/bin/python3

import getopt, sys

a = 'forthy-two'
b = 42

def usage():
	print("{0} -a, --aa str -b, --bb int".format(sys.argv[0]))

# If default setting is possible
default = False

try:
	opts, args = getopt.getopt(sys.argv[1:], "ha:b:", ["help","aa=","bb="])
except getopt.GetoptError:
	usage()
	print("using default settings...")
	default = True

if not default:
	for op, ar in opts:
		if op in ("-h", "--help"):
			usage()
			sys.exit()
		elif op in ("-a", "--aa"):
			a = ar
		elif op in ("-b", "--bb"):
			b = int(ar)
		else:
			assert False, "unhandled option"

print(a, b)
