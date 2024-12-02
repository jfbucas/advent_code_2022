#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

listA = []
listB = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	line=line.strip().split(" ")

	listA.append(int(line[0]))
	listB.append(int(line[3]))

listA = sorted(listA)
listB = sorted(listB)

# Part 1
listAB=zip(listA,listB)

sumd=0
for a,b in listAB:
	d = abs(a-b)
	sumd += d

print("Part1:", sumd)

# Part 2
similarity=0
for a in listA:
	count = 0
	for b in listB:
		if a==b:
			count+=1

	similarity += a*count 
		
print("Part2:", similarity)
