#!/usr/bin/python3
import requests, os, random
r = requests.get("https://type.fit/api/quotes")
os.popen("export DISPLAY=:0")
json = r.json()
t = json[random.randint(0, len(json) - 1)]
limit = 40
t['text'] = '-\n'.join(t['text'][i:i+30] for i in range(0, len(t['text']), 30))
os.popen("notify-send '{0}' '{1}'".format(t['text'], t['author']))
