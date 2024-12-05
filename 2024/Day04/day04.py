#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

NEEDLE=list("XMAS")

words=[]
f = open( sys.argv[1], "r" )
for line in f.readlines():
	words.append(list(line.strip()))
	

def search_xmas(x, y, dirx, diry):
	i = 0
	while i<len(NEEDLE) and (x>=0) and (y>=0) and (x<len(words[0])) and (y<len(words)) and (words[y][x] == NEEDLE[i]):
		x+=dirx
		y+=diry
		i+=1

	if i == len(NEEDLE):
		return True
	
	return False

def search_x_mas(x, y):

	if words[y][x] != "A":
		return False
	
	if (x==0) or (y==0) or (x==len(words[0])-1) or (y==len(words)-1):
		return False

	if words[y-1][x-1] not in [ "M", "S"]:
		return False
	if words[y+1][x+1] not in [ "M", "S"]:
		return False
	if words[y+1][x-1] not in [ "M", "S"]:
		return False
	if words[y-1][x+1] not in [ "M", "S"]:
		return False

	if words[y-1][x-1] == "M" and words[y+1][x+1] != "S":
		return False
	if words[y-1][x-1] == "S" and words[y+1][x+1] != "M":
		return False

	if words[y-1][x+1] == "M" and words[y+1][x-1] != "S":
		return False
	if words[y-1][x+1] == "S" and words[y+1][x-1] != "M":
		return False

	return True

# Part 1
total=0
for y in range(len(words)):
	for x in range(len(words[0])):
		for diry in [-1,0,1]:
			for dirx in [-1,0,1]:
				total+=int(search_xmas(x,y,dirx,diry))
	
print("Part1:", total)

# Part 2
total=0
for y in range(len(words)):
	for x in range(len(words[0])):
		total+=int(search_x_mas(x,y))
	
print("Part2:", total)

