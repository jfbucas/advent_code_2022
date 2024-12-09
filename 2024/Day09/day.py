#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

diskmap=[]

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	diskmap = list(map(int,list(line.strip())))

def expand_diskmap(dm):
	dme = []
	i = 0
	file_id = 0
	for d in dm:
		if i%2 == 0:
			dme.extend( [file_id]*d )
			file_id+=1
		else:
			dme.extend( ["."]*d )
		i+=1
	return dme

def refrag(dme):
	free_indexes=[]
	fileblocks = 0
	i=0
	for d in dme:
		if d == ".":
			free_indexes.append(i)
		else:
			fileblocks+=1
		i+=1
	
	dmed=list(dme)
	last=len(dme)-1
	for i in free_indexes:
		if i >= fileblocks:
			break

		while dme[last] == ".":
			last-=1

		dmed[i] = dme[last]
		dmed[last] = "."
		last-=1

	return dmed

def checksum(dmed):
	cs=0
	i=0
	for d in dmed:
		if d == ".":
			break
		cs += i*d
		i+=1

	return cs


def describe_diskmap(dm):
	i = 0
	file_id = 0
	dmd=[]
	for d in dm:
		if i%2 == 0:
			dmd.append( (d, "file", file_id) )
			file_id+=1
		else:
			dmd.append( (d, "free", None) )
		i+=1

	return dmd
	
def find_next_match(dmd, last_fi, last_si):
	fi = last_fi
	while fi>0:
		if dmd[fi][1] == "free":
			fi-=1
			continue

		f_size,f_type,f_id = dmd[fi]


		si=last_si
		while si<len(dmd)-1 and si<fi:
			if dmd[si][1] == "file":
				si+=1
				continue

			s_size,s_type,s_id = dmd[si]
			if f_size <= s_size:
				# Found a space
				return fi, si
			si+=1
		fi-=1
	return None
				

def defrag(old_dmd):
	dmd=list(old_dmd)
	i=0
	last_fi = len(dmd) -1
	last_si = 0
	while True:
		fnm=find_next_match(dmd, last_fi, 0)
		if fnm==None:
			break

		fi,si = fnm
		last_fi,last_si = fnm

		# Same size? we just swap
		if dmd[si][0] == dmd[fi][0]:
			tmp=dmd[si]
			dmd[si]=dmd[fi]
			dmd[fi]=tmp
		elif dmd[fi][0] < dmd[si][0]:

			diff = dmd[si][0]-dmd[fi][0]
			tmp=dmd[si]
			dmd[si]=dmd[fi]
			dmd[fi]=tmp

			dmd.insert(si+1, (diff, "free", None))
			fi+=1
			last_fi+=1
			dmd[fi] = (dmd[fi][0]-diff, "free", None) 
		else:
			print("ERROR")

		# Merge Free space
		if fi>0 and fi<len(dmd)-1 and dmd[fi-1][1] == "free" and dmd[fi+1][1] == "free":
			dmd[fi-1] = (dmd[fi-1][0]+dmd[fi][0]+dmd[fi+1][0], "free", None) 
			dmd.pop(fi)
			dmd.pop(fi)
			last_fi-=2

		elif fi>0 and dmd[fi-1][1] == "free":
			dmd[fi-1] = (dmd[fi-1][0]+dmd[fi][0], "free", None) 
			dmd.pop(fi)
			last_fi-=1
		elif fi< len(dmd)-1 and dmd[fi+1][1] == "free":
			dmd[fi+1] = (dmd[fi+1][0]+dmd[fi][0], "free", None) 
			dmd.pop(fi)
			last_fi-=1

	return dmd

def expand_described_diskmap(dmd):
	dmde = []
	for d in dmd:
		if d[1] == "file":
			dmde.extend( [d[2]]*d[0] )
		else:
			dmde.extend( ["."]*d[0] )
	return dmde

def checksum_described(dmded):
	cs=0
	i=0
	for d in dmded:
		if d != ".":
			cs += i*d
		i+=1

	return cs


############################
# Part 1

total=checksum(refrag(expand_diskmap(diskmap)))
print("Part1:", total)

############################
# Part 2

total=checksum_described(expand_described_diskmap(defrag(describe_diskmap(diskmap))))
print("Part2:", total)

