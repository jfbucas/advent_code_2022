#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

antennas = {}
antinodes = []
antinodess = []

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip()
	line_antennas = list(line.replace(".", ""))

	for a in line_antennas:
		if a not in antennas.keys():
			antennas[a] = []
		antennas[a].extend( [ (x,y) for x, l in enumerate(line) if l == a] )
	
	antinodes.append([" "]*len(line))
	antinodess.append([" "]*len(line))
	y += 1

def add_antinode(y,x,l):
	if y>=0 and y<len(antinodes):
		if x>=0 and x<len(antinodes[0]):
			antinodes[y][x] = l

def add_antinodes(y,dy,x,dx,l):
	i=0
	added=True
	while added:
		added = False
		if y+dy*i>=0 and y+dy*i<len(antinodess):
			if x+dx*i>=0 and x+dx*i<len(antinodess[0]):
				antinodess[y+dy*i][x+dx*i] = l
				added = True
		i+=1

############################
# Part 1

total=0
for atype in antennas.keys():
	for a in antennas[atype]:
		for b in antennas[atype]:
			if a == b:
				continue

			xa,ya = a
			xb,yb = b

			if xa <= xb:
				if ya <= yb:
					add_antinode(ya-abs(yb-ya), xa-abs(xb-xa), 'A')
					add_antinode(yb+abs(yb-ya), xb+abs(xb-xa), 'B')
				else:
					add_antinode(ya+abs(yb-ya), xa-abs(xb-xa), 'C')
					add_antinode(yb-abs(yb-ya), xb+abs(xb-xa), 'D')
			else:
				if ya <= yb:
					add_antinode(ya-abs(yb-ya), xa+abs(xb-xa), 'E')
					add_antinode(yb+abs(yb-ya), xb-abs(xb-xa), 'F')
				else:
					add_antinode(ya+abs(yb-ya), xa+abs(xb-xa), 'G')
					add_antinode(yb-abs(yb-ya), xb-abs(xb-xa), 'H')

for a in antinodes:
	print("".join(a))

total = len("".join([ "".join(a).replace(" ","") for a in antinodes ]))

print("Part1:", total)

############################
# Part 2

for atype in antennas.keys():
	for a in antennas[atype]:
		for b in antennas[atype]:
			if a == b:
				continue

			xa,ya = a
			xb,yb = b

			if xa <= xb:
				if ya <= yb:
					add_antinodes(ya, -abs(yb-ya), xa, -abs(xb-xa), 'A')
					add_antinodes(yb, +abs(yb-ya), xb, +abs(xb-xa), 'B')
				else:
					add_antinodes(ya, +abs(yb-ya), xa, -abs(xb-xa), 'C')
					add_antinodes(yb, -abs(yb-ya), xb, +abs(xb-xa), 'D')
			else:
				if ya <= yb:
					add_antinodes(ya, -abs(yb-ya), xa, +abs(xb-xa), 'E')
					add_antinodes(yb, +abs(yb-ya), xb, -abs(xb-xa), 'F')
				else:
					add_antinodes(ya, +abs(yb-ya), xa, +abs(xb-xa), 'G')
					add_antinodes(yb, -abs(yb-ya), xb, -abs(xb-xa), 'H')
for a in antinodess:
	print("".join(a))

total = len("".join([ "".join(a).replace(" ","") for a in antinodess ]))


print("Part2:", total)

