#!/usr/bin/python3

import sys
import functools
sys.setrecursionlimit(32768)

PROGRESS = False # True # False #True
PART_ONE = True
PART_TWO = True #False

f = open("lists.txt", "r")
#f = open("minilists.txt", "r")

recurs_counter = 0

lists = []
one = None
two = None
for line in f.readlines():
	line = line.strip()

	if one == None:
		one = eval(line)
	elif two == None:
		two = eval(line)
	else:
		lists.append( (one, two) )
		one = None
		two = None
		


def compare(A, B, depth=0):

	ta = str(type(A))
	tb = str(type(B))

	if PROGRESS:
		print("  "*depth, A, ta, " -Vs- ", B, tb)

	if ta == tb:
		
		if ta == "<class 'list'>":
			la = len(A)
			lb = len(B)

			lrange = 0
			if la == lb:
				lrange = la
			elif la > lb:
				lrange = lb
			elif la < lb:
				lrange = la

			for i in range(lrange):
				result = compare(A[i], B[i], depth+1)
				if result in [ -1, 1 ]:
					return result
			if la > lb:
				return 1
			if la < lb:
				return -1

			return 0
					
		elif ta == "<class 'int'>":
			if A == B:
				return 0
			elif A < B:
				return -1
			else:
				return 1
		else:
			print("  "*depth, "Strange type:", ta, tb)

	else:
		if ta == "<class 'list'>" and tb == "<class 'int'>":
			return compare(A, [ B ], depth+1)

		if ta == "<class 'int'>" and tb == "<class 'list'>":
			return compare([ A ], B, depth+1)
		
		print("  "*depth, "Strange mixed types", ta, tb)


	return -2


# Chapter One
if PART_ONE:
	results = []
	for one, two in lists:
		result = compare(one, two, 0)
		results.append( result )

	print(sum([ i+1 for i in range(len(results)) if results[i] in [ -1, 0 ] ]))


# Chapter Two
if PART_TWO:

	all_lists = []
	for one, two in lists:
		all_lists.append(one)
		all_lists.append(two)
	
	all_lists.append( [[2]] )
	all_lists.append( [[6]] )

	all_lists = sorted(all_lists, key=functools.cmp_to_key(compare))
	
	result = 1
	index = 1
	for l in all_lists:
		#print(l)
		if str(l) in [ "[[2]]", "[[6]]" ]:
			result *= index
		index += 1
	print(result)
