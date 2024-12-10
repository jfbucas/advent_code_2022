#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

topo=[]
heads=[]

f = open( sys.argv[1], "r" )
for line in f.readlines():
	t = []
	for h in list(line.strip()):
		if h == ".":
			t.append(-1)
		else:
			t.append(int(h))
	topo.append( t )

# List the trailheads
y=0
for t in topo:
	x=0
	for h in t:
		if h == 0:
			heads.append((x,y))
		x+=1 
	y+=1

directions=[ (0,-1), (1,0), (0,1), (-1,0) ]

def print_topo(cx,cy):
	y=0
	for t in topo:
		x=0
		o=""
		for h in t:
			if x==cx and y==cy:
				o+="X"
			else:
				if h == -1:
					o += "."
				elif h == 10:
					o += "#"
				else:
					o+=str(h)
			x+=1 
		print(o)
		y+=1
	

def find_trails(x,y,h,reached):
	#print("----")
	#print_topo(x,y)
	if h==9:
		if reached == None:
			return 1

		if (x,y,h) in reached:
			return 0
		reached.add( (x,y,h) )
		return 1

	count=0
	for dx,dy in directions:
		nx,ny = x+dx, y+dy
		if nx>=0 and ny>=0 and nx<len(topo[0]) and ny<len(topo):
			if topo[ny][nx] == h+1:
				count += find_trails(nx,ny,h+1,reached)
	
	return count


############################
# Part 1

total=0
for hx,hy in heads:
	reached=set()
	total+=find_trails(hx,hy,0,reached)

print("Part1:", total)

############################
# Part 2

total=0
for hx,hy in heads:
	reached=None
	total+=find_trails(hx,hy,0,reached)

print("Part2:", total)

