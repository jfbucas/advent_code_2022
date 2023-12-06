#!/usr/bin/python3

import re
import sys

f = open( sys.argv[1], "r" )
lines=f.readlines()

time=list(map(int, re.split(r'\s{2,}', lines[0].strip())[1:]))
dist=list(map(int, re.split(r'\s{2,}', lines[1].strip())[1:]))

records=[]
for race in range(len(time)):
	winners=[]

	for button_time in range(time[race]):
		d = button_time * (time[race]-button_time)
		if d > dist[race]:
			winners.append(button_time)
	records.append(len(winners))

answer=1
for r in records:
	answer*=r

print(answer)
			
