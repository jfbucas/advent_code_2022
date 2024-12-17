#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

room=[]
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

def dist_to_finish(p):
	px, py, pd = p
	return (finish[0]-px)*(finish[0]-px) + (finish[1]-py)+(finish[1]-py)


def find_path(pos, score, max_turn):
	curx, cury, curd = pos
	if (curx,cury) == finish:
		return score
	else:
		#if max_turn == 0:
		#	print(".", end="")
			#print("-----")
			#for r in room:
			#	print("".join(r).replace("#", " "))

		best_score = 10000000000

		# Try to move straight
		newx, newy = curx+steps[curd][0], cury+steps[curd][1]
		if room[ newy ][ newx ] == ".":
			room[ newy ][ newx ] = "x"
			tmp_score = find_path((newx, newy, curd), score+1, max_turn)
			if tmp_score < best_score:
				return tmp_score
				best_score = tmp_score
			room[ newy ][ newx ] = "."

		# Try to turn
		if max_turn > 0:
			next_step_options = []
			for newd in turn[curd]:
				newx, newy = curx+steps[newd][0], cury+steps[newd][1]
				if room[ newy ][ newx ] == ".":
					next_step_options.append((newx, newy, newd))

			if len(next_step_options) > 0:

				for newx, newy, newd in sorted(next_step_options, key=lambda x:-dist_to_finish(x)):
						
					room[ newy ][ newx ] = "x"
					tmp_score = find_path((newx, newy, newd), score+1001, max_turn-1)
					if tmp_score < best_score:
						return tmp_score
						best_score = tmp_score
					room[ newy ][ newx ] = "."
	
		#print(best_score)
		return best_score


	

############################
# Part 1

total=0

# Start on S, facing East
robot=(start[0],start[1],0)

best_score = 10000000000
#for mt in range(0,40):
for mt in range(150,200):
	print("Trying",mt,"turns")
	tmp_score = find_path(robot, 0, mt)
	if tmp_score < best_score:
		best_score = tmp_score
		break
print(best_score)
exit()
print("Part1:", total)


############################
# Part 2

total=0
print("Part2:", total)

