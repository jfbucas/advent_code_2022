#!/usr/bin/python3

import sys
sys.setrecursionlimit(32768)

PROGRESS = True # False #True
PART_ONE = False #True
PART_TWO = True #False

f = open("land.txt", "r")
#f = open("miniland.txt", "r")


recurs_counter = 0

startX = 0
startY = 0
endX = 0
endY = 0

land = []
for line in f.readlines():
	line = line.strip()

	if line.rfind("S") != -1:
		startX = line.rfind("S")
		startY = len(land)

	if line.rfind("E") != -1:
		endX = line.rfind("E")
		endY = len(land)

	land.append([])
	for z in line:
		if z == "S":
			z = "a"
		elif z == "E":
			z = "z"
		land[-1].append(ord(z)-ord("a"))
	
W = len(land[0])
H = len(land)


# Create the Graph
def addnewmove(m, curX, curY, nX, nY, c):
	if (    (land[curY][curX] == land[nY][nX]-1) or \
		(land[curY][curX] == land[nY][nX]+0) or \
		(land[curY][curX] == land[nY][nX]+1) or \
		(land[curY][curX] == land[nY][nX]+2)):
		m.append( (c, nX, nY, (endX-nX)**2 + (endY-nY)**2) )


graph = []
for curY in range(H):
	for curX in range(W):
		moves = []
		if curX > 0:
			addnewmove(moves, curX, curY, curX-1, curY, "<")

		if curX < W-1:
			addnewmove(moves, curX, curY, curX+1, curY, ">")

		if curY > 0:
			addnewmove(moves, curX, curY, curX, curY-1, "^")

		if curY < H-1:
			addnewmove(moves, curX, curY, curX, curY+1, "V")

		# We try the moves that are getting closer to the End first
		moves = sorted(moves, key=lambda x: x[3])

		graph.append(moves)
	






def explore(depth, curX, curY):
	global recurs_counter
	if PROGRESS:
		recurs_counter += 1
		if recurs_counter % 15000 == 0:
			print("\033[H\033[2J")
			for y in range(H):
				print("".join(visited[y*W:(y+1)*W]))

	if curX == endX and curY == endY:
		return (depth, list(visited))


	moves = graph[ curY*W+curX ]

	depths_seen = {}
	for c, x, y, d in moves:
		# If we have visited the place before and the depth was greater
		# we need a revisit => we mark it as unvisited
		if visited[y*W+x] == "x":
			if visited_depth[y*W+x] > depth+2:
				visited[y*W+x] = "."

		# If we have visited the place before, we skip
		if visited[y*W+x] != ".":
			continue

		visited[curY*W+curX] = c
		(depth_seen, v) = explore(depth+1, x, y)
		depths_seen[depth_seen] = v
		visited[curY*W+curX] = "x"
		visited_depth[curY*W+curX] = depth
	
	if len(depths_seen.keys()) > 0:
		m = min(depths_seen.keys())
		return (m, depths_seen[m]) 
	else:
		return (16**16, None)


# From the S
if PART_ONE:
	visited = [ "." ] * (W*H)
	visited_depth = [ 16**16 ] * (W*H)

	result = explore(0, startX, startY)

	#for y in range(H):
	#	print("".join(visited[y*W:(y+1)*W]))

	v = result[1]
	if v != None:
		for y in range(H):
			print("".join(v[y*W:(y+1)*W]).replace("x", " ").replace(".", " "))
	print(result[0])


# List all the A's
if PART_TWO:
	aaa = []
	for curY in range(H):
		for curX in range(W):
			if land[curY][curX] == 0:
				aaa.append( (curX, curY, (endX-curX)**2 + (endY-curY)**2) )
				

	# We sort the A's to get the ones closer to the End first
	aaa = sorted(aaa, key=lambda x: x[2])

	print(aaa)

	aaa_fewest = []
	#for (x, y, _) in aaa[0:100]:
	for (x, y, _) in aaa:
		#print(x, y)
		visited = [ "." ] * (W*H)
		visited_depth = [ 16**16 ] * (W*H)

		aaa_fewest.append( explore(0, x, y) )

	aaa_fewest = sorted(aaa_fewest, key=lambda x: x[0])

	result = aaa_fewest[0]

	v = result[1]
	if v != None:
		for y in range(H):
			print("".join(v[y*W:(y+1)*W]).replace("x", " ").replace(".", " "))
	print(result[0])
