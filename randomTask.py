#!/usr/bin/python3
import os, json, random

filename = "/home/nuvhandra/src/Ruby-ERB-Sinatra-Task-Scheduler/public/history.json"
f = open(filename, "r")
tasks = json.load(f)
f.close()
rnd_inx = random.randint(0, len(tasks))
rnd_task = tasks[rnd_inx]

os.popen("notify-send -i /home/nuvhandra/Pictures/xek.png '" + rnd_task['comd'] + "'")
