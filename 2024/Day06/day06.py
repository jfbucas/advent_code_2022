#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

orig_room=[]
orig_guard=[0,0,0]

directions = ( (0,-1), (1,0), (0, 1), (-1,0) )

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip()
	orig_room.append(list(line))
	if "^" in line:
		x=line.index("^")
		orig_guard=[x,y,0]
	y+=1

def turn_guard(guard):
	guard[2] = (guard[2]+1)%len(directions)

def is_obstacle(room,guard):
	try:
		return room[guard[1]+directions[guard[2]][1]][guard[0]+directions[guard[2]][0]] == "#"
	except:
		return False

def move_guard(guard):
	guard[0]+=directions[guard[2]][0]
	guard[1]+=directions[guard[2]][1]


# Part 1
guard=list(orig_guard)
room=[]
for r in orig_room:
	room.append(list(r))

while (guard[0]>=0)and(guard[0]<len(room[0])) and \
	(guard[1]>=0)and(guard[1]<len(room)):
		room[guard[1]][guard[0]] = "X"
		if is_obstacle(room,guard):
			turn_guard(guard)
		move_guard(guard)

for r in room:
	print("".join(r))

total= "".join(["".join(r) for r in room]).count("X")

on_path=[]
for r in room:
	on_path.append(list(r))
	
print("Part1:", total)

# Part 2
total=0

room=[]
for r in orig_room:
	room.append(list(r))

for (x,y) in [(x,y) for x in range(len(room[0])) for y in range(len(room))]:

	print(x,y)
	if on_path[y][x] != "X":
		continue
	
	room[y][x] = "#"
	guard      = list(orig_guard)
	visited    = set()

	while ((guard[0]>=0)and(guard[0]<len(room[0])) and \
		(guard[1]>=0)and(guard[1]<len(room))):

		visited.add( (guard[0],guard[1],guard[2]) )
		if is_obstacle(room,guard):
			turn_guard(guard)
		move_guard(guard)

		if (guard[0],guard[1],guard[2]) in visited:
			# Loop detected
			total+=1 
			break
	
	room[y][x] = orig_room[y][x]
	
print("Part2:", total-4)

