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
			starttime = nowt.replace(hour=int(i['srttime'].split(':')[0]), minute=int(i['srttime'].split(':')[1]), second=0, microsecond=0)
			if i['endtime']:
				endtime = nowt.replace(hour=int(i['endtime'].split(':')[0]), minute=int(i['endtime'].split(':')[1]), second=0, microsecond=0)
				if nowt >= starttime and nowt <= endtime:
					if i['duedate'] == '':
						sendNotification(i['comd'])
					elif i['duedate'] == nowt.strftime("%Y-%m-%d"):
						sendNotification(i['comd'])
			else:
				if nowt >= starttime:
					if i['duedate'] == '':
						sendNotification(i['comd'])
					elif i['duedate'] == nowt.strftime("%Y-%m-%d"):
						sendNotification(i['comd'])
		else:
			if i['duedate'] != "" and i['duedate'] <= nowt.strftime("%Y-%m-%d"):
				sendNotification(i['comd'])

main()
