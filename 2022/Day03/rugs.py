#!/usr/bin/python3

f = open( "rugs.txt", "r" )

prio = 0

for line in f.readlines():
	line = line.strip()
	s = len(line)
	rug1 = line[:s//2]
	rug2 = line[s//2:]


	common = None
	for c1 in rug1:
		for c2 in rug2:
			if c1 == c2:
				common = c1
				break

		if common != None:
			break
	
	#print( line, rug1, rug2, common )
	
	if common.isupper():
		prio += ord(common) - ord("A") +27
	else:
		prio += ord(common) - ord("a") +1

			
print(prio)
	
