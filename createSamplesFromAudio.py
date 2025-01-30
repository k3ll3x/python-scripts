#!/usr/bin/python3

#Author: Siegfried Paul Keller Schippner 2020

# Create Samples for a given audio

# ver 0.0 : Standart croping, high to low

import numpy as np
import sys
from scipy.io import wavfile

def wavFileToArray(filename):
	"""Converts a wav file into a numpy array. Only opens WAV files..."""
	#only reads wav files
	fs, data = wavfile.read(filename)
	return fs, data

def separate_regions(arr, mask):
	"""Subarrys from array with a given mask."""
	m0 = np.concatenate(( [False], mask, [False] ))
	idx = np.flatnonzero(m0[1:] != m0[:-1])
	return [arr[idx[i]:idx[i+1]] for i in range(0,len(idx),2)]

def saveArrayToWav(array, filename, rate):
	wavfile.write(filename, rate, array)

def processData(npArr, cutAt, samplesMinLength, rate, path='', name=''):
	"""Process Numpy array to create subarrays."""
	mask = (npArr != cutAt)
	samples = separate_regions(npArr, mask)
	nsamples = [x for x in samples if len(x) >= samplesMinLength]
	for i in range(len(nsamples)):
		saveArrayToWav(nsamples[i], path + name + str(i) + ".wav", rate)

def main():
	filename = ""
	if len(sys.argv) < 2:
		filename = input("filename")
	else:
		filename = sys.argv[1]
	fs, data = wavFileToArray(filename)
	processData(
		data,
		int(input("cut at (default=0): ") or "0"),
		int(input("sample min len (default=199): ") or "199"),
		fs,
		name = filename.split('.')[0] + "Sample"
	)

main()
