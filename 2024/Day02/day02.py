#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

reports = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	reports.append( list(map(int, line.strip().split(" "))) )


def eval_safety(r):
	diff=[]
	increase = True
	decrease = True
	toomuch = False
	for i in range(len(r)-1):
		diff.append(r[i+1]-r[i])
		increase = increase and (diff[-1] > 0)
		decrease = decrease and (diff[-1] < 0)
		toomuch  = toomuch or (abs(diff[-1]) not in [1,2,3])
	
	if (increase or decrease) and not toomuch:
		return True

	return False
	
# Part 1
safe = 0
for r in reports:
	safe += int(eval_safety(r))

print("Part1:", safe)


# Part 2
safe = 0
for r in reports:

	for j in range(len(r)):
		nr = list(r)
		nr.pop(j)
		
		diff=[]
		increase = True
		decrease = True
		toomuch = False
		for i in range(len(nr)-1):
			diff.append(nr[i+1]-nr[i])
			increase = increase and (diff[-1] > 0)
			decrease = decrease and (diff[-1] < 0)
			toomuch  = toomuch or (abs(diff[-1]) not in [1,2,3])
				
		if (increase or decrease) and not toomuch:
			#print(diff)
			print(nr, diff)
			safe += 1
			break
		else:
			print("             ", r, nr, diff, increase, decrease, toomuch)
	print()

print("Part2:", safe)

