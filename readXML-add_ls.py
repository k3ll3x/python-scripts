#!/usr/bin/python3
import xml.etree.ElementTree as et
import os

t = et.parse(input("load xml file: "))
r = t.getroot()

path = input('Set a path to read from')

#read from path all files and add them as item elements to the tree
l = os.popen("cd " + path + ";ls").read().split('\n')
for i in l:
	if i != '':
		item = r.makeelement('item', {})
		r.append(item)
		name = r[-1].makeelement('name',{})
		name.text = i
		url = r[-1].makeelement('url',{})
		url.text = path + i
		r[-1].append(url)
		rating = r[-1].makeelement('rating',{})
		rating.text = "3"
		r[-1].append(rating)
		breedability = r[-1].makeelement('breedability',{})
		breedability.text = "3"
		r[-1].append(breedability)

t.write(input("output xml file: "))
