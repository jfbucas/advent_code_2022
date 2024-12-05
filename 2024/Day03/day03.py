#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

mul_pattern = re.compile(r'mul\(\d+,\d+\)')
inst_pattern = re.compile(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))')
muls = []
insts = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	muls.extend( mul_pattern.findall(line) )
	insts.extend( inst_pattern.findall(line) )

def eval_mul(m):
	a=int(m.replace("mul(","").split(",")[0])
	b=int(m.replace(")","").split(",")[1])
	return a*b

# Part 1
total=0
for m in muls:
	total+=eval_mul(m)
	
print("Part1:", total)

# Part 2
total = 0
do=True
for i in insts:
	if i in "do()":
		do=True
	elif i in "don't()":
		do=False
	elif do:
		total+=eval_mul(i)


print("Part2:", total)

