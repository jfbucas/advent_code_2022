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

def compare_to_desc(totest, desc):
	if len(totest) != len(desc):
		return None

	for i in range(len(totest)):
		if totest[i] == desc[i] or desc[i] == "?":
			continue
		return None

	return totest


def get_variations(row):

	desc=row["desc"]

	#print(row)
	minimum = []
	for x in row["faulties"][:-1]:
		minimum.append("#"*x)
		minimum.append(".")
	minimum.append("#"*row["faulties"][-1])

	minimum_str = "".join(minimum)
	#print("Min:", minimum, minimum_str)

	if len(minimum_str) > len(desc):
		return { desc:None }

	missing_count = len(desc) - len(minimum_str)
	if missing_count == 0:
		return { desc: [ compare_to_desc(minimum_str, desc) ] }
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
				comp = compare_to_desc("".join(tmp), desc)
				if comp != None:
					if comp not in accepted:
						accepted.append(comp)
				#print(pos, "".join(tmp), desc, len(accepted))

		return { desc: accepted }

total = {}
for s in springs:
	v = get_variations(s)

	for k in v.keys():
		if v[k] != None:
			total[k]= v[k]

total = [ y for x in total.values() for y in x ]
print(len(total))


# Part 2

total = 0
for s in springs:
	a = s["desc"]
	b = s["desc"]+"?"
	c = "?"+s["desc"]+"?"
	d = "?"+s["desc"]

	for l in "abcd":
		exec('s'+l+' = { "desc":'+l+', "faulties":s["faulties"] }')
		exec('v'+l+' = get_variations(s'+l+')')
		exec('c'+l+' = len(v'+l+'['+l+'])')
		exec('c'+l+'ds = len([x for x in v'+l+'['+l+'] if x.startswith(".")])')
		exec('c'+l+'hs = len([x for x in v'+l+'['+l+'] if x.startswith("#")])')
		exec('c'+l+'de = len([x for x in v'+l+'['+l+'] if x.endswith(".")])')
		exec('c'+l+'he = len([x for x in v'+l+'['+l+'] if x.endswith("#")])')

	best_count = 0
	unfolded_str = "?".join([s["desc"]]*5)
	for comb in itertools.product('abcd', repeat=5):
		(c0, c1, c2, c3, c4) = comb
		exec("comb_str = "+c0+"+"+c1+"+"+c2+"+"+c3+"+"+c4)
		if comb_str == unfolded_str:
			exec("comb_count = c"+c0+"*c"+c1+"*c"+c2+"*c"+c3+"*c"+c4+" - (c"+c0+"he*c"+c1+"hs + c"+c1+"he*c"+c2+"hs + c"+c2+"he*c"+c3+"hs + c"+c3+"he*c"+c4+"hs)")
			if best_count < comb_count:
				best_count = comb_count
				print(comb_count)

	total += best_count
	print(a, best_count)

print(total)
