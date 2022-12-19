#!/usr/bin/python3

import functools
from operator import methodcaller

PART_ONE = not False # True
PART_TWO = not True # False

f = open("inbeak.txt", "r")
f = open("miniinbeak.txt", "r")

recurs_counter = 0

lists = []
sensors = []
beacons = []
for line in f.readlines():
	line = line.strip()

	line = line.split(":")
	sensor = eval( "("+line[0].replace("Sensor at ", "").replace("x=", "").replace("y=", "")+")" )
	beacon = eval( "("+line[1].replace("closest beacon is at ", "").replace("x=", "").replace("y=", "")+")" )
	sensors.append(sensor)
	beacons.append(beacon)

print(sensors)
print(beacons)

lists = list(sensors + beacons)
minW = min([x for (x,y) in lists ])
minH = min([y for (x,y) in lists ])
maxW  = max([x for (x,y) in lists ])
maxH  = max([y for (x,y) in lists ])

print(minW, minH, maxW, maxH)

W=abs(minW)+abs(maxW)
H=abs(minH)+abs(maxH)


M2 = 2000000
M2 = 10
line2M = [ " " ] * (W*4)


"""
for (x,y) in sensors:
	x += abs(minW)
	if y == 20000000:
		line2M[x] = "S"

for (x,y) in beacons:
	x += abs(minW)
	if y == 20000000:
		line2M[x] = "B"
"""

for (sx, sy), (bx, by) in zip(sensors, beacons):
	if bx > sx:
		dx = bx-sx
	else:
		dx = sx-bx

	if by > sy:
		dy = by-sy
	else:
		dy = sy-by
	
	

	print(sx, sy, bx, by, " - ", dx, dy)

	x1 = x2 = None
	starters = None

	if sy > by:
		if sx > bx:
			starters = [ (bx, by), (sx+dx, by), (bx, sy+dy), (sx+dx, sy+dy) ]
		else:
			starters = [ (sx-dx, by), (bx, by), (sx-dx, sy+dy), (bx, sy+dy) ]
	else:
		if sx > bx:
			starters = [ (bx, sy-dy), (sx+dx, sy-dy), (bx, by), (sx+dx, by) ]
		else:
			starters = [ (sx-dx, sy-dy), (bx, sy-dy), (sx-dx, by), (bx, by) ]

	print(starters)

	# /.
	(x,y) = starters[0]
	while y <= sy:
		y += 1
		x -= 1
		if y == M2: x1 = x

	(x,y) = starters[0]
	while x <= sx:
		y -= 1
		x += 1
		if y == M2: x1 = x
	
	# .\
	(x,y) = starters[1]
	while y <= sy:
		y += 1
		x += 1
		if y == M2: x2 = x

	(x,y) = starters[1]
	while x >= sx:
		y -= 1
		x -= 1
		if y == M2: x2 = x

	# \.
	(x,y) = starters[2]
	while y >= sy:
		y -= 1
		x -= 1
		if y == M2: x1 = x

	(x,y) = starters[2]
	while x <= sx:
		y += 1
		x += 1
		if y == M2: x1 = x

	# ./
	(x,y) = starters[3]
	while y >= sy:
		y -= 1
		x += 1
		if y == M2: x2 = x

	(x,y) = starters[3]
	while x >= sx:
		y += 1
		x -= 1
		if y == M2: x2 = x

	# Markup the 2M line
	if x1 != None or x2 != None:
		print("Line2M", x1, x2)
		for x in range(x1, x2+1):
			line2M[2*W+x] = "#"
	print()

print( "Count:", len([ s for s in line2M if s == "#" ]) )

"""
def grow(x,y,d):
	result = None
	i = 0
	for j in range(y-d, y+d):
		
		if j == 2000000 + abs(minH):
			if line2M[-i+x] == " ":
				line2M[-i+x] = "#"
			if line2M[i+x] == " ":
				line2M[i+x] = "#"

		#if (i+x, j) in beacons:
		#	result = (i+x, j)


		if j < y:
			i += 1
		elif j >= y:
			i -= 1
	return result

for (x,y) in sensors:
	print("Sensor", x, y)
	x += abs(minW)
	y += abs(minH)
	d = 1
	found_beacon = None
	while found_beacon == None:
		found_beacon = grow(x, y, d)
		d += 1
		print(d, end=" ")
	print("Found beacon at ", found_beacon)
"""


exit()

caveW = 2**16


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

