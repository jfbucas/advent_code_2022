#!/usr/bin/python3

f = open( "inepoute.txt", "r" )

initial_position = \
"""
                                      // Empty line first 
    [S] [C]         [Z]            
[F] [J] [P]         [T]     [N]    
[G] [H] [G] [Q]     [G]     [D]    
[V] [V] [D] [G] [F] [D]     [V]    
[R] [B] [F] [N] [N] [Q] [L] [S]    
[J] [M] [M] [P] [H] [V] [B] [B] [D]
[L] [P] [H] [D] [L] [F] [D] [J] [L]
[D] [T] [V] [M] [J] [N] [F] [M] [G]
"""
initial_position = initial_position.split("\n")

crates = { }
for stack in [ 1,   2,   3,   4,   5,   6,   7,   8,   9 ]:
	crates[stack] = []
	for h in reversed(range(len(initial_position)-1)):
		crate = initial_position[h][(stack-1)*4+1]
		if crate == " ":
			break
		crates[stack].append(crate)

#print(crates)


for line in f.readlines():
	if not line.startswith("move"):
		continue

	line = line.strip()
	line = line.split(" ")

	count = int(line[1])
	sfrom = int(line[3])
	sto   = int(line[5])

	cs = crates[sfrom][-count:]
	crates[sto].extend(cs)
	for n in range(count):
		crates[sfrom].pop()

result = ""
for stack in crates.keys():
	result += crates[stack].pop()

print(result)
