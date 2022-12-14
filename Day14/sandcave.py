#!/usr/bin/python3

import functools
from operator import methodcaller

PART_ONE = False # True
PART_TWO = True # False

f = open("lines.txt", "r")
#f = open("minilists.txt", "r")

recurs_counter = 0

lists = []
for line in f.readlines():
	line = line.strip()

	line = line.split(" -> ")
	line = [ (int(n[0]), int(n[1]))  for n in map(methodcaller("split", ","), line) ]
	lists.append(line)

#print(lists)

minW = min([x for l in lists for (x,y) in l ]) - 10
minH = min([y for l in lists for (x,y) in l ]) - 10
maxW  = max([x for l in lists for (x,y) in l ]) + 10
maxH  = max([y for l in lists for (x,y) in l ]) + 10

caveW = 2**16

print(minW, minH, caveW, maxH)

cave = [ "." ] * (caveW*maxH)

# Print the cave
def printCave():
	print("\033[H\033[2J")
	for h in range(maxH):
		print("".join(cave[minW+h*caveW:maxW+h*caveW]))

# Place a wall
def do_wall( A, B ):
	(x1, y1) = A
	(x2, y2) = B
	if x1 == x2:
		s = y1
		d = y2
		if y1 > y2:
			s = y2
			d = y1
		for y in range(s, d+1):
			cave[x1+y*caveW] = "#"
	elif y1 == y2:
		s = x1
		d = x2
		if x1 > x2:
			s = x2
			d = x1
		for x in range(s, d+1):
			cave[x+y1*caveW] = "#"
	else:
		print("Strange coordinates")

# Place the walls
for walls in lists:
	l = len(walls)
	for i in range(l-1):
		do_wall(walls[i], walls[i+1])


# Chapter One
if PART_ONE:

	sandcount = 0
	startx = 500

	x = startx
	y = 0

	while y < maxH-5:
		ny = y+1
		if cave[x+ny*caveW] == ".":
			y = ny
		elif cave[x-1+ny*caveW] == ".":
			y = ny
			x = x-1
		elif cave[x+1+ny*caveW] == ".":
			y = ny
			x = x+1
		else:
			# Sand rests
			cave[x+y*caveW] = "o"
			x = startx
			y = 0
			sandcount += 1
			printCave()

	print(sandcount)


# Chapter Two
if PART_TWO:
	bottom = max([y for l in lists for (x,y) in l ])+2
	do_wall( (0, bottom), ((2**16)-1, bottom))
	sandcount = 0
	startx = 500
	starty = 0

	x = startx
	y = starty

	while cave[startx+starty*caveW] != "o":
		ny = y+1
		if cave[x+ny*caveW] == ".":
			y = ny
		elif cave[x-1+ny*caveW] == ".":
			y = ny
			x = x-1
		elif cave[x+1+ny*caveW] == ".":
			y = ny
			x = x+1
		else:
			# Sand rests
			cave[x+y*caveW] = "o"

			x = startx
			y = starty

			sandcount += 1

			if sandcount % 1000 == 0:
				printCave()

	print(sandcount)

