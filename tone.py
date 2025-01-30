#!/usr/bin/python3
import time
import argparse
import numpy as np
from scipy.io.wavfile import write
import os
import sounddevice as sd

def generate_wave(duration, frequency, sample_rate, save):
	print(frequency)
	t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
#	data = np.sin(2 * np.pi * frequency * t)
	data = np.sin(2 * np.pi * frequency * t) * np.sin(2*np.pi*frequency/2*t)
	if save != 0:
		write("{0}.wav".format(frequency), sample_rate, data)
	return data

def play_sound(data, sample_rate):
	sd.play(data, sample_rate)
	sd.wait()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Sine Tone generator')
	parser.add_argument('d', type=int, help='duration')
	parser.add_argument('f', type=int, help='frequency')
	parser.add_argument('--save', default=0,type=int, help='save samples')
	args = parser.parse_args()
	print(args)

	generate_wave(args.d, args.f, 44100, args.save)
