#!/usr/bin/python3

import sys
#import secrets
import random

if len(sys.argv) < 2:
	sys.exit(-1)


#print(secrets.token_hex(int(sys.argv[1])))


hex_chars = '0123456789abcdef'
hex_key = ''.join(random.choice(hex_chars) for _ in range(64))
print(hex_key)
