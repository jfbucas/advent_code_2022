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
room_extend = {
	".":[".", "."],
	"O":["[", "]"],
	"#":["#", "#"],
	"@":["@", "."],
	}

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip()
	if len(line) > 0:
			
		if ">" in line:
			instructions.extend(list(line))
		else:
			new_line = []
			for l in line:
				new_line.extend(room_extend[l])

			room.append(list(new_line))

			if "@" in line:
				x=new_line.index("@")
				robot=(x,y)
			y+=1


def print_room(room):
	print("------")
	for r in room:
		print("".join(r))

def move_stuff(room, robot, d):
	dx, dy = d
	to_move = []
	to_move.append( robot )

	while True:
		
		new_move = []
		for pos in to_move:
			
			px, py = pos
			new_pos = nx, ny = px+dx, py+dy

			if new_pos in to_move:
				continue

			if room[ny][nx] == ".":
				pass

			elif room[ny][nx] == "[":
				new_move.append( (nx,ny) )
				new_move.append( (nx+1,ny) )

			elif room[ny][nx] == "]":
				new_move.append( (nx,ny) )
				new_move.append( (nx-1,ny) )

			elif room[ny][nx] == "#":
				return False

		for n in new_move:
			if n not in to_move:
				to_move.append(n)

		if len(new_move) == 0:
			break

	#print("To move:", to_move)

	for a in reversed(to_move):
		px,py = a
		nx, ny = px+dx, py+dy

		tmp = room[ py ][ px ]
		room[ py ][ px ] = room[ ny ][ nx ]
		room[ ny ][ nx ] = tmp

	return True

def get_gps(room):
	result = []
	y = 0
	for r in room:
		x = 0
		for o in r:
			if o == "[":
				result.append( x+y*100 )
			x+=1
		y+=1
	return result	

print_room(room)
print(robot)
print(instructions)

############################
# Part 2

total=0
for i in instructions:
	moved = move_stuff(room, robot, move[i])
	if moved:
		robot = (robot[0]+move[i][0], robot[1]+move[i][1])

print_room(room)
total = sum(get_gps(room))

print("Part2:", total)

