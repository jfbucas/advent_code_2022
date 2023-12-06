#!/usr/bin/python3

import functools
import sys
import itertools
from operator import methodcaller

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
PART_ONE = True
PART_TWO = True

f = open("coords.txt", "r")
MINI=False
#f = open("minicoords.txt", "r")
#MINI=True

coords = []
coordstxt = []
for line in f.readlines():
	line = line.strip()

	coords.append( list(map(int,line.split(","))) )
	#coordstxt.append( line )

# Adjust the coordinates so that they are not at 0
newcoords = []
for [x,y,z] in coords:
	newcoords.append( [x+3, y+3, z+3] )
coords = newcoords

coordstxt = []
for [x,y,z] in coords:
	coordstxt.append( str(x)+","+str(y)+","+str(z) )


#print(coords)
#print(coordstxt)
minx = miny = minz = 128
maxx = maxy = maxz = -128
for [x,y,z] in coords:
	if x < minx: minx = x
	if y < miny: miny = y
	if z < minz: minz = z
	if x > maxx: maxx = x
	if y > maxy: maxy = y
	if z > maxz: maxz = z

print("Min:", minx, miny, minz )
print("Max:", maxx, maxy, maxz )

# We make the volume bigger
minx = 0
miny = 0
minz = 0
maxx += 3
maxy += 3
maxz += 3

print("Min:", minx, miny, minz )
print("Max:", maxx, maxy, maxz )

# Create the volume
volume = []
for x in range(minx, maxx+1):
	volume.append( [] )
	for y in range(miny, maxy+1):
		volume[x].append( [] )
		for z in range(minz, maxz+1):
			volume[x][y].append( 0 )

# Mark the obsidian
for [x,y,z] in coords:
	volume[x][y][z] = 2

#print(volume)

# Floooood
def flood(x, y, z):
	result = 0
	volume[x][y][z] = 1
	for d in [-1, 1]:
		if x+d > minx and x+d < maxx:
			if volume[x+d][y][z] == 0:
				result += flood(x+d, y, z)
			elif volume[x+d][y][z] == 2:
				result += 1
			
		if y+d > miny and y+d < maxy:
			if volume[x][y+d][z] == 0:
				result += flood(x, y+d, z)
			elif volume[x][y+d][z] == 2:
				result += 1

		if z+d > minz and z+d < maxz:
			if volume[x][y][z+d] == 0:
				result += flood(x, y, z+d)
			elif volume[x][y][z+d] == 2:
				result += 1
	return result
	

# Chapter One
if PART_ONE:

	surface = 0
	for [x,y,z] in coords:
		for dx in [-1, 1]:
			if str(x+dx)+","+str(y)+","+str(z) not in coordstxt:
				surface += 1
		for dy in [-1, 1]:
			if str(x)+","+str(y+dy)+","+str(z) not in coordstxt:
				surface += 1
		for dz in [-1, 1]:
			if str(x)+","+str(y)+","+str(z+dz) not in coordstxt:
				surface += 1

	print("Part1: Surface =", surface)

# Chapter Two
if PART_TWO:
	surface2 = flood(minx, miny, minz)
	print("Part2: Surface =", surface2)

