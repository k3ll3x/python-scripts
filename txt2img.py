#!/usr/bin/python3

from PIL import Image
import numpy as np
import math
import sys

def usage():
	print("{0} encode/decode filename".format(sys.argv[0]))

def encode(filename):
    f = open(filename)
    txt = f.read()
    f.close()

    f = np.vectorize(ord)
    arr = np.array(list(txt))
    narr = f(arr)

    x = math.ceil(math.sqrt(len(narr)))

    narr = np.resize(narr,(x,x)).astype(np.uint8)
    img = Image.fromarray(narr)
    img.save("{0}e.png".format(filename))

def decode(filename):
    img = Image.open(filename)
    narr = np.array(img)
    f = np.vectorize(chr)
    txt = ""
    for i in f(narr).flatten():
        txt += i
    f = open("{0}d.txt".format(filename),"w")
    f.write(txt)
    f.close()
    
if len(sys.argv) < 2:
	usage()
	sys.exit(-1)

ch = sys.argv[1]
filename = sys.argv[2]

if ch == "encode":
    encode(filename)
elif ch == "decode":
    decode(filename)
else:
    usage()