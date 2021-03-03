#!/usr/bin/python3
from datetime import datetime
import json, re, random

#format:
#	task string whatever due-date start-time end-time
#all days format
#	whatever notification-time
#notification at due date
#	whatever due-date
#	whatever due-date start-time
task = input("task (due_date start_time end_time)?: ")

#filename = "test.json"
filename = "/home/nuvhandra/src/Ruby-ERB-Sinatra-Task-Scheduler/public/history.json"
f = open(filename, "r+")
tasks = json.load(f)

date_regex = "\d{4}-\d{2}-\d{2}"
duedate = re.findall(date_regex, task)[0] if re.findall(date_regex, task) else ""
time_regex = "\d{2}:\d{2}"
times = re.findall(time_regex, task) if re.findall(time_regex, task) else ""
tasks.append(
	{
		'comd': re.findall(".+?(?=\d{4}-\d{2}-\d{2}|\d{2}:\d{2}|$)", task)[0],
		'srttime': times[0] if len(times) >= 1 else "",
		'endtime': times[1] if len(times) > 1 else "",
		'duedate': duedate,
		'timestamp': str(datetime.now()),
		'id': random.randint(1000, 9999)
	}
)
f.seek(0)
json.dump(tasks, f)
f.truncate()
f.close()
