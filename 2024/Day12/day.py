#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

plot=[]

f = open( sys.argv[1], "r" )
for line in f.readlines():
	plot.append(list(line.strip()))


def propagate_region(pos, plot_list, region_number):
	(x,y) = pos
	plot_list.remove(pos)
	result=[(x,y,region_number)]
	for newpos in [(x,y-1),(x+1,y),(x,y+1), (x-1,y)]:
		if newpos in plot_list:
			result.extend( propagate_region(newpos, plot_list, region_number) )
	return result

def get_regions(plot):
	plot_types={}
	y = 0
	for row in plot:
		x =0
		for p in row:
			if p not in plot_types.keys():
				plot_types[p] = set()
			plot_types[p].add( (x,y) )
			x+=1
		y+=1


	regions=[]
	for p in plot_types.keys():

		while len(plot_types[p]) > 0:
			regions.append( propagate_region(list(plot_types[p])[0], plot_types[p], len(regions) ) )

	return regions

def calculate_perimeter(region):
	perimeter=0
	for x,y,_ in region:
		for nx,ny in [(x,y-1),(x+1,y),(x,y+1), (x-1,y)]:
			if (nx,ny,_) not in region:
				perimeter+=1
	return perimeter

def calculate_sides(region):
	sides=0
	sides_seen = set()
	for x,y,_ in region:
		for dx,dy, ddx,ddy in [(0,-1, 1,0),(+1,0, 0,1),(0,+1, 1,0),(-1,0, 0,1)]:
			seen_count = 0
			for muld in [ -1, 1]:
				mul=0
				while True:
					rx,ry = x   + ddx*muld*mul, y   + ddy*muld*mul
					ex,ey = x+dx+ ddx*muld*mul, y+dy+ ddy*muld*mul
					if (rx,ry,_) in region and \
					   (ex,ey,_) not in region:
						if (rx,ry,ex,ey) not in sides_seen:
							sides_seen.add( (rx,ry,ex,ey) )
							seen_count += 1 
					else:
						break
					mul += 1

				if seen_count > 0:
					sides+=1
	return sides

regions = get_regions(plot)

############################
# Part 1

total=0
for r in regions:
	total += len(r)*calculate_perimeter(r)

print("Part1:", total)

############################
# Part 2

total=0
for r in regions:
	total += len(r)*calculate_sides(r)

print("Part2:", total//2)

