#!/usr/bin/python3

import functools
import sys
from operator import methodcaller
import itertools

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
PART_ONE = True
#PART_TWO = True

# cat factory.txt | tr -d "[a-zA-Z:.]" | tr -s " " > factory-tr.txt
f = open("factory-tr2.txt", "r")
MINI=False
f = open("minifactory-tr.txt", "r")
MINI=True

"""Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."""

blueprints = {}
for line in f.readlines():
	line = line.strip()

	line = list(map(int,line.split(" ")))
	blueprints[line[0]] = line[1:]

#print(blueprints)



def build_n_collect(time, blueprint,  rob_ore, rob_clay, rob_obs, rob_geo,  res_ore, res_clay, res_obs, res_geo):
	global global_recurs_count, global_best_geo, global_recurs_count_limit

	# Cache to speed things up
	key = str(time)+"_"+str(rob_ore)+"_"+str(rob_clay)+"_"+str(rob_obs)+"_"+str(rob_geo)+"_"+str(res_ore)+"_"+str(res_clay)+"_"+str(res_obs)+"_"+str(res_geo)
	if key in cache:
		return cache[key]

	# Out of time
	if time > 23:
		if res_geo > global_best_geo:
			global_best_geo = res_geo
			print("    !!! Time", time, "Blueprint", blueprint, "Robots", rob_ore, rob_clay, rob_obs, rob_geo, "Resources", res_ore, res_clay, res_obs, res_geo, "Best", global_best_geo)
		cache[key] = res_geo
		return res_geo

	# If we're searching too hard
	if global_recurs_count > global_recurs_count_limit:
		return 0
	
	# Heuristics
	if (heuristic_rob_min[time][0] > rob_ore) or \
		(heuristic_rob_min[time][1] > rob_clay) or \
		(heuristic_rob_min[time][2] > rob_obs) or \
		(heuristic_rob_min[time][3] > rob_geo) or \
		(heuristic_rob_max[time][0] < rob_ore) or \
		(heuristic_rob_max[time][1] < rob_clay) or \
		(heuristic_rob_max[time][2] < rob_obs) or \
		(heuristic_rob_max[time][3] < rob_geo):
		cache[key] = 0
		return 0


	possibilities = []

	# If we don't build a robot, only collect resources
	possibilities.append( (0,0,0,0, 0,0,0,0) )

	# Build a rob_ore
	if res_ore >= blueprints[blueprint][0]:
		possibilities.append( (1,0,0,0, blueprints[blueprint][0],0,0,0) )

	# Build a rob_clay
	if res_ore >= blueprints[blueprint][1]:
		possibilities.append( (0,1,0,0, blueprints[blueprint][1],0,0,0) )

	# Build a rob_obs
	if (res_ore >= blueprints[blueprint][2]) and (res_clay >= blueprints[blueprint][3]):
		possibilities.append( (0,0,1,0, blueprints[blueprint][2],blueprints[blueprint][3],0,0) )
		
	# Build a rob_geo
	if (res_ore >= blueprints[blueprint][4]) and (res_obs >= blueprints[blueprint][5]):
		possibilities.append( (0,0,0,1, blueprints[blueprint][4],0,blueprints[blueprint][5],0) )
	

	# Collect resources
	best_geo = 0
	for new_rob_ore, new_rob_clay, new_rob_obs, new_rob_geo, used_res_ore, used_res_clay, used_res_obs, used_res_geo in possibilities:
		tmp_geo = build_n_collect(time+1, blueprint, rob_ore+new_rob_ore, rob_clay+new_rob_clay, rob_obs+new_rob_obs, rob_geo+new_rob_geo,  res_ore+rob_ore-used_res_ore, res_clay+rob_clay-used_res_clay, res_obs+rob_obs-used_res_obs, res_geo+rob_geo-used_res_geo)
		if tmp_geo > best_geo:
			best_geo = tmp_geo
	
	# Some info on recursion
	global_recurs_count += 1
	recurs_count_time[ time ] += 1
	#if global_recurs_count % 750000 == 0:
	#	print("        Time", time, "Blueprint", blueprint, "Robots", rob_ore, rob_clay, rob_obs, rob_geo, "Resources", res_ore, res_clay, res_obs, res_geo, "Best", best_geo, "Recurs", recurs_count_time)

	cache[key] = best_geo
	return best_geo



# Chapter One
if PART_ONE:
	quality_levels = []
	for b in blueprints.keys():

		global_best_geo = 0
		product = itertools.product( [1], [1], [1], [1])
		"""
		if MINI:
			product = []
			if b == 1:
				product = itertools.product( [3], [6,7], [11], [18,19])
			if b == 2:
				product = itertools.product( [5,6], [7,8], [8,9,10,11,12,13,14], [18,19])
		else:
			product = itertools.product( [5,6], [7,8,9,10,11,12,13,14,15,16], [8,9,10,11,12,13,14,15,16,17,18], [16,17,18,19,20,21])
			product = itertools.product( range(5,9), range(7,25), range(8,18), range(16,22) )
			product = itertools.product( range(5,25), range(7,25), range(8,25), range(10,25) )
		"""

#Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 20 obsidian.
#Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 9 clay. Each geode robot costs 3 ore and 9 obsidian.

		for heuristic_rob_max_ore, \
			heuristic_rob_max_clay, \
			index_heuristic_rob_min_obs, \
			index_heuristic_rob_min_geo \
			in product:
			#itertools.product( [7,6,5,4,3,2], [4,5,6,7,8], [8,9,10,11,12,13,14]):
			#in itertools.product( [3], [6,7], [11]):
			#in [ [2,6,11] ]:


			heuristic_rob_min = [
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
				[0, 0, 0, 0]
				]

			heuristic_rob_max = [
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25],
				[25, 25, 25, 25]
				]

			"""
			for h in range(len(heuristic_rob_max)):
				heuristic_rob_max[h][0] = heuristic_rob_max_ore

			for h in range(len(heuristic_rob_max)):
				heuristic_rob_max[h][1] = heuristic_rob_max_clay

			heuristic_rob_min[index_heuristic_rob_min_obs][2] = 1 # We need a Obsidian robot as early as possible
			heuristic_rob_min[index_heuristic_rob_min_geo][3] = 1 # Same for Geode robot
			"""

			global_recurs_count = 0
			global_recurs_count_limit = 2000000 * 100
			recurs_count_time = [ 0 ] * 25

			cache = {}
			geo = build_n_collect(0, b, 1,0,0,0, 0,0,0,0)
			#if geo != 0:
			print("Heuristics: rob_max_ore", heuristic_rob_max_ore, 
			"rob_max_clay", heuristic_rob_max_clay,
			"Index_rob_min_obs", index_heuristic_rob_min_obs,
			"Index_rob_min_geo", index_heuristic_rob_min_geo,
			" : ", end="")
			print("--| Blueprint", b, "collected", geo, "geodes in", global_recurs_count, "recursion |---------------")
			#else:
			#	index_heuristic_rob_min_obs += 1

		if global_best_geo > 0:
			print("=====================================================")
			print("|||")
			print("||| Blueprint", b, "collected", global_best_geo, "geodes")
			print("|||")
			print("=====================================================")

		quality_levels.append( global_best_geo * b )
	
	print("Sum of quality levels", sum(quality_levels), "   (", quality_levels, ")")

# Chapter Two
if PART_TWO:
	pass
