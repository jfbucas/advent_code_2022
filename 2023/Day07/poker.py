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



def is_hand_paire1(h):
	for a,b in HAND_TUPLES["paire"]:
		if h[a] == h[b]:
			return { "typerank1":1, "type":"paire", "cards":(a,b) }
	
	return None

def is_hand_double1(h):
	for a,b, d,e in HAND_TUPLES["double"]:
		if h[a] == h[b] and h[d] == h[e]:
			return { "typerank1":2, "type":"double", "cards":(a,b, d,e) }
	
	return None

def is_hand_brelan1(h):
	for a,b,c in HAND_TUPLES["brelan"]:
		if h[a] == h[b] == h[c]:
			return { "typerank1":3, "type":"brelan", "cards":(a,b,c) }
	
	return None

def is_hand_full1(h):
	for a,b,c,d,e in HAND_TUPLES["full"]:
		if h[a] == h[b] == h[c] and h[d] == h[e]:
			return { "typerank1":4, "type":"full", "cards":(a,b,c, d,e) }
	
	return None

def is_hand_carre1(h):
	for a,b,c,d in HAND_TUPLES["carre"]:
		if h[a] == h[b] == h[c] == h[d]:
			return { "typerank1":5, "type":"carre", "cards":(a,b,c,d) }
	
	return None

def is_hand_five1(h):
	if h[0] == h[1] == h[2] == h[3] == h[4]:
		return { "typerank1":6, "type":"five", "cards":(h[0], h[1], h[2], h[3], h[4]) }
	
	return None


def get_hand_type1(h):

	c5 = is_hand_five1(h)
	if c5 != None:
		return c5

	cc = is_hand_carre1(h)
	if cc != None:
		return cc

	cf = is_hand_full1(h)
	if cf != None:
		return cf

	cb = is_hand_brelan1(h)
	if cb != None:
		return cb

	cd = is_hand_double1(h)
	if cd != None:
		return cd

	cp = is_hand_paire1(h)
	if cp != None:
		return cp

	ch = { "typerank1":0, "type": "high", "cards":None }
	return ch


def is_hand_paire2(h):
	for a,b in HAND_TUPLES["paire"]:
		t = h
		if t[a] == "J":
			t[a] = t[b]
		if t[b] == "J":
			t[b] = t[a]

		if t[a] == t[b]:
			return { "typerank2":1, "type":"paire", "cards":(a,b) }
	
	return None

def is_hand_double2(h):
	for a,b, d,e in HAND_TUPLES["double"]:
		t = h
		if t[a] == "J":
			t[a] = t[b]
		if t[b] == "J":
			t[b] = t[a]
		if t[d] == "J":
			t[d] = t[e]
		if t[e] == "J":
			t[e] = t[d]
		if t[a] == t[b] and t[d] == t[e]:
			return { "typerank2":2, "type":"double", "cards":(a,b, d,e) }
	
	return None

def is_hand_brelan2(h):
	for a,b,c in HAND_TUPLES["brelan"]:
		t = h
		if t[a] == "J":
			if t[b] == "J":
				t[a] = t[c]
			else:
				t[a] = t[b]
		if t[b] == "J":
			t[b] = t[c]
		if t[c] == "J":
			t[c] = t[a]
		if t[a] == t[b] == t[c]:
			return { "typerank2":3, "type":"brelan", "cards":(a,b,c) }
	
	return None

def is_hand_full2(h):
	for a,b,c,d,e in HAND_TUPLES["full"]:
		t = h
		if t[a] == "J":
			if t[b] == "J":
				t[a] = t[c]
			else:
				t[a] = t[b]
		if t[b] == "J":
			t[b] = t[c]
		if t[c] == "J":
			t[c] = t[a]
		if t[d] == "J":
			t[d] = t[e]
		if t[e] == "J":
			t[e] = t[d]
		if t[a] == t[b] == t[c] and t[d] == t[e]:
			return { "typerank2":4, "type":"full", "cards":(a,b,c, d,e) }
	
	return None

def is_hand_carre2(h):
	for a,b,c,d in HAND_TUPLES["carre"]:
		if h[a] == h[b] == h[c] == h[d]:
			return { "typerank2":5, "type":"carre", "cards":(a,b,c,d) }
	
	return None

def is_hand_five2(h):
	if h[0] == h[1] == h[2] == h[3] == h[4]:
		return { "typerank2":6, "type":"five", "cards":(h[0], h[1], h[2], h[3], h[4]) }
	
	return None


def get_hand_type1(h):

	c5 = is_hand_five1(h)
	if c5 != None:
		return c5

	cc = is_hand_carre1(h)
	if cc != None:
		return cc

	cf = is_hand_full1(h)
	if cf != None:
		return cf

	cb = is_hand_brelan1(h)
	if cb != None:
		return cb

	cd = is_hand_double1(h)
	if cd != None:
		return cd

	cp = is_hand_paire1(h)
	if cp != None:
		return cp

	ch = { "typerank1":0, "type": "high", "cards":None }
	return ch
def hand_rank1(h):
	r=1
	rank=0
	for c in reversed(h):
		rank += r * CARDS_RANK1.index(c)
		r *= 16
	return rank 

def hand_rank2(h):
	r=1
	rank=0
	for c in reversed(h):
		rank += r * CARDS_RANK2.index(c)
		r *= 16
	return rank 

hands=[]
for line in f.readlines():
	line=line.strip().split(" ")
	hands.append( { "cards":line[0], "bid":int(line[1]) } )

for h in hands:
	h["type1"] = get_hand_type1(h["cards"])
	h["type2"] = get_hand_type2(h["cards"])
	h["cardrank1"] = hand_rank1(h["cards"])
	h["cardrank2"] = hand_rank2(h["cards"])
	h["totalrank1"] = h["type1"]["typerank1"]*(2**22) + h["cardrank1"]
	h["totalrank2"] = h["type2"]["typerank2"]*(2**22) + h["cardrank2"]

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


exit()

time=list(map(int, re.split(r'\s{2,}', lines[0].strip())[1:]))
dist=list(map(int, re.split(r'\s{2,}', lines[1].strip())[1:]))

records=[]
for race in range(len(time)):
	winners=[]

	for button_time in range(time[race]):
		d = button_time * (time[race]-button_time)
		if d > dist[race]:
			winners.append(button_time)
	records.append(len(winners))

answer=1
for r in records:
	answer*=r

print(answer)
			
