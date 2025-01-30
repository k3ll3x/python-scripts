#!/usr/bin/python3

# Play search string

import subprocess, os, sys, random,time

if len(sys.argv) < 2:
	sys.exit()

srch = ""
for i in sys.argv[1:]:
	srch += f"*{i}"
srch += "*"

print(srch)

muspath = os.popen("echo $HOME").read().split('\n')[0] + "/Music"

print(muspath)

cmd = f'find {muspath} -iname {srch}'

print(cmd)
lst = os.popen(cmd).read().split('\n')

random.shuffle(lst)
print(lst)

for i in lst:
	if i != '':
		a = time.perf_counter()
		subprocess.run(["mplayer", i],check=True)
		b = time.perf_counter()
		if (b-a) < 100:
			subprocess.runb(f'mplayer {i}/**')

time.sleep(5)
