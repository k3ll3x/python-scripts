#!/usr/bin/python3
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import os
import sounddevice as sd

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def generate_sine_wave(duration, frequency, sample_rate, save):
	print(frequency)
	t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
	data = t
	for i in range(1, 10):
		fib = fibonacci(i)
		#data += np.sin(fib * 2 * np.pi * frequency/fib * t)/fib
		data += np.sin(1/fib * 2 * np.pi * frequency/fib * t)/fib
		#data += np.sin(fib * frequency/fib * t)/fib
	if save != 0:
		saveplot(data, "{0}".format(frequency))
		write("{0}.wav".format(frequency), 44100, data)
	return data

def saveplot(data, name):
	plt.plot(data)
	plt.title(name)

	# Save the plot as an image file
	plt.savefig('{0}.png'.format(name), dpi=300)

def play_sound(data, sample_rate):
	sd.play(data, sample_rate)
	sd.wait()

def pomodoro(work_time, rest_time, freq, save):
	sample_rate = 44100  # Sample rate for the audio
	duration = 5  # Duration of each work/rest period in seconds
	#work_frequency = 432  # Frequency of the sine wave for work time
	#rest_frequency = 440  # Frequency of the sine wave for rest time
	#freq = 33

	print("Starting Pomodoro timer...")
	while True:
		print(f"Work for {work_time} minutes")
		#data = generate_sine_wave(duration, work_frequency, sample_rate)
		data = generate_sine_wave(duration, freq, sample_rate, save)
		os.popen("notify-send WORK").read()
		play_sound(data, sample_rate)
		time.sleep(work_time * 60)

		freq += 3

		print(f"Rest for {rest_time} minutes")
		#data = generate_sine_wave(duration, rest_frequency, sample_rate)
		data = generate_sine_wave(duration, freq, sample_rate, save)
		os.popen("notify-send REST").read()
		play_sound(data, sample_rate)
		time.sleep(rest_time * 60)
		
		freq += 6

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Pomodoro timer')
	parser.add_argument('work_time', type=int, help='work time in minutes')
	parser.add_argument('rest_time', type=int, help='rest time in minutes')
	parser.add_argument('freq', type=int, help='base frequency')
	parser.add_argument('--save', default=0,type=int, help='save samples')
	args = parser.parse_args()
	print(args)

	pomodoro(args.work_time, args.rest_time, args.freq, args.save)
