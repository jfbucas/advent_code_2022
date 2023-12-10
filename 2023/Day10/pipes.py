#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

DELTA = [
	( 0, -1),
	(-1,  0),
	( 1,  0),
	( 0,  1),
	]

PIPES_DELTA = {
	"S" : [ (-1,  0), ( 0, -1), ( 1,  0), ( 0,  1) ],
	"F" : [ ( 1,  0), ( 0,  1) ],
	"7" : [ (-1,  0), ( 0,  1) ],
	"L" : [ ( 0, -1), ( 1,  0) ],
	"J" : [ ( 0, -1), (-1,  0) ],
	"|" : [ ( 0, -1), ( 0,  1) ],
	"-" : [ (-1,  0), ( 1,  0) ],
	"." : [],
	}

f = open( sys.argv[1], "r" )

pipes=[]
for line in f.readlines():
	line=line.strip()
	pipes.append(list(line))

WIDTH  = len(pipes[0])
HEIGHT = len(pipes)

def find_start():
	for y in range(HEIGHT):
		for x in range(WIDTH):
			if pipes[y][x] == "S":
				return (x, y)

start = find_start()
print(start)



visited = []
for y in range(HEIGHT):
	visited.append( [ None ] * WIDTH )

def find_loop(x,y, depth):
	if visited[y][x] != None:
		return depth

	visited[y][x] = depth
	pipe = pipes[y][x]

	max_depth = depth
	
	for dx,dy in PIPES_DELTA[pipe]:
		if x+dx >= 0 and x+dx < WIDTH and y+dy >= 0 and y+dy < HEIGHT:
			np = pipes[y+dy][x+dx]
			for ndx,ndy in PIPES_DELTA[np]:
				if dx+ndx == 0 and dy+ndy == 0:
					# if we have a pipe that connects back
					d = find_loop( x+dx, y+dy, depth+1 )
					if d > max_depth:
						max_depth = d
	return max_depth				
				




len_loop = find_loop(start[0], start[1], 0)

for v in visited:
	print(v)

print(len_loop//2)



# Part 2
for y in range(HEIGHT):
	for x in range(WIDTH):
		if visited[y][x] == None:
			pipes[y][x] = "."

repipes = []
for y in range(HEIGHT):
	repipes.append([])
	for x in range(WIDTH):
		repipes[y].append(pipes[y][x])

revisited = []
for y in range(HEIGHT):
	revisited.append( [ False ] * WIDTH )


def get_GD(x,y):
	
	if revisited[y][x]:
		return

	revisited[y][x] = True

	pipe = pipes[y][x]
	for dx,dy in PIPES_DELTA[pipe]:
		if x+dx >= 0 and x+dx < WIDTH and y+dy >= 0 and y+dy < HEIGHT:
			np = pipes[y+dy][x+dx]
			for ndx,ndy in PIPES_DELTA[np]:
				if dx+ndx == 0 and dy+ndy == 0:
					# if we have a pipe that connects back
					if revisited[y+dy][x+dx]:
						continue
					
					if dx == 1:
						if y-1 >= 0 and visited[y-1][x] == None:
							repipes[y-1][x] = "G"
						if y-1 >= 0 and visited[y-1][x+dx] == None:
							repipes[y-1][x+dx] = "G"
						if y+1 < HEIGHT and visited[y+1][x] == None:
							repipes[y+1][x] = "D"
						if y+1 < HEIGHT and visited[y+1][x+dx] == None:
							repipes[y+1][x+dx] = "D"
					
					elif dx == -1:
						if y-1 >= 0 and visited[y-1][x] == None:
							repipes[y-1][x] = "D"
						if y-1 >= 0 and visited[y-1][x+dx] == None:
							repipes[y-1][x+dx] = "D"
						if y+1 < HEIGHT and visited[y+1][x] == None:
							repipes[y+1][x] = "G"
						if y+1 < HEIGHT and visited[y+1][x+dx] == None:
							repipes[y+1][x+dx] = "G"

					
					if dy == 1:
						if x-1 >= 0 and visited[y][x-1] == None:
							repipes[y][x-1] = "D"
						if x-1 >= 0 and visited[y+dy][x-1] == None:
							repipes[y+dy][x-1] = "D"
						if x+1 < WIDTH and visited[y][x+1] == None:
							repipes[y][x+1] = "G"
						if x+1 < WIDTH and visited[y+dy][x+1] == None:
							repipes[y+dy][x+1] = "G"
					elif dy == -1:
						if x-1 >= 0 and visited[y][x-1] == None:
							repipes[y][x-1] = "G"
						if x-1 >= 0 and visited[y+dy][x-1] == None:
							repipes[y+dy][x-1] = "G"
						if x+1 < WIDTH and visited[y][x+1] == None:
							repipes[y][x+1] = "D"
						if x+1 < WIDTH and visited[y+dy][x+1] == None:
							repipes[y+dy][x+1] = "D"
					

					get_GD( x+dx, y+dy )
				
		
get_GD(start[0], start[1])



def fill_GD():
	changed = True
	while changed:
		changed = False
		for y in range(HEIGHT):
			for x in range(WIDTH):
				c = repipes[y][x]
				if c in ["G", "D"]:
					for dx,dy in DELTA:
						if x+dx >= 0 and x+dx < WIDTH and y+dy >= 0 and y+dy < HEIGHT:
							if repipes[y+dy][x+dx] == ".":
								repipes[y+dy][x+dx] = c
								changed = True
	count={}
	for y in range(HEIGHT):
		for x in range(WIDTH):
			c = repipes[y][x]
			if c not in count.keys():
				count[c] = 0
			count[c] += 1
						
	return count

result = fill_GD()

for p in repipes:
	print("".join(p))

print(result)
	
