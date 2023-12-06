#!/usr/bin/python3

f = open( "inepoute.txt", "r" )

lenstarter = 4
lenstarter = 14

for line in f.readlines():
	line = line.strip()

	for i in range(0, len(line)-lenstarter):

		pack = line[i:i+lenstarter]

		dupfound = False
		for j in range(lenstarter):
			a = pack[j]
			newpack = pack.replace(a, "")
			if len(newpack) != lenstarter-1:
				dupfound = True
				break

		if not dupfound:
			print(i+lenstarter)
			exit()
