#!/usr/bin/python3

import sys, random, string

N = 0
punc = ''

if len(sys.argv) == 3:
	N = int(sys.argv[1])
	punc = string.punctuation
elif len(sys.argv) == 2:
	N = int(sys.argv[1])
else:
	N = int(input("String length: "))

print(''.join(random.choice(string.ascii_letters + string.digits + punc) for _ in range(N)))
