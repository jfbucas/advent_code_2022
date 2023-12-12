#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

sky = []
stars = []
WIDTH  = 0
HEIGHT = 0

springs = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	line=line.strip()
	line=line.split(" ")
	desc=line[0]
	faulties=list(map(int,line[1].split(",")))
	springs.append({"desc":desc, "faulties":faulties})


def get_str_combinations(input_str):
	combinations = []

	def _get_combinations(prefix, remaining):
		for i in range(1, len(remaining)):
			_get_combinations(prefix + (remaining[:i],), remaining[i:])

		combinations.append(prefix + (remaining,))

	_get_combinations((), input_str)
	return combinations

def compare(totest, desc):
	if len(totest) != len(desc):
		return None

	for i in range(len(totest)):
		if totest[i] == desc[i] or desc[i] == "?":
			continue
		return None

	return totest


def get_variations(row):

	desc=row["desc"]

	print(row)
	minimum = []
	for x in row["faulties"][:-1]:
		minimum.append("#"*x)
		minimum.append(".")
	minimum.append("#"*row["faulties"][-1])

	minimum_str = "".join(minimum)
	#print(minimum, minimum_str)

	if len(minimum_str) > len(desc):
		return 0

	missing_count = len(desc) - len(minimum_str)
	if missing_count == 0:
		return 0 if compare(minimum_str, desc) == None else 1
	else:
		#print("We need to insert ", missing_count, "springs into", minimum_str)
		missing_springs = get_str_combinations("."*missing_count)
		#print(missing_springs)

		accepted=[]
		for missing in missing_springs:
			for pos in itertools.combinations(range(len(minimum)+1), len(missing)):
				tmp = list(minimum)
				rpos = list(reversed(pos))

				#print(tmp)
				for i in range(len(rpos)):
					tmp.insert(rpos[i], missing[i])

				#print(tmp)
				comp = compare("".join(tmp), desc)
				if comp != None:
					if comp not in accepted:
						accepted.append(comp)
				#print(pos, "".join(tmp), desc, len(accepted))

		return len(list(set(accepted)))


#total = 0
#for s in springs:
#	total += get_variations(s)
#
#print(total)

# Part 2

unfolded_springs = []
for s in springs:
	unfolded_springs.append({"desc":"?".join([s["desc"]]*5), "faulties":s["faulties"]*5})

total = 0
for s in unfolded_springs:
	total += get_variations(s)

print(total)
