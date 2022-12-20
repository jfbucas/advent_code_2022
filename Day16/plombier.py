#!/usr/bin/python3

import functools
import sys
from operator import methodcaller

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
#PART_ONE = True
PART_TWO = True

f = open("pipes.txt", "r")
MINI=False
f = open("minipipes.txt", "r")
MINI=True

valves = {}
for line in f.readlines():
	line = line.strip()

	line = line.split(";")
	name = line[0].split(" ")[1]
	rate = int(line[0].split("=")[1])

	tunnels = line[1].replace(" tunnel leads to valve ", "").replace(" tunnels lead to valves ", "").replace(",", "").split(" ")
	valves[name] = {}
	valves[name]["rate"] = rate
	valves[name]["tunnels"] = tunnels

#print(valves)


def visitationPart1(time, name, released):
	
	if time <= 0:
		global leaves, max_released, best_visited, best_open, best_released

		leaves += 1
		if released > max_released:
			max_released = released
			best_visited = list(valves["visited"])
			best_open = list(valves["open"])
			best_released = list(valves["released"])

		if leaves % 10000 == 0:
			print(leaves, max_released, best_visited, best_released)

		return

	# Heuristic
	if valves["sum"] < ref_sum[30-time]:
		return
	
	valves["visited"].append(name)
	valves["released"].append(valves["sum"])

	# Do we consider opening the valve?
	if (valves[name]["rate"] > 0) and (name not in valves["open"]):
		current_sum = valves["sum"]
		valves["open"].append(name)
		valves["sum"] += valves[name]["rate"]
		visitationPart1(time-1, name, released+current_sum)
		valves["sum"] -= valves[name]["rate"]
		valves["open"].pop()

	# Visit the connected tunnels
	for t in valves[name]["tunnels"]:
		visitationPart1(time-1, t, released+valves["sum"])

	valves["visited"].pop()
	valves["released"].pop()

	return

def visitationPart2(time, zeroone, name0, name1, released):

	if time <= 0:
		global leaves, max_released, best_visited, best_open, best_released

		leaves += 1
		if released > max_released:
			max_released = released
			best_visited = list(valves["visited"])
			best_open = list(valves["open"])
			best_released = list(valves["released"])

		if leaves % 50000 == 0:
			print(leaves, max_released, best_visited, best_released)

		return

	
	if zeroone == 1:
		added = 0
		for o in valves["open"]:
			added += valves[o]["rate"]

		# Heuristic
		if added < ref_sum[26-time]:
			return
		
		valves["released"].append(added)
		new_released = released + added

	
	valves["visited"].append(str(zeroone)+":"+name0+"*"+name1)

	# Do we consider opening the valve?
	if zeroone == 0:
		if (valves[name0]["rate"] > 0) and (name0 not in valves["open"]):
			valves["open"].append(name0)
			visitationPart2(time, 1, name0, name1, released)
			valves["open"].pop()
	else:
		if (valves[name1]["rate"] > 0) and (name1 not in valves["open"]):
			valves["open"].append(name1)
			visitationPart2(time-1, 0, name0, name1, new_released)
			valves["open"].pop()

	# Visit the connected tunnels
	if zeroone == 0:
		for t in valves[name0]["tunnels"]:
			visitationPart2(time, 1, t, name1, released)
	else:
		for t in valves[name1]["tunnels"]:
			visitationPart2(time-1, 0, name0, t, new_released)

	valves["visited"].pop()
	if zeroone == 1:
		valves["released"].pop()

	return



# Chapter One
if PART_ONE:

	if MINI:
		ref_sum = [0, 0, 20, 20, 20, 30, 30, 30, 30, 50, 50, 50, 50, 50, 50, 50, 50, 70, 70, 70, 70, 70, 70, 7, 80, 80, 80, 80, 80, 80]
	else: 
		ref_sum = [0, 0, 0, 0, 0, 0, 10, 10, 10, 21, 21, 21, 40, 40, 40, 40, 60, 60, 60, 90, 90, 90, 90, 100, 100, 100, 120, 120, 120, 120, 140, 140, 140, 0]

	valves["sum"] = 0
	valves["visited"] = []
	valves["open"] = []
	valves["released"] = []


	leaves = 0
	max_released = 0
	best_visited = []
	best_open = []
	best_released = []

	# Start the Recursion
	visitationPart1(30, "AA", 0)

	print(leaves)
	print(max_released)
	print(len(best_visited))
	print(best_visited)
	print(best_open)
	print(best_released)


# Chapter Two
if PART_TWO:
	if MINI:
		ref_sum = [0, 20, 20, 20, 20, 30, 30, 30, 30, 50, 50, 50, 50, 50, 50, 50, 50, 80, 80, 80, 80, 80, 80, 80, 80, 80]
		ref_sum = [x-1 if x>0 else 0 for x in ref_sum ]

	else: 
		ref_sum = [0, 0, 0, 0, 0, 0, 10, 10, 10, 21, 21, 21, 40, 40, 40, 40, 60, 60, 60, 90, 90, 90, 90, 100, 100, 100, 120, 120, 120, 120, 140, 140, 140, 0]

	valves["sum"] = 0
	valves["visited"] = []
	valves["open"] = []
	valves["released"] = []


	leaves = 0
	max_released = 0
	best_visited = []
	best_open = []
	best_released = []

	# Start the Recursion
	visitationPart2(26, 0, "AA", "AA", 0)

	print(leaves)
	print(max_released)
	print(len(best_visited))
	print(best_visited)
	print(best_open)
	print(best_released)
