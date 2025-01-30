#!/usr/bin/python3
#Generate random wav file

import numpy as np
from scipy.fft import fft, ifft
from scipy.io.wavfile import write

# 44100 random samples between -1 and 1
data = np.random.uniform(-1,1,44100)
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('sound.wav', 44100, scaled)
