#!/usr/bin/python3

f = open( "rugs.txt", "r" )

prio = 0

groups = []

group = []
for line in f.readlines():
	group.append(line.strip())
	if len(group) == 3:
		groups.append(group)
		group = []

for [rug1, rug2, rug3] in groups:

	common = None
	for c1 in rug1:
		for c2 in rug2:
			if c1 == c2:
				for c3 in rug3:
					if c1 == c3:
						common = c1
						break

				if common != None:
					break
		if common != None:
			break
	
	print( line, rug1, rug2, rug3, common )
	
	if common.isupper():
		prio += ord(common) - ord("A") +27
	else:
		prio += ord(common) - ord("a") +1

			
print(prio)
	
