#!/usr/bin/python3

import random, sys

if len(sys.argv) < 3:
	seasons = int(input("seasons: ") or 20)
	episodes = int(input("episodes: ") or 20)
else:
	seasons = int(sys.argv[1])
	episodes = int(sys.argv[2])

print("S{0}-E{1}".format(random.randint(1,seasons), random.randint(1, episodes)))
