#!/usr/bin/python3

import re
import sys
import itertools
import math

f = open( sys.argv[1], "r" )


cards=[]
for line in f.readlines():
	line=line.strip()
	numbers=line.split(":")[1]
	numbers.replace("  "," ")
	numbers.replace("  "," ")
	numbers.replace("  "," ")
	winning=list(map(int, [ n for n in numbers.split("|")[0].split(" ") if n != "" ]))
	scratch=list(map(int, [ n for n in numbers.split("|")[1].split(" ") if n != "" ]))
	cards.append( {"copies": 1, "winning":sorted(winning), "scratch":sorted(scratch)} )

def we_got_a_winner(card):
	points = 0
	for n in card["scratch"]:
		if n in card["winning"]:
			points += 1

	if points > 0:
		points = 1 << (points-1)

	return points
	
def we_got_a_copier(card):
	copies = 0
	for n in card["scratch"]:
		if n in card["winning"]:
			copies += 1

	return copies
	
# Part 1
total = 0
for c in cards:
	print( c, we_got_a_winner(c) )
	total += we_got_a_winner(c)

print(total)

# Part 2
total = 0
c = 0
new_cards = []
while c < len(cards):
	copy = we_got_a_copier(cards[c])
	print( c, copy )
	for i in range(1,copy+1):
		if c+i < len(cards):
			cards[c+i]["copies"] += cards[c]["copies"]
	c += 1

for c in cards:
	print( c )
print(sum([ c["copies"] for c in cards]))

exit()

def get_next(h):
	if h == [ 0 ]*len(h):
		return 0
	
	meta_h = []
	a = h[0]
	for b in h[1:]:
		meta_h.append(b-a)
		a = b

	return h[-1] + get_next(meta_h)

total = 0
for h in histories:
	total += get_next(h)
	#print(h, get_next(h))

print(total)

total = 0
for h in histories:
	total += get_next(list(reversed(h)))
	#print(h, get_next(h))

print(total)

exit()


#print(instructions)
#print(network)

cursor = "AAA"
i = 0
steps = 0
while cursor != "ZZZ":
	cursor = network[cursor][instructions[i]]
	i+=1
	if i >= len(instructions):
		i = 0
	steps+=1

print(steps)


# Part 2
cursors = [ x for x in network.keys() if x.endswith("A") ]

def period_length(cursor):
	i = 0
	steps = 0
	while True:
		cursor = network[cursor][instructions[i]]
		steps += 1
		i+=1
		if i >= len(instructions):
			i = 0
		if cursor[2] == "Z":
			return steps


all_periods=[]
for c in cursors:
	all_periods.append(period_length(c))


a=all_periods[0]
multi=1
for p in all_periods[1:]:
	b=p
	while True:
		if a*multi % b == 0:
			print("Found multiple:", multi)
			a = a*multi
			multi=1
			break
		multi += 1
print(a)

#for p in all_periods:
#	print(p)
#	#print(math.gcd(largest, p[0]))


exit()

i = 0
steps = 0
END = "Z" * len(cursors)
while "".join([ x[2] for x in cursors ]) != END:

	for c in range(len(cursors)):
		#if cursors[c][2] != "Z":
		cursors[c] = network[cursors[c]][instructions[i]]

	i += 1
	if i >= len(instructions):
		i = 0
		print( "".join([ x[2] for x in cursors ]), END)
	steps += 1

print(steps)
