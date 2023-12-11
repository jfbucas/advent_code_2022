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

games = {}
f = open( sys.argv[1], "r" )
for line in f.readlines():
	line=line.strip()
	line=line.split(":")
	game_id=int(line[0].replace("Game ",""))
	draws=line[1].split(";")
	games[game_id]=[]
	for d in draws:
		drawset={"red":0, "blue":0, "green":0}
		d=d.replace("  "," ")
		colors=d.split(",")
		for c in colors:
			c=c.split(" ")
			cubes=int(c[1])
			cubecolor=c[2]
			drawset[cubecolor] = cubes
		games[game_id].append(drawset)

print(games)
impossible_games = []
for g in games.keys():
	for d in games[g]:
		# only 12 red cubes, 13 green cubes, and 14 blue cubes
		if d["red"] > 12 or d["green"] > 13 or d["blue"] > 14:
			impossible_games.append(g)
			print("Impossible: ", d)

possible_games = []
for g in games.keys():
	if g not in impossible_games:
		possible_games.append(g)

possible_games=list(set(possible_games))
print(possible_games)
print(sum(possible_games))


def game_power(game):
	mindraw={"red":None, "blue":None, "green":None}
	for d in games[game]:
		for c in d.keys():
			if mindraw[c] == None:
				mindraw[c] = d[c]
			elif mindraw[c] < d[c]:
				mindraw[c] = d[c]
	

	power=1
	for c in mindraw.keys():
		power *= mindraw[c]

	return power
	
total = 0
for g in games.keys():
	total += game_power(g)

print(total)
