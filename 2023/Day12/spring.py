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

unfolded_springs = []
for s in springs:
	#unfolded_springs.append({"desc":"?".join([s["desc"]]*5), "faulties":s["faulties"]*5})
	unfolded_springs.append({"desc":s["desc"]+"?", "faulties":s["faulties"]})

total = 0
for s in springs:
	a = s["desc"]
	b = s["desc"]+"?"
	c = "?"+s["desc"]+"?"
	d = "?"+s["desc"]

	sa = { "desc":a, "faulties":s["faulties"] }
	sb = { "desc":b, "faulties":s["faulties"] }
	sc = { "desc":c, "faulties":s["faulties"] }
	sd = { "desc":d, "faulties":s["faulties"] }

	va = get_variations(sa)
	vb = get_variations(sb)
	vc = get_variations(sc)
	vd = get_variations(sd)

	ca = len(va[a])
	cb = len(vb[b])
	cc = len(vc[c])
	cd = len(vd[d])

	best_count = 0
	unfolded_str = "?".join([s["desc"]]*5)
	for comb in itertools.product('abcd', repeat=5):
		exec("comb_str = "+comb[0]+"+"+comb[1]+"+"+comb[2]+"+"+comb[3]+"+"+comb[4])
		if comb_str == unfolded_str:
			exec("comb_count = c"+comb[0]+"*c"+comb[1]+"*c"+comb[2]+"*c"+comb[3]+"*c"+comb[4])
			if best_count < comb_count:
				best_count = comb_count
				print(comb_count)

	total+=best_count
	print(a, best_count)

print(total)
