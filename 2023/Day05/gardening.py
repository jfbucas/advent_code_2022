#!/usr/bin/python3

import re
import sys
chain = [ 'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location' ]
f = open( sys.argv[1], "r" )
lines=f.readlines()

# part 1
seeds=list(map(int, re.split(r'\s{1,}', lines[0].strip())[1:]))

# part 2
seeds_range=[]
for i in range(len(seeds)//2):
	seeds_range.append( [{ "begin":seeds[i*2+0], "end":seeds[i*2+0]+seeds[i*2+1]}] )

cartes={}

current_carte=""
for l in lines[1:]:
	l = l.strip()
	if l.endswith(" map:"):
		current_carte=l.replace(" map:","")
		cartes[current_carte] = []
	elif len(l) > 0:
		trip=list(map(int, re.split(r'\s{1,}', l)))
		cartes[current_carte].append( { "dst":trip[0], "src": trip[1], "len": trip[2] } ) # src, len, dst
	elif len(l) == 0:
		if current_carte != "":
			cartes[current_carte] = sorted(cartes[current_carte], key=lambda d: d['src'])

answer=None
for s in seeds:
	cursor = s
	for carte in chain:
		new_cursor = cursor
		for c in cartes[ carte ]:
			if cursor >= c["src"] and cursor <= c["src"]+c["len"]:
				new_cursor = c["dst"]+ (cursor-c["src"])
				break
		cursor = new_cursor
	if answer == None or cursor < answer:
		answer = cursor

print("Part 1:", answer)





def copy_list_ranges(r):
	new_range = []
	for x in r:
		new_range.append({"begin":x["begin"], "end":x["end"]})
	return new_range


answer=None
for sr in seeds_range:
	cursor_list_ranges = copy_list_ranges(sr)
	for carte in chain:
		new_cursor_list_ranges = copy_list_ranges(cursor_list_ranges)
		for c in cartes[ carte ]:
			remaining_cursor_list_ranges = copy_list_ranges(new_cursor_list_ranges)
			done_cursor_list_ranges = []
			while len(remaining_cursor_list_ranges) > 0:
				tmp_remaining_cursor_list_ranges=[]
				for cursor in remaining_cursor_list_ranges:

					# Case 0 seed range is not within the carte range
					if cursor["end"] < c["src"] or cursor["begin"] > c["src"]+c["len"]:
						done_cursor_list_ranges.append(cursor)
						continue

					# Case 1 seed range is completely within the carte range
					if cursor["begin"] >= c["src"] and cursor["end"] <= c["src"]+c["len"]:
						cursor["begin"] = c["dst"]+ (cursor["begin"]-c["src"])
						cursor["end"  ] = c["dst"]+ (cursor["end"  ]-c["src"])
						done_cursor_list_ranges.append(cursor)
						continue

					# Case 2 seed range is a cheval at the beginning of the carte range
					if cursor["begin"] < c["src"] and cursor["end"] <= c["src"]+c["len"]:
						print("case 2")

						split_cursor={"begin": cursor["begin"], "end":c["src"]-1}
						tmp_remaining_cursor_list_ranges.append(split_cursor)

						cursor["begin"] = c["dst"]+ 0 # (cursor["begin"]-c["src"])
						cursor["end"  ] = c["dst"]+ (cursor["end"]-c["src"])
						done_cursor_list_ranges.append(cursor)
						continue

					# Case 3 seed range is a cheval at the end of the carte range
					if cursor["begin"] >= c["src"] and cursor["end"] > c["src"]+c["len"]:
						print("case 3")

						split_cursor={"begin": c["src"]+c["len"]+1, "end":cursor["end"]}
						tmp_remaining_cursor_list_ranges.append(split_cursor)

						cursor["begin"] = c["dst"]+ (cursor["begin"]-c["src"])
						cursor["end"  ] = c["dst"]+ c["len"] # (cursor["end"  ]-c["src"])
						done_cursor_list_ranges.append(cursor)
						continue

				remaining_cursor_list_ranges = tmp_remaining_cursor_list_ranges
			new_cursor_list_ranges = done_cursor_list_ranges
		cursor_list_ranges = new_cursor_list_ranges

	for cursor in cursor_list_ranges:
		if answer == None or cursor["begin"] < answer:
			answer = cursor["begin"]

print("Part 2:", answer-1)
			
