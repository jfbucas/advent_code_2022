#!/usr/bin/python3

import re
import sys
import itertools
import math

f = open( sys.argv[1], "r" )

DELTA = [
	(-1, -1),
	( 0, -1),
	( 1, -1),
	(-1,  0),
	( 1,  0),
	(-1,  1),
	( 0,  1),
	( 1,  1),
	]

schema=[]
for line in f.readlines():
	line=line.strip()
	schema.append(line)

WIDTH  = len(schema[0])
HEIGHT = len(schema)

def find_symbol(list_coord):
	for x,y in list_coord:
		for dx, dy in DELTA:
			if x+dx >= 0 and x+dx < WIDTH and y+dy >= 0 and y+dy < HEIGHT:
				if schema[y+dy][x+dx] not in ".0123456789":
					return True
	return False

def find_symbol(list_coord):
	for x,y in list_coord:
		for dx, dy in DELTA:
			if x+dx >= 0 and x+dx < WIDTH and y+dy >= 0 and y+dy < HEIGHT:
				if schema[y+dy][x+dx] not in ".0123456789":
					return True
	return False


numbers = []
current_number = None
current_coord = None
for y in range(HEIGHT):
	for x in range(WIDTH):
		if schema[y][x] in "0123456789":
			if current_number == None:
				current_number = ""
				current_coord = []
			current_number += schema[y][x]
			current_coord.append( (x,y) )
		else:
			if current_number != None:
				numbers.append( { "number": int(current_number), "coord": current_coord } )
				current_number = None
				current_coord = None

	if current_number != None:
		numbers.append( { "number": int(current_number), "coord": current_coord } )
		current_number = None
		current_coord = None

total = 0
for n in numbers:
	if find_symbol(n["coord"]):
		total += n["number"]
		

print(total, len(numbers))


# Part 2

stars = []
for y in range(HEIGHT):
	for x in range(WIDTH):
		if schema[y][x] in "*":
			stars.append( { "x":x,"y":y, "voisin": [] } )

for star in stars:
	sx = star["x"]
	sy = star["y"]
	for dx, dy in DELTA:
		if sx+dx >= 0 and sx+dx < WIDTH and sy+dy >= 0 and sy+dy < HEIGHT:
			for n in numbers:
				for nx, ny in n["coord"]:
					if nx == sx+dx and ny == sy+dy:
						if n not in star["voisin"]:
							star["voisin"].append( n )

print(stars)

total = 0
for star in stars:
	print(star)
	if len(star["voisin"]) == 2:
		total += star["voisin"][0]["number"] * star["voisin"][1]["number"]
		

print(total)
