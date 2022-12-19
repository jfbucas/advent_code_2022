#!/usr/bin/python3

import functools
import sys
from operator import methodcaller

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
PART_ONE = True
#PART_TWO = True

f = open("pipes.txt", "r")
f = open("minipipes.txt", "r")


valves = {}
for line in f.readlines():
	line = line.strip()

	line = line.split(";")
	name = line[0].split(" ")[1]
	rate = int(line[0].split("=")[1])

	tunnels = line[1].replace(" tunnel leads to valve ", "").replace(" tunnels lead to valves ", "").replace(",", "").split(" ")
	valves[name] = {}
	valves[name]["rate"] = rate
	valves[name]["tunnels"] = tunnels
	valves[name]["open"] = False
	valves[name]["visited"] = False

print(valves)

leaves = 0
def visitation(time, name):
	global leaves

	if time <= 0:
		leaves += 1
		return

	#valves[name]["visited"] = True

	for t in valves[name]["tunnels"]:
		#if valves[t]["visited"] == False:
		more_time = 0
		if valves[t]["rate"] > 0 and not valves[t]["open"]:
			valves[t]["open"] = True
			more_time = 1
		visitation(time-1-more_time, t)

	#valves[name]["visited"] = False

visitation(20, "AA")

print(leaves)

exit()


lists = list(sensors + beacons)
minW = min([x for (x,y) in lists ])
minH = min([y for (x,y) in lists ])
maxW  = max([x for (x,y) in lists ])
maxH  = max([y for (x,y) in lists ])

print(minW, minH, maxW, maxH)

W=abs(minW)+abs(maxW)
H=abs(minH)+abs(maxH)

sparse_lines = [ ]
for i in range(MAX_Y):
	sparse_lines.append([])

# Calculate the sparse grid
for (sx, sy), (bx, by) in zip(sensors, beacons):
	dx = abs(sx-bx)
	dy = abs(sy-by)
	
	print("Sensor:", sx, ",", sy, "Beacon:", bx, ",", by, "  dx/dy", dx, "/", dy)

	x1 = x2 = None
	starters = None

	starters = [ (sx-dx, sy-dy), (sx-dx, sy+dy) ]

	# /.
	(x,y) = starters[0]
	while y <= sy:
		if y>=0 and y<MAX_Y:
			sparse_lines[ y ].append( (x, sx+sx-x) )
		y += 1
		x -= 1

	(x,y) = starters[0]
	while x <= sx:
		if y>=0 and y<MAX_Y:
			sparse_lines[ y ].append( (x, sx+sx-x) )
		y -= 1
		x += 1
	

	# \.
	(x,y) = starters[1]
	while y >= sy:
		if y>=0 and y<MAX_Y:
			sparse_lines[ y ].append( (x, sx+sx-x) )
		y -= 1
		x -= 1

	(x,y) = starters[1]
	while x <= sx:
		if y>=0 and y<MAX_Y:
			sparse_lines[ y ].append( (x, sx+sx-x) )
		y += 1
		x += 1

# Chapter One
if PART_ONE:

	l2M = [ " " ] * (W*4)
	for x1, x2 in sparse_lines[ M2 ]:
		for x in range(x1, x2):
			l2M[2*W+x] = "#"

	print( "Count:", len([ s for s in l2M if s == "#" ]) )

# Chapter Two
if PART_TWO:
	for m2 in range(MAX_Y):
		slm2 = sorted(sparse_lines[m2], key=lambda x: x[0])
		#print(slm2)

		nslm2 = []
		last_x = -10
		for x1, x2 in slm2:
			if x1 < 0:
				x1 = 0
			if x2 > MAX_X:
				x2 = MAX_X

			if x1 > last_x+1:
				nslm2.append( (x1, x2) )
				last_x = x2
			else:
				if x2 > last_x:
					last_x = x2
				nslm2[-1] = (nslm2[-1][0], last_x)

		if len(nslm2) > 1:
			print(m2, nslm2)

	# 3403960*4000000+3289729
