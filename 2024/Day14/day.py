#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

robots=[]

f = open( sys.argv[1], "r" )
for line in f.readlines():
	line = line.strip()
	robots.append(tuple(map(int,re.findall(r"[-]*\d+", line))))

#for r in robots:
#	print(r)

WX,WY=1,1
if len(robots) <= 12:
	WX,WY=11,7
else:
	WX,WY=101,103

def print_map(robots):
	mappy=[]
	for y in range(WY):
		mappy.append( list(["."]*WX) )
	for r in robots:
		if mappy[r[1]][r[0]] != ".":
			mappy[r[1]][r[0]] += 1
		else:
			mappy[r[1]][r[0]] = 1
	for m in mappy:
		print("".join(map(str,m)))

def move_robots(robots):
	nrobots = []
	for r in robots:
		nx=r[0]+r[2]
		ny=r[1]+r[3]
		if nx < 0:
			nx += WX
		if ny < 0:
			ny += WY
		if nx >= WX:
			nx -= WX
		if ny >= WY:
			ny -= WY
		nrobots.append( (nx,ny, r[2],r[3]) )
	return nrobots

def count_quadrants(robots):
	count=[0,0,0,0]
	mx, my = WX//2, WY//2
	for r in robots:
		if r[0]<mx and r[1]<my:
			count[0]+=1
		elif r[0]>mx and r[1]<my:
			count[1]+=1
		elif r[0]>mx and r[1]>my:
			count[2]+=1
		elif r[0]<mx and r[1]>my:
			count[3]+=1
		else:
			#print("piggy in the middle")
			pass
	
	return count

def symetrical(robots):
	mappy=[]
	for y in range(WY):
		mappy.append( list([" "]*WX) )

	for r in robots:
		mappy[r[1]][r[0]] = "X"

	mx, my = WX//2, WY//2
	for m in mappy:
		if "XXXXXXXX" in "".join(map(str,m)):
			return True
	return False


############################
# Part 1

total=1
r=robots
for i in range(100):
	r=move_robots(r)

for c in count_quadrants(r):
	total *= c

print("Part1:", total)

############################
# Part 2

# With the corrected data
total=0

r=robots
while not symetrical(r):
	r = move_robots(r)
	total+=1

print_map(r)

print("Part2:", total)

