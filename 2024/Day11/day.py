#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

stones=[]

f = open( sys.argv[1], "r" )
for line in f.readlines():
	stones=list(map(int,line.strip().split(" ")))

def do_rules(number):
	if number == 0:
		return [ 1 ]

	sn = str(number)
	if len(sn)%2 == 0:
		return [ int(sn[:len(sn)//2]), int(sn[len(sn)//2:]) ]
	
	return [ number*2024 ]

def do_line(stones):
	new_stones = []
	for s in stones:
		new_stones.extend(do_rules(s))
	return new_stones


def to_meta(stones):
	return {i:stones.count(i) for i in stones}

def do_meta_line(meta_stones):
	new_meta_stones = {}
	for ms in meta_stones.keys():
		ns = do_rules(ms)
		for s in ns:
			if s not in new_meta_stones.keys():
				new_meta_stones[s] = 0
			new_meta_stones[s] += meta_stones[ms]

	return new_meta_stones

############################
# Part 1

new_stones = stones
for i in range(25):
	new_stones = do_line(new_stones)

total=len(new_stones)

print("Part1:", total)

############################
# Part 2

new_meta_stones = to_meta(stones)
for i in range(75):
	new_meta_stones = do_meta_line(new_meta_stones)

total=sum([x[1] for x in new_meta_stones.items()])

print("Part2:", total)

