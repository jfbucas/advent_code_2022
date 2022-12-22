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

chamber = []

def print_tower(chamber, from_y, number = None, start_y_repetition = 0, repetition_period = None):
	print()
	y = 0
	if number != None:
		if from_y+number > len(chamber):
			number = len(chamber)-from_y
		for y in range(from_y, from_y+number):
			syr = ""
			if start_y_repetition != 0:
				if len(chamber)-1-y == start_y_repetition:
					syr = " Start Repetition"
			rp = ""
			if repetition_period != None:
				if (len(chamber)-1-y-start_y_repetition) % repetition_period == 0:
					rp = " Repetition Period "+str(repetition_period)
			print("|"+"".join(chamber[y])+"| "+str(y)+" "+str(len(chamber)-1-y)+syr+rp)
	else:
		for y in range(from_y, len(chamber)):
			syr = ""
			if start_y_repetition != 0:
				if len(chamber)-1-y == start_y_repetition:
					syr = " Start Repetition"
			rp = ""
			if repetition_period != None:
				if (len(chamber)-1-y-start_y_repetition) % repetition_period == 0:
					rp = " Repetition Period "+str(repetition_period)
			print("|"+"".join(chamber[y])+"| "+str(y)+" "+str(len(chamber)-1-y)+syr+rp)

	if y == len(chamber)-1:
		print("\-------/")
	else:
		print("[~~~~~~~]")

	
def tower_size(chamber, from_bottom=None):

	
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

def rockrain(limit, tower_size_limit=None, print_chamber=False):

	jets_index = 0

	above = len(chamber)-1
	for rock_count in range(limit):
		rocks_index = rock_count % len(rocks)

		rock = copy_rock( rocks[ rocks_index ] )

		above = tower_size(chamber, above+5)

		# To find how many rocks it takes to reach a specific size
		#print("Rockcount :", rock_count, len(chamber)-1-above)
		if tower_size_limit != None:
			if (len(chamber)-1-above) >= tower_size_limit:
				print("Size limit reached:", rock_count, above)
				return rock_count

		above -= 3
		
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

		#history.append( (jets_index, rocks_index) )

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
		#if print_chamber or (rock_count % 50000 == 0):
		if print_chamber:
			print("\033[H\033[2J")
			print("#"+str(rock_count))
			print_tower(chamber, above, 40)

	return len(chamber)-1-tower_size(chamber)

def guess_seq_len(seq):
	for startx in [ 25, 1666 ]:
		if startx % 10 == 0:
			print( "Search for match at", startx )
		max_len = len(seq) // 2
		for x in range(30, max_len):
			if seq[startx+0:startx+x] == seq[startx+x:startx+2*x] :
				print( "Repetition Match:", startx, x )
				#print( " -> ", seq[startx+0:startx+x] )
				#print( " -> ", seq[startx+x:startx+2*x] )
				return (startx, x)

	return (0, 1)


# Chapter One
if PART_ONE:
	print( "Tower size :", rockrain( 2022, True ))

# Chapter Two
if PART_TWO:
	rocks_to_simulate = 1000000000000

	# Fill the chamber with 10000 rocks to try to detect a repetition
	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	tmp = rockrain( 10000 )
	
	# Convert to numbers
	chamberN = []
	for [a,b,c,d,e,f,g] in list(reversed(chamber)): #chamber:
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
	print("Tower size:", len(chamberN), tmp)
	
	(repetition_start, repetition_size) = guess_seq_len(chamberN)
	print("Repetition starts at",  repetition_start, "and has size",  repetition_size)
	#for n in range(0,4):
	#	print( chamberN[repetition_start+repetition_size*n:repetition_start+repetition_size*(n+1)] )

	# Find the number of rocks necessary for the start/repetitions/remaining parts
	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	rocks_count_start = rockrain( 10000, tower_size_limit=repetition_start )

	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	rocks_count_one = rockrain( 10000, tower_size_limit=repetition_start+repetition_size )

	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	rocks_count_two = rockrain( 10000, tower_size_limit=repetition_start+repetition_size*2 )
	
	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	rocks_count_three = rockrain( 10000, tower_size_limit=repetition_start+repetition_size*3 )
	
	# Check the periodicity is regular
	if rocks_count_three - rocks_count_two != rocks_count_two - rocks_count_one:
		print("Strange, no periodicity!")
		exit()
	rock_period = rocks_count_three - rocks_count_two

	rocks_remain =  (rocks_to_simulate-rocks_count_start) % rock_period

	print("Number of rocks for periodicity: start", rocks_count_start, " | period", rock_period, " | remain", rocks_remain)


	# Find the tower size for the start/1 repetition/remaining parts
	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	tower_size_start = rockrain( rocks_count_start )
	#print_tower(chamber, tower_size(chamber), start_y_repetition = tower_size_start)

	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	tower_size_start_repetition = rockrain( rocks_count_start+rock_period )
	#print_tower(chamber, tower_size(chamber), start_y_repetition = tower_size_start, repetition_period = repetition_size)

	chamber = []
	for line in range(100000):
		chamber.append( [ " " ] * 7)
	tower_size_start_repetition_remain = rockrain( rocks_count_start+rock_period+rocks_remain )
	print_tower(chamber, tower_size(chamber), start_y_repetition = tower_size_start, repetition_period = repetition_size)

	print("Start", rocks_count_start,"=", tower_size_start)
	print("Start/Repetition", rocks_count_start,"+", rock_period,"=", tower_size_start_repetition )
	print("Start/Repetition/Remain", rocks_count_start,"+", rock_period,"+", rocks_remain,"=", tower_size_start_repetition_remain)
	print("Total rocks", rocks_count_start,"+", rock_period, "*", ((rocks_to_simulate-rocks_count_start)//rock_period), "+", rocks_remain,"=", rocks_count_start+rock_period*((rocks_to_simulate-rocks_count_start)//rock_period)+rocks_remain)

	size = tower_size_start + (tower_size_start_repetition-tower_size_start)*((rocks_to_simulate-rocks_count_start)//rock_period) + (tower_size_start_repetition_remain - tower_size_start_repetition)
	size = (tower_size_start_repetition-tower_size_start)*(((rocks_to_simulate-rocks_count_start)//rock_period)-1) + tower_size_start_repetition_remain

	print( "Tower size :", size, " - incorrect result for the actual simulation" )

