#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

room=[]
instructions=[]
robot=(0,0)

move = { ">":(1,0), "v":(0,1), "<":(-1,0), "^":(0,-1) }

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip()
	if len(line) > 0:
		if "@" in line:
			x=line.index("@")
			robot=(x,y)
		if ">" in line:
			instructions.extend(list(line))
		else:
			room.append(list(line))
			y+=1

#for r in room:
#	print(r)
#print(robot)
#print(instructions)

def move_stuff(room, pos, d):
	px, py = pos
	dx, dy = d
	nx, ny = px+dx, py+dy
	if room[ny][nx] == ".":
		tmp = room[ny][nx]
		room[ny][nx] = room[py][px]
		room[py][px] = tmp
		return True
	elif room[ny][nx] == "O":
		if move_stuff(room, (nx,ny), d):
			tmp = room[ny][nx]
			room[ny][nx] = room[py][px]
			room[py][px] = tmp
			return True

	return False
		
def print_room(room):
	print("------")
	for r in room:
		print("".join(r))

def get_gps(room):
	result = []
	y = 0
	for r in room:
		x = 0
		for o in r:
			if o == "O":
				#result.append( (x,y) )
				result.append( x+y*100 )
			x+=1
		y+=1
	return result	

############################
# Part 1

total=0
for i in instructions:
	if move_stuff(room, robot, move[i]):
		robot = (robot[0]+move[i][0], robot[1]+move[i][1])

print_room(room)
total = sum(get_gps(room))

print("Part1:", total)

############################
# Part 2

# With the corrected data
total=0

print("Part2:", total)

