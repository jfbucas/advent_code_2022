#!/usr/bin/python3

import re
import sys
import itertools

f = open( sys.argv[1], "r" )

CARDS_RANK1="23456789TJQKA"
CARDS_RANK2="J23456789TQKA"
HAND_SIZE=5

HAND_TUPLES = {
	"paire"  : list(itertools.combinations(range(HAND_SIZE), 2)),
	"brelan" : list(itertools.combinations(range(HAND_SIZE), 3)),
	"carre"  : list(itertools.combinations(range(HAND_SIZE), 4)),
	"full"   : list([ (a,b,c, d,e) for (a,b,c),(d,e) in itertools.product(itertools.combinations(range(HAND_SIZE), 3), itertools.combinations(range(HAND_SIZE), 2)) if d not in [a, b, c] and e not in [a, b, c]]),
	"double" : list([ (a,b,   d,e) for (a,b  ),(d,e) in itertools.product(itertools.combinations(range(HAND_SIZE), 2), itertools.combinations(range(HAND_SIZE), 2)) if d not in [a, b   ] and e not in [a, b   ]]),
}



def is_hand_paire(h):
	for a,b in HAND_TUPLES["paire"]:
		if h[a] == h[b]:
			return { "typerank":1, "type":"paire", "cards":(a,b) }
	
	return None

def is_hand_double(h):
	for a,b, d,e in HAND_TUPLES["double"]:
		if h[a] == h[b] and h[d] == h[e]:
			return { "typerank":2, "type":"double", "cards":(a,b, d,e) }
	
	return None

def is_hand_brelan(h):
	for a,b,c in HAND_TUPLES["brelan"]:
		if h[a] == h[b] == h[c]:
			return { "typerank":3, "type":"brelan", "cards":(a,b,c) }
	
	return None

def is_hand_full(h):
	for a,b,c,d,e in HAND_TUPLES["full"]:
		if h[a] == h[b] == h[c] and h[d] == h[e]:
			return { "typerank":4, "type":"full", "cards":(a,b,c, d,e) }
	
	return None

def is_hand_carre(h):
	for a,b,c,d in HAND_TUPLES["carre"]:
		if h[a] == h[b] == h[c] == h[d]:
			return { "typerank":5, "type":"carre", "cards":(a,b,c,d) }
	
	return None

def is_hand_five(h):
	if h[0] == h[1] == h[2] == h[3] == h[4]:
		return { "typerank":6, "type":"five", "cards":(h[0], h[1], h[2], h[3], h[4]) }
	
	return None


def get_hand_type(h):

	c5 = is_hand_five(h)
	if c5 != None:
		return c5

	cc = is_hand_carre(h)
	if cc != None:
		return cc

	cf = is_hand_full(h)
	if cf != None:
		return cf

	cb = is_hand_brelan(h)
	if cb != None:
		return cb

	cd = is_hand_double(h)
	if cd != None:
		return cd

	cp = is_hand_paire(h)
	if cp != None:
		return cp

	ch = { "typerank":0, "type": "high", "cards":None }
	return ch

def get_hand_type2(h):
	best_type = get_hand_type(h)
	if "J" in h:
		for c in CARDS_RANK2[1:]:
			t = h.replace("J", c, 1)
			new_type = get_hand_type2(t)
			if new_type["typerank"] > best_type["typerank"]:
				best_type = new_type
	
	return best_type


def hand_rank(h, card_rank):
	r=1
	rank=0
	for c in reversed(h):
		rank += r * card_rank.index(c)
		r *= 16
	return rank 

hands=[]
for line in f.readlines():
	line=line.strip().split(" ")
	hands.append( { "cards":line[0], "bid":int(line[1]) } )

for h in hands:
	h["type1"] = get_hand_type(h["cards"])
	h["type2"] = get_hand_type2(h["cards"])

	h["cardrank1"] = hand_rank(h["cards"], CARDS_RANK1)
	h["cardrank2"] = hand_rank(h["cards"], CARDS_RANK2)
	h["totalrank1"] = h["type1"]["typerank"]*(2**22) + h["cardrank1"]
	h["totalrank2"] = h["type2"]["typerank"]*(2**22) + h["cardrank2"]

hands1 = sorted(hands, key=lambda h: h['totalrank1'])

total_bids1=0
for h, p in zip(hands1,range(1,len(hands1)+1)):
	total_bids1 += h["bid"] * p

print(total_bids1)


hands2 = sorted(hands, key=lambda h: h['totalrank2'])

total_bids2=0
for h, p in zip(hands2,range(1,len(hands2)+1)):
	total_bids2 += h["bid"] * p

print(total_bids2)

