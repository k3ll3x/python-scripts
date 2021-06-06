#!/usr/bin/python3
import numpy as np
from scipy.io.wavfile import read
import sys
import cv2

f = ""
if len(sys.argv) == 2:
	f = sys.argv[1]
else:
	f = input("wav file: ")

#convert audio to numpy array
a = read(f)
a_np = np.array(a[1], dtype=int)

#divided by 3 because of RGB
#dim = (a_np.shape[0] * a_np.shape[1]) / 3

frames = 10
height = 64
width = 64
size = (width, height)

vid_arr = np.resize(a_np, (frames, width, height, 3))
vid_arr = np.array(list(map(lambda x: (x*500) % 255, vid_arr)))

print(vid_arr)

out = cv2.VideoWriter('out.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 15, size)

for i in range(len(vid_arr)):
	out.write(vid_arr[i])
out.release()
