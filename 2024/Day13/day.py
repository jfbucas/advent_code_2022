#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

A="A"
B="B"
P="P"
nP="nP"
X=0
Y=1
C=2
CORRECTION=10000000000000

machines=[]

f = open( sys.argv[1], "r" )
m = {}
for line in f.readlines():
	line = line.strip()
	if "Button A: " in line:
		m[A] = list(map(int,re.findall(r"\d+", line)))
	elif "Button B: " in line:
		m[B] = list(map(int,re.findall(r"\d+", line)))
	elif "Prize: " in line:
		m[P] = list(map(int,re.findall(r"\d+", line)))
	elif len(line) == 0:
		machines.append(m)
		m = {} 

#for m in machines:
#	print(m)


def find_minimum(m, start=(0,0,0), rangy=100):
	
	solutions=[]
	for b in range(rangy):
		for a in range(rangy):
			x,y = start[X]+a*m[A][X]+b*m[B][X], start[Y]+a*m[A][Y]+b*m[B][Y]
			if x > m[P][X] or y > m[P][Y]:
				break
			if x == m[P][X] and y == m[P][Y]:
				solutions.append((a,b, a*3+b*1+start[C]))
	
	if len(solutions) > 0:
		solutions = sorted(solutions, key=lambda x:x[C])
		return solutions[0]
	
	return None
		
# Maths to the rescue
def find_minimum_corrected(m, c=CORRECTION):

	d = m[A][Y] * m[B][X] - m[A][X] * m[B][Y]
	countA = (m[B][X] * (c+m[P][Y]) - m[B][Y] * (c+m[P][X])) // d
	countB = ((c+m[P][X]) * m[A][Y] - (c+m[P][Y]) * m[A][X]) // d
	if countA >= 0 and countB >= 0 and countA * m[A][X] + countB * m[B][X] == c+m[P][X] and countA * m[A][Y] + countB * m[B][Y] == c+m[P][Y]:
		return 3 * countA + countB

	return None

			

############################
# Part 1

total=0
for m in machines:
	r = find_minimum(m)
	if r != None:
		total += r[C]
		print("Machine", m, "minimum is", r)
	else:
		print("Machine", m, "is impossible")

print("Part1:", total)

############################
# Part 2

# With the corrected data
total=0
for m in machines:
	r = find_minimum_corrected(m)
	if r != None:
		total += r
		print("Machine", m, "minimum is", r)
	else:
		print("Machine", m, "is impossible")


print("Part2:", total)

