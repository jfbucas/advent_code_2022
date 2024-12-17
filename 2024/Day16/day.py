#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

MAX=100000000000

room=[]
room_score={}
best_seats={}
start=(0,0)
finish=(0,0)
robot=(0,0,0)

steps = { 0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1) }
turn = { 0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2] }

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip()
	if "S" in line:
		x=line.index("S")
		start=(x,y)
	if "E" in line:
		x=line.index("E")
		finish=(x,y)
	room.append(list(line.replace("S",".").replace("E",".")))
	y+=1

# Define room infinity
y=0
for r in room:
	x=0
	for s in r:
		for d in [0,1,2,3]:
			room_score[ (x,y,d) ] = MAX
		x+=1
	y+=1

def dist_to_finish(p):
	px, py, pd = p
	return (finish[0]-px)*(finish[0]-px) + (finish[1]-py)+(finish[1]-py)


def find_path(pos, score):
	room_score[ pos ] = score
	curx, cury, curd = pos

	if (curx,cury) == finish:
		if score not in best_seats.keys():
			best_seats[score]=[]
			for r in room:
				tmp = []
				for c in r:
					tmp.append(" ")
				best_seats[score].append(tmp)
		y=0
		for r in room:
			x=0
			for c in r:
				if c == "x":
					best_seats[score][y][x]=c
				x+=1
			y+=1

	# Try to move straight
	newx, newy = curx+steps[curd][0], cury+steps[curd][1]
	if room[ newy ][ newx ] == "." and room_score[ (newx,newy,curd) ] >= score+1:
		room[ newy ][ newx ] = "x"
		find_path((newx, newy, curd), score+1)
		room[ newy ][ newx ] = "."

	# Try to turn
	next_step_options = []
	for newd in turn[curd]:
		newx, newy = curx+steps[newd][0], cury+steps[newd][1]
		if room[ newy ][ newx ] == "." and room_score[ (newx,newy,newd) ] >= score+1001:
			room[ newy ][ newx ] = "x"
			find_path((newx, newy, newd), score+1001)
			room[ newy ][ newx ] = "."


	

############################
# Part 1

total=0

# Start on S, facing East
robot=(start[0],start[1],0)

room[ start[1] ][ start[0] ] = "x"
find_path(robot, 0)
room[ start[1] ][ start[0] ] = "."
total = min([room_score[ (finish[0],finish[1],d) ] for d in [0,1,2,3]])
print("Part1:", total)


############################
# Part 2

total = "".join(["".join(r) for r in best_seats[total]]).count("x")
print("Part2:", total)

