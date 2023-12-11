#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

sky = []
stars = []
WIDTH  = 0
HEIGHT = 0

def load_sky():
	global sky, stars, WIDTH, HEIGHT
	sky = []
	f = open( sys.argv[1], "r" )
	for line in f.readlines():
		line=line.strip()
		sky.append(list(line))

	WIDTH  = len(sky[0])
	HEIGHT = len(sky)

	stars = []
	for y in range(HEIGHT):
		for x in range(WIDTH):
			if sky[y][x] == "#":
				stars.append( [x, y,  x, y] )

def expand_universe(expansion):
	line_list=[]
	for y in range(HEIGHT):
		for x in range(WIDTH):
			if sky[y][x] == "#":
				break
		else:
			line_list.append( y )

	col_list=[]
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if sky[y][x] == "#":
				break
		else:
			col_list.append( x )


	for c in col_list:
		for s in stars:
			if s[0] > c:
				s[2] += expansion

	for l in line_list:
		for s in stars:
			if s[1] > l:
				s[3] += expansion
		


def distance(xa,ya, xb,yb):
	if xa > xb:
		if ya > yb:  return xa-xb + ya-yb
		if ya < yb:  return xa-xb + yb-ya
		if ya == yb: return xa-xb + 0
	if xa < xb:
		if ya > yb:  return xb-xa + ya-yb
		if ya < yb:  return xb-xa + yb-ya
		if ya == yb: return xb-xa
	if xa == xb:
		if ya > yb:  return ya-yb
		if ya < yb:  return yb-ya
		if ya == yb: return 0

def total_distance():
	total = 0
	for _,_, xa,ya in stars:
		for _,_, xb,yb in stars:
			total += distance(xa,ya, xb,yb)

	return total//2


load_sky()
expand_universe(1)
print( total_distance() )

load_sky()
expand_universe(10-1)
print( total_distance() )

load_sky()
expand_universe(100-1)
print( total_distance() )

load_sky()
expand_universe(1000000-1)
print( total_distance() )

