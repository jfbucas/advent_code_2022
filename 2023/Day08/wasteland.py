#!/usr/bin/python3

import re
import sys
import itertools
import math

f = open( sys.argv[1], "r" )
instructions=""
network={}
for line in f.readlines():
	if instructions == "":
		instructions=line.strip()
	else:
		if line.strip() == "":
			pass
		else:
			line=line.strip().replace("(", "").replace(")", "").replace(",","").split(" ")
			network[line[0]] = {"L": line[2], "R": line[3]}


#print(instructions)
#print(network)

cursor = "AAA"
i = 0
steps = 0
while cursor != "ZZZ":
	cursor = network[cursor][instructions[i]]
	i+=1
	if i >= len(instructions):
		i = 0
	steps+=1

print(steps)


# Part 2
cursors = [ x for x in network.keys() if x.endswith("A") ]

def period_length(cursor):
	i = 0
	steps = 0
	while True:
		cursor = network[cursor][instructions[i]]
		steps += 1
		i+=1
		if i >= len(instructions):
			i = 0
		if cursor[2] == "Z":
			return steps


all_periods=[]
for c in cursors:
	all_periods.append(period_length(c))


a=all_periods[0]
multi=1
for p in all_periods[1:]:
	b=p
	while True:
		if a*multi % b == 0:
			print("Found multiple:", multi)
			a = a*multi
			multi=1
			break
		multi += 1
print(a)

#for p in all_periods:
#	print(p)
#	#print(math.gcd(largest, p[0]))


exit()

i = 0
steps = 0
END = "Z" * len(cursors)
while "".join([ x[2] for x in cursors ]) != END:

	for c in range(len(cursors)):
		#if cursors[c][2] != "Z":
		cursors[c] = network[cursors[c]][instructions[i]]

	i += 1
	if i >= len(instructions):
		i = 0
		print( "".join([ x[2] for x in cursors ]), END)
	steps += 1

print(steps)
