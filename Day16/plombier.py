#!/usr/bin/python3

import functools
import sys
from operator import methodcaller

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
PART_ONE = True
PART_TWO = True

f = open("pipes.txt", "r")
MINI=False
#f = open("minipipes.txt", "r")
#MINI=True

total_rate = 0
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
	total_rate += rate

#print(valves)
print("Total rate", total_rate)


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

def visitationPart2_A(time, name0, name1, released):

	global total_rate

	# Sum released
	added = 0
	for o in valves["open"]:
		added += valves[o]["rate"]

	# Heuristic
	if added < ref_sum[25-time]:
		return
	
	# Speedup the search
	if added == total_rate:
		new_released = released + total_rate*(time+1)
		visitationPart2_B(0, name0, name1, new_released)
		return
	
	valves["visited"].append("A:"+name0+"*"+name1)
	valves["released"].append(added)
	new_released = released + added

	# Do we consider opening the valve?
	if (valves[name0]["rate"] > 0) and (name0 not in valves["open"]):
		valves["open"].append(name0)
		visitationPart2_B(time, name0, name1, new_released)
		valves["open"].pop()

	# Visit the connected tunnels
	for t in valves[name0]["tunnels"]:
		visitationPart2_B(time, t, name1, new_released)

	valves["visited"].pop()
	valves["released"].pop()

	return

def visitationPart2_B(time, name0, name1, released):

	if time == 0:
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
	
	# Do we consider opening the valve?
	if (valves[name1]["rate"] > 0) and (name1 not in valves["open"]):
		valves["open"].append(name1)
		visitationPart2_A(time-1, name0, name1, released)
		valves["open"].pop()

	# Visit the connected tunnels
	for t in valves[name1]["tunnels"]:
		visitationPart2_A(time-1, name0, t, released)

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
	print(best_visited)
	print(best_open)
	print(best_released)


# Chapter Two
if PART_TWO:
	if MINI:
		ref_sum = [0, 0, 20, 41, 41, 41, 41, 76, 76, 76, 56, 81, 81, 59, 59, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81]
		ref_sum = [x-1 if x>0 else 0 for x in ref_sum ]

	else: 
		ref_sum = [0, 0, 0, 0, 0, 0, 10, 10, 10, 21, 21, 21, 40, 40, 40, 40, 60, 60, 60, 90, 90, 90, 90, 100, 100, 100, 120, 120, 120, 120, 140, 140, 140, 0]
		ref_sum = [0, 0, 0, 0, 0, 0, 10, 10, 10, 20, 20, 20, 56, 56, 56, 70, 70, 70, 70, 100, 100, 100, 100, 147, 147, 147]
		ref_sum = [0, 0, 0, 0, 0, 10, 10, 10, 10, 20, 20, 20, 56, 56, 56, 70, 70, 70, 70, 100, 100, 100, 100, 147, 147, 147]
		ref_sum = [0, 0, 0, 0, 10, 10, 10, 20, 10, 20, 20, 20, 56, 56, 56, 70, 70, 70, 70, 100, 100, 100, 100, 147, 147, 147]
		ref_sum = [0, 0, 0, 0, 10, 10, 10, 20, 20, 20, 63, 63, 63, 63, 82, 93, 93, 115, 132, 132, 132, 178, 178, 178, 201, 201]
		ref_sum = [0, 0, 0, 0, 15, 15, 15, 25, 49, 49, 65, 85, 85, 85, 104, 121, 121, 143, 164, 164, 164, 212, 212, 212, 212, 212]
		ref_sum = [0, 0, 0, 0, 11, 21, 21, 21, 63, 63, 63, 94, 94, 94, 111, 111, 111, 151, 151, 151, 196, 196, 196, 196, 221, 221]
		ref_sum = [0, 0, 0, 18, 33, 33, 44, 44, 68, 68, 78, 98, 98, 114, 114, 135, 135, 154, 177, 177, 199, 199, 199, 216, 241, 241]
		ref_sum = [0, 0, 0, 0, 0, 18, 33, 33, 44, 44, 68, 68, 78, 98, 98, 114, 114, 135, 135, 154, 177, 177, 199, 199, 199, 216, 241, 241]
		ref_sum = [0, 0, 0, 18, 33, 33, 44, 44, 68, 85, 85, 85, 125, 125, 125, 170, 170, 170, 170, 195, 195, 215, 215, 215, 215, 215]
		#ref_sum = [x-1 if x>0 else 0 for x in ref_sum ]

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
	visitationPart2_A(25, "AA", "AA", 0)

	print(leaves)
	print(max_released)
	print(best_visited)
	print(best_open)
	print(best_released)
