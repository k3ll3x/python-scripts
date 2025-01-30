#!/usr/bin/python3
import sys

def usage():
    print(f"{sys.argv[0]} filename keystr")

if len(sys.argv) < 3:
    usage()
    sys.exit()

filename = sys.argv[1]
keystr = sys.argv[2]

f = open(filename, "rb")
b = f.read()
f.close()

klen = len(keystr)
idx = 0

nb = []

for i in b:
    nb.append(i ^ ord(keystr[idx]))
    idx = (idx + 1) % klen

f = open(f"{filename}.xtal","wb")
f.write(bytes(nb))
f.close()