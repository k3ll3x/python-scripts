#!/usr/bin/python3

#Author: Siegfried Paul Keller Schippner

#run this script as super user

#based on:
#	https://www.cyberciti.biz/faq/linux-add-a-swap-file-howto/

import random, string, os

def get_random_string(n):
	letters = string.ascii_lowercase
	rstr = "".join(random.choice(letters) for i in range(n))
	return rstr

def update_fstab(str):
	f = open("/etc/fstab")
	content = f.read()
	f.close()

	content += "\n" + str
	f = open("/etc/fstab", "w")
	f.write(content)
	f.close()

def create_swap(size, swap_filename = "swap" + get_random_string(random.randint(0,4))):
	"Creates swap as root, size is in MB"

	logs = []

	#Create Storage File
	size = 1024 * size
	cmd = "dd if=/dev/zero of=/" + swap_filename + " bs=1024 count=" + str(size)
	logs.append(os.popen(cmd).read())

	#Secure swap file
	cmd = "chown root:root /" + swap_filename
	logs.append(os.popen(cmd).read())
	cmd = "chmod 0600 /" + swap_filename
	logs.append(os.popen(cmd).read())

	#Setup a Linux swap area
	cmd = "mkswap /" + swap_filename
	logs.append(os.popen(cmd).read())

	#Enabling the swap file
	cmd = "swapon /" + swap_filename
	logs.append(os.popen(cmd).read())

	#Update /etc/fstab file
	update_fstab("/" + swap_filename + " none swap sw 0 0")

	#swap activated?
	logs.append(os.popen("free -m").read())

	#swap usage summary
	logs.append(os.popen("swapon -s").read())

	return logs

def main():
	logs = create_swap(
		int(input("size in MB (default=700): ") or '700')
	)
	ch = input("print logs? (y/n): ")
	if ch == "y":
		for i in logs:
			print(i)

main()
