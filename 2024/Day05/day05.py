#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

NEEDLE=list("XMAS")

rules_before={}
rules_after={}
interval=False
orders=[]

f = open( sys.argv[1], "r" )
for line in f.readlines():
	line = line.strip()
	if line == "":
		interval=True
		continue
	if not interval:
		line = list(map(int, line.split("|")))

		if line[0] not in rules_before.keys():
			rules_before[line[0]] = []
		if line[1] not in rules_after.keys():
			rules_after[line[1]] = []

		rules_before[line[0]].append(line[1])
		rules_after[line[1]].append(line[0])
	else:
		orders.append(list(map(int, line.split(","))))


def validate_order(o):

	for i in range(len(o)):
		for iafter in range(0,i):
			if o[i] not in rules_after.keys() or \
			   o[iafter] not in rules_after[o[i]]:
				return False
		for ibefore in range(i+1,len(o)):
			if o[i] not in rules_before.keys() or \
			   o[ibefore] not in rules_before[o[i]]:
				return False
	return True

def validate_and_fix_order(o, move=None, movedir=None):

	if move != None:
		if movedir == "before":
			tmp=o[move-1]
			o[move-1]=o[move]
			o[move]=tmp
		if movedir == "after":
			tmp=o[move+1]
			o[move+1]=o[move]
			o[move]=tmp

	for i in range(len(o)):
		for iafter in range(0,i):
			if o[iafter] not in rules_after[o[i]]:
			   	return validate_and_fix_order(o, move=iafter, movedir="after")

		for ibefore in range(i+1,len(o)):
			if o[ibefore] not in rules_before[o[i]]:
			   	return validate_and_fix_order(o, move=ibefore, movedir="before")
	return o


# Part 1
total=0
for o in orders:
	if validate_order(o):
		total+=o[len(o)//2]
	
print("Part1:", total)


# Part 2
total=0
for o in orders:
	if not validate_order(o):
		oo = validate_and_fix_order(list(o))
		total+=oo[len(oo)//2]
	
print("Part2:", total)

