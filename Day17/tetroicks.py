#!/usr/bin/python3

import functools
import sys
from operator import methodcaller

sys.setrecursionlimit(32768)

PART_ONE = False
PART_TWO = False
#PART_ONE = True
PART_TWO = True

f = open("jets.txt", "r")
MINI=False
#f = open("minijets.txt", "r")
#MINI=True

jets = []
for line in f.readlines():
	line = line.strip()

	jets = list(line)



rocks = [ 
	# @@@@
	[ [0,0], [1,0], [2,0], [3,0] ], 

	#  @
	# @@@
	#  @
	[ [0,-1], [1,-1], [2,-1], [1,-2], [1, 0] ], 

	#   @
	#   @
	# @@@
	[ [0,0], [1,0], [2,0], [2,-1], [2, -2] ], 

	# @
	# @
	# @
	# @
	[ [0,0], [0,-1], [0,-2], [0,-3] ], 

	# @@
	# @@
	[ [0,0], [1,0], [0,-1], [1,-1] ],
	]


def print_tower(from_y, number = None):
	print()
	y = 0
	if number != None:
		if from_y+number > len(chamber):
			number = len(chamber)-from_y
		for y in range(from_y, from_y+number):
			print("|"+"".join(chamber[y])+"|")
	else:
		for y in range(from_y, len(chamber)):
			print("|"+"".join(chamber[y])+"|")

	if y == len(chamber)-1:
		print("\-------/")
	else:
		print("[~~~~~~~]")

	
def tower_size(from_bottom=None):

	if from_bottom == None:
		bottom = len(chamber)-1
	else:
		bottom = from_bottom
		if bottom > len(chamber)-1:
			bottom = len(chamber)-1

	while chamber[ bottom ] != [ " ", " ", " ", " ", " ", " ", " " ]:
		bottom -= 1
	
	return bottom


def copy_rock(rock, to_left=False, to_right=False, down=False):
	tmp_rock = []
	for [rx, ry] in rock:
		if to_left:
			rx -= 1
		if to_right:
			rx += 1
		if down:
			ry += 1
		tmp_rock.append([rx, ry])

	return tmp_rock

def rockrain(limit, print_chamber=False):
	jets_index = 0

	history = []

	above = len(chamber)-1
	for rock_count in range(limit):
		rocks_index = rock_count % len(rocks)

		rock = copy_rock( rocks[ rocks_index ] )

		above = tower_size(above+5)-3
		
		# Start the fall
		for r in rock:
			r[0] += 2
			r[1] += above

		#print("Count", rock_count, jets_index, rocks_index)
		#if (jets_index, rocks_index) in history:
		#	print("Repetition on Count", rock_count, jets_index, rocks_index)
		#print_tower(above, 40)

		#print(jets_index, rocks_index)
		#if jets_index == 0 and rocks_index == 0:
		#	print("Rock Count", rock_count)

		history.append( (jets_index, rocks_index) )

		while True: 


			# To the left, to the right
			if jets[jets_index] == "<":
				tmp_rock = copy_rock(rock, to_left=True)
			elif jets[jets_index] == ">":
				tmp_rock = copy_rock(rock, to_right=True)

			jets_index = (jets_index+1) % len(jets)


			can_move = True
			for [rx, ry] in tmp_rock:
				if (rx < 0) or (rx > 6) or (chamber[ry][rx] != " "):
					can_move = False
					break
			if can_move:
				rock = tmp_rock

			# Down
			tmp_rock = copy_rock(rock, down=True)

			can_move_down = True
			for [rx, ry] in tmp_rock:
				if (ry >= len(chamber)) or (chamber[ry][rx] != " "):
					can_move_down = False
					break
			if can_move_down:
				rock = tmp_rock
			else:
				break

		# The rock stays
		for [rx, ry] in rock:
			chamber[ry][rx] = "#"

		# Print a bit
		if print_chamber or (rock_count % 50000 == 0):
			print("\033[H\033[2J")
			print("#"+str(rock_count))
			print_tower(above, 40)

	return len(chamber)-1-tower_size()

def guess_seq_len(seq):
	guess = 1
	max_len = len(seq) // 2
	for x in range(2, max_len):
		if seq[0:x] == seq[x:2*x] :
			return x

	return guess


# Chapter One
if PART_ONE:
	chamber = []
	for line in range(1000000):
		chamber.append( [ " " ] * 7)

	print( "Tower size :", rockrain( 2022, True ))

# Chapter Two
if PART_TWO:
	limit = 1000000000000


	chamber = []
	for line in range(500000):
		chamber.append( [ " " ] * 7)
	rockrain( 50000 )
	
	chamberN = []
	for [a,b,c,d,e,f,g] in chamber:
		a = 0 if a == " " else 1
		b = 0 if b == " " else 1
		c = 0 if c == " " else 1
		d = 0 if d == " " else 1
		e = 0 if e == " " else 1
		f = 0 if f == " " else 1
		g = 0 if g == " " else 1
		x = (a<<7)+(b<<6)+(c<<5)+(d<<4)+(e<<3)+(f<<2)+(g<<1)
		if x > 0:
			chamberN.append(x)
	
	limit_one = guess_seq_len(chamberN)
	print("Repetition from:", limit_one)
	limit_two = limit % limit_one

	chamber = []
	for line in range(500000):
		chamber.append( [ " " ] * 7)
	size_one = rockrain( limit_one )

	chamber = []
	for line in range(500000):
		chamber.append( [ " " ] * 7)
	size_two = rockrain( limit_two )

	#print_tower(tower_size())

	print( "Limits :", limit_one, limit_two)
	print( "Size one :", size_one )
	print( "Size two :", size_two )
	print( "Tower size :", size_one*(limit//limit_one)+size_two )

