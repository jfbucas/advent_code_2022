#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

def check():
	total = 0
	for line in numbers:
		first = None
		last  = None
		for n in line:
			if n in "0123456789":
				first=n
				break

		for n in reversed(line):
			if n in "0123456789":
				last=n
				break

		print(first, last, "".join(line)) 
		total += int(first+last) 

	print(total)

#numbers = []
#f = open( sys.argv[1], "r" )
#for line in f.readlines():
#	line=line.strip()
#	numbers.append(list(line))

#check()


# Part 2
nombres = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

numbers = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	line=line.strip()

	print(line)
	found = False
	for i in range(len(line)):
		if line[i] in "0123456789":
			break
		for n in nombres:
			if line[i:i+len(n)] == n:
				line = line[0:i]+str(nombres.index(n))+line[i+len(n):]
				found = True
				break
		if found:
			break


	found = False
	for i in reversed(range(len(line))):
		if line[i] in "0123456789":
			break
		for n in nombres:
			if line[i:i+len(n)] == n:
				line = line[0:i]+str(nombres.index(n))+line[i+len(n):]
				found = True
				break
		if found:
			break

	print(line)
	numbers.append(list(line))

check()
