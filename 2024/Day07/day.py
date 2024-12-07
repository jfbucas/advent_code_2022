#!/usr/bin/python3

import re
import sys
import itertools
import math
import random

sys.setrecursionlimit(150000)

operations = {}

f = open( sys.argv[1], "r" )
y=0
for line in f.readlines():
	line = line.strip().split(": ")
	key=int(line[0])
	operations[key] = list(map(int,line[1].split(" ")))

#print(operations)
#exit()

def ternary (n):
	if n == 0:
		return '0'
	nums = []
	while n:
		n, r = divmod(n, 3)
		nums.append(str(r))

	return ''.join(reversed(nums))


############################
# Part 1

total=0
for result,numbers in operations.items():
	for b in range(1<<len(numbers)-1):
		s = format(b,'#050b').replace("0b","")
		sb = s[-(len(numbers)-1):].replace("0", "*").replace("1", "+") + " "
		sbl = list(sb)
		sblp = [ ")"+x for x in sbl ]

		tmp_result = eval( "("*len(numbers) +"".join([str(a)+str(b) for a,b in zip(numbers,sblp)]))
		if tmp_result == result:
			total+=result
			break
	

	
print("Part1:", total)

############################
# Part 2

total=0
for result,numbers in operations.items():
	ln=len(numbers)
	for b in range(pow(3,ln-1)):
		s = ternary(b).rjust(len(numbers)-1, "0")
		sb = s[-(len(numbers)-1):].replace("0", "*").replace("1", "+").replace("2", "|") + " "
		sbl = list(sb)
		sblp = [ ")"+x for x in sbl ]
		sblpe = "".join([str(a)+str(b) for a,b in zip(numbers,sblp)])
		sblpes = sblpe.split(")|")

		presese=""
		for se in sblpes:
			ses = "("*(se.count(")"))+presese+se
			presese = str(eval(ses))

		if int(presese) == result:
			total+=result
			break

print("Part2:", total)

