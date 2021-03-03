#!/usr/bin/python3
import os, json
from datetime import datetime

filename = "/home/nuvhandra/src/Ruby-ERB-Sinatra-Task-Scheduler/public/history.json"
f = open(filename, "r")
tasks = json.load(f)
f.close()

#get datetime now
nowt = datetime.now()

def sendNotification(task):
	os.popen("notify-send -i /home/nuvhandra/Pictures/xek.png '" + task + "'")

def main():
	for i in tasks:
		if i['srttime']:
			hour_now = int(nowt.strftime("%H"))
			min_now = int(nowt.strftime("%M"))
			strtime_hour = int(i['srttime'].split(':')[0])
			strtime_min = int(i['srttime'].split(':')[1])
			if i['endtime']:
				endtime_hour = int(i['endtime'].split(':')[0])
				endtime_min = int(i['endtime'].split(':')[1])
				if hour_now >= strtime_hour and hour_now <= endtime_hour:
					if min_now >= strtime_min and min_now <= endtime_min:
						if i['duedate'] == '':
							sendNotification(i['comd'])
						elif i['duedate'] == nowt.strftime("%Y-%m-%d"):
							sendNotification(i['comd'])
			else:
				if hour_now >= strtime_hour:
					if min_now >= strtime_min:
						if i['duedate'] == '':
							sendNotification(i['comd'])
						elif i['duedate'] == nowt.strftime("%Y-%m-%d"):
							sendNotification(i['comd'])
		else:
			if i['duedate'] == nowt.strftime("%Y-%m-%d"):
				sendNotification(i['comd'])

main()
